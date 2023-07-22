import torch

a = torch.eye(10)
print(torch.sum(a))
print(torch.sum(a,0))
print(torch.cumsum(a,1))
print(torch.diff(a))
print(torch.prod(a))