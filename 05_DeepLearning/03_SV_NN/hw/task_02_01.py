import torch.nn as nn

def create_mlp_model():
    first_model = nn.Sequential(
        nn.Flatten(),
        nn.Linear(28 * 28, 392),
        nn.ReLU(),
        nn.Linear(392, 10)
    )
    return first_model