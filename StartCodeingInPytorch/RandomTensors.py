import matplotlib.pyplot as plt
import torch
import matplotlib.pyplot

random = torch.rand((1,2))
random_normal = torch.randn((1,2))

rand = 2*torch.randn(10000)+1.2
plt.hist(rand,100)
plt.show()

rand_perm = torch.randperm(10)

torch.manual_seed(50)
rand_perm = torch.randperm(10)
