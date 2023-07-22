import torch

vec = torch.tensor([[2.3, 2.6, 5.3], [2.3, 2.6, 5.3]])
print(vec.shape)
print(vec.mean())
print(vec.std())
print(vec.var())    
print(vec.t())
print(vec.ceil())
# ceil with change
print(vec.ceil_())
