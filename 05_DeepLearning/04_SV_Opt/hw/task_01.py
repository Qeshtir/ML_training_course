import torch

def get_normalize(features: torch.Tensor):
    mean = features.mean(dim=(0,2,3))
    std = features.std(dim=(0,2,3))
    return mean, std


if __name__ =="__main__":
    batch = torch.rand((5, 4, 3, 3))
    print(batch)
    print(get_normalize(batch))
