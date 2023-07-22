import torch

x = torch.tensor([[1., 2., 0., 4., 1.],
                  [0., 1., 1., 1., 1.],
                  [2., 3., 0., 1., 4.]
                  ])

w = torch.tensor([1., 0.5, 1., -1, -0.5])

b = torch.tensor(1.)


def neuron(x, w, b, af):
    y = af(x@w + b)
    return y


def linear(x):
    return x

def step(x):
    if x > 0:
        y = torch.tensor(1.)
    elif x > 0:
        y = torch.tensor(0.)
    else:
        y = torch.tensor(0.5)
    return y

class Neorun:

    def __init__(self, m, af):
        self.w = torch.randn(m)
        self.b = torch.randn(1)
        self.af = af

    def __call__(self,x):
        self.y = self.af(self.w@x+self.b)