import torch
from torch import nn
from torch.utils.data import DataLoader


@torch.inference_mode
def predict(model: nn.Module, loader: DataLoader, device: torch.device):
    model.eval()
    predicts = []

    for x, y in loader:

        x, y = x.to(device), y.to(device)

        output = model(x)
        _, y_pred = torch.max(output, 1)
        predicts.append(y_pred)
    result = torch.cat(predicts)
    return result