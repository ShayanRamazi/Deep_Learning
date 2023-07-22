import torch.nn as nn
import torch
import torch.nn.functional as F

mse = nn.MSELoss()
print(mse(torch.tensor(1.),torch.tensor(1.)))
print(F.mse_loss(torch.tensor(1.),torch.tensor(1.)))