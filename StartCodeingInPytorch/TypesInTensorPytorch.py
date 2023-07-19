import torch

scaler = torch.tensor(2.6)
print(scaler.dtype)

tensor = torch.tensor([1, 3, 5], dtype=torch.float16)
print(tensor.dtype)

tensor = torch.tensor([1, -1], dtype=torch.uint8)
print(tensor)

print(tensor.float())
tensor = tensor.dtype(torch.bool)
