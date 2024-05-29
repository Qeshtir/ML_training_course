import torch
from torch import nn
from torch.utils.data import DataLoader


@torch.inference_mode
def predict_tta(model: nn.Module, loader: DataLoader, device: torch.device, iterations: int = 2):
    model.eval()
    full_preds = []
    while iterations != 0:
        predicts = []
        for x, y in loader:

            x, y = x.to(device), y.to(device)

            output = model(x)
            predicts.append(output)

        full_preds.append(torch.vstack(predicts))
        iterations -= 1

    full_preds = torch.stack(full_preds).mean(dim=0)
    _, y_pred = torch.max(full_preds, 1)

    return y_pred