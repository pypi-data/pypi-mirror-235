# -*- coding: utf-8 -*-

import torch.nn as nn
import torch.nn.functional as F
from torch_geometric.nn import MessagePassing

"""# GNN Model"""

class GNNLayer(MessagePassing):
  def __init__(self, in_channels, out_channels):
    super(GNNLayer, self).__init__(aggr='add')
    self.lin = nn.Linear(in_channels, out_channels)

  def forward(self, x, edge_index, edge_index_inter):
    # Convert x to the same dtype
    x = x.to(self.lin.weight.dtype)
    return self.propagate(edge_index, x=x, edge_index_inter=edge_index_inter)

  def message(self, x_i, x_j):
    return self.lin(x_j - x_i)

class GNN(nn.Module):
  def __init__(self, in_channels, hidden_channels, out_channels, num_layers):
    super(GNN, self).__init__()
    self.conv1 = GNNLayer(in_channels, hidden_channels)
    self.convs = nn.ModuleList()
    for _ in range(num_layers-2):
        self.convs.append(GNNLayer(hidden_channels, hidden_channels))
    self.conv2 = GNNLayer(hidden_channels, out_channels)

  def forward(self, x, edge_index, edge_index_inter):
    x = self.conv1(x, edge_index, edge_index_inter)
    for conv in self.convs:
        x = conv(x, edge_index, edge_index_inter)
    x = self.conv2(x, edge_index, edge_index_inter)
    # x = F.relu(x) #
    # x = F.dropout(x, p=0.25,training=self.training) #
    return x

"""# GIN Model"""

##
# GIN is a type of graph convolutional network that generalizes the GNN by adding
# an additional layer of non-linear transformations.
##
class GINLayer(MessagePassing):
  def __init__(self, in_channels, out_channels):
    super(GINLayer, self).__init__(aggr='add')
    self.mlp = nn.Sequential(
      nn.Linear(in_channels, out_channels),
      nn.ReLU(),
      nn.Linear(out_channels, out_channels)
    )

  def forward(self, x, edge_index, edge_attr):
    x = x.to(self.mlp[0].weight.dtype)
    return self.propagate(edge_index, x=x, edge_attr=edge_attr)

  def message(self, x_j, edge_attr):
    return x_j

class GIN(nn.Module):
  def __init__(self, in_channels, hidden_channels, out_channels, num_layers):
    super(GIN, self).__init__()
    self.conv1 = GINLayer(in_channels, hidden_channels)
    self.convs = nn.ModuleList()
    for _ in range(num_layers - 2):
      self.convs.append(GINLayer(hidden_channels, hidden_channels))
    self.conv2 = GINLayer(hidden_channels, out_channels)

  def forward(self, x, edge_index, edge_attr):
    x = self.conv1(x, edge_index, edge_attr)
    for conv in self.convs:
      x = conv(x, edge_index, edge_attr)
    x = self.conv2(x, edge_index, edge_attr)
    return x

###

def custom_loss(embeddings_graph1, embeddings_graph2):
  # Calculate cosine similarity
  cosine_sim = F.cosine_similarity(embeddings_graph1, embeddings_graph2)
  # A negative cosine_sim maximizes the cosine similarity
  loss = -cosine_sim.mean()
  return loss