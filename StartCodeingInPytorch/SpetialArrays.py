import torch

ones = torch.ones((10, 2), device='cuda', dtype=torch.uint8)
zeros = torch.zeros((2, 3, 6), device='cpu', dtype=torch.uint8)
eyes = torch.eye(1, device='cuda')
emp = torch.empty((2, 3), device='cuda')
print(emp)
print(emp.fill_(0.1))
print(emp.zero_())
print(torch.full((2,3),10.))
print(torch.zeros_like(emp))
print(torch.full_like(emp,2.3))