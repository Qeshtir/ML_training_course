import torch
from torch import nn


def function04(x: torch.Tensor, y: torch.Tensor):
    step_size = 1e-2
    n_steps = 200
    row_length = x.shape[1]
    layer = nn.Linear(in_features=row_length, out_features=1)
    for i in range(n_steps):
        y_pred = layer(x).ravel()
        mse = torch.mean((y_pred - y) ** 2)
        if i < 20 or i % 10 == 0:
            print(f'MSE на шаге {i + 1} {mse.item():.5f}')

        mse.backward()

        with torch.no_grad():
            layer.weight -= layer.weight.grad * step_size
            layer.bias -= layer.bias.grad * step_size
        layer.zero_grad()
    return layer


if __name__ == "__main__":
    n_features = 2  # Размерность указана для примера, не нужно использовать её в коде
    n_objects = 300

    w_true = torch.randn(n_features)
    X = (torch.rand(n_objects, n_features) - 0.5) * 5
    Y = X @ w_true + torch.randn(n_objects) / 2

    function04(X, Y)