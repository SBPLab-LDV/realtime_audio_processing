import torch.nn as nn

class SimpleNetwork(nn.Module):
    def __init__(self):
        super(SimpleNetwork, self).__init__()
        self.identity = nn.Identity()

    def forward(self, x):
        return self.identity(x)