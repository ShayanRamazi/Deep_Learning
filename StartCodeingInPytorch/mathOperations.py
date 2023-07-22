import torch

x1 = torch.randint(10,(2,2))
x2 = torch.randint(10,(2,2))

print(x1,x2)

print(x1+x2)
print(x1-x2)
print(x1*x2)
print(x1/x2)
print(x1@x2)
print(x1+5)

a = torch.zeros((3,3))
b = torch.arange(0,3)
print(a+b)