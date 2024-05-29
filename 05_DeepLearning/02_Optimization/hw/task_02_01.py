import torch.nn as nn
from torch.utils.data import DataLoader
from torch.optim import Optimizer

def train(model: nn.Module, data_loader: DataLoader, optimizer: Optimizer, loss_fn):
    model.train()

    loss_sum = 0

    for x, y in data_loader:

        optimizer.zero_grad()

        output = model(x)

        loss = loss_fn(output, y)

        loss.backward()

        print(f'{loss.item():.5f}')

        optimizer.step()

        loss_sum += loss.item()

    return loss_sum/len(data_loader)