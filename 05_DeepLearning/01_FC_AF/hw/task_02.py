import torch


def function02(tensor: torch.Tensor) -> torch.Tensor:
    row_length = tensor.shape[1]
    return torch.tensor(torch.rand(row_length), dtype=torch.float32, requires_grad=True)
