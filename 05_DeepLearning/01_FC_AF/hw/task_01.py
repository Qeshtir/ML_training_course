import torch


def function01(tensor: torch.Tensor, count_over: str) -> torch.Tensor:
    if count_over == 'columns':
        return tensor.mean(dim=0)
    else:
        return tensor.mean(dim=1)
    