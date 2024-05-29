import torch
import torch.nn as nn
from collections import OrderedDict



def create_model():
    net = nn.Sequential(
        OrderedDict(
            [
                ('linear1', nn.Linear(100, 10)),
                ('relu1', nn.ReLU()),
                ('linear2', nn.Linear(10, 1)),
            ]
        )
    )
    return net


if __name__ == "__main__":
    print(create_model())