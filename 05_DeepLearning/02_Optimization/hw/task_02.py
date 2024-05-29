import torch
import torch.nn as nn
from torch.utils.data import DataLoader, TensorDataset
from torch import optim
from torch.optim import Optimizer
import logging

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)


def train(model: nn.Module, data_loader: DataLoader, optimizer: Optimizer, loss_fn):
    model.train()

    loss_sum = 0

    for i, (x, y) in enumerate(data_loader):

        optimizer.zero_grad()

        output = model(x)

        loss = loss_fn(output, y)

        loss.backward()

        logger.info(f'MSE на шаге {i} {loss.item():.5f}')

        optimizer.step()

        loss_sum += loss.item()

    return loss_sum/len(data_loader)


if __name__ == "__main__":
    n_features = 2
    n_objects = 300

    class CustomTaskNetwork(nn.Module):
        def __init__(self):
            super().__init__()

            self.linear = nn.Linear(n_features, 1)

        def forward(self, x):
            return self.linear(x)

    torch.manual_seed(0)
    w_true = torch.randn(n_features)
    X = (torch.rand(n_objects, n_features) - 0.5) * 10
    X *= (torch.arange(n_features) * 2 + 1)
    Y = (X @ w_true + torch.randn(n_objects)).unsqueeze(1)

    net = CustomTaskNetwork()

    optimizer = optim.Adam(net.parameters(), lr=1e-1)

    loss_fn = nn.MSELoss()

    dataset = TensorDataset(X, Y)

    loader = DataLoader(dataset, batch_size=4, shuffle=True)
    logger.info(len(loader))

    logger.info(train(net, loader, optimizer, loss_fn))
