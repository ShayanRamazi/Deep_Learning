import torch

vec = torch.tensor(2.6, device='cuda')
print(vec)

vec_cpu = torch.tensor(2.3, device='cpu')
vec_cpu = vec_cpu.cuda()
print(vec_cpu)
