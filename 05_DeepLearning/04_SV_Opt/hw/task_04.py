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


if __name__ == "__main__":
    class FirstModel(nn.Module):
        def __init__(self):
            super().__init__()

            self.net = nn.Sequential(
                nn.Conv2d(in_channels=3, out_channels=16, kernel_size=3, padding=1),  # 32 x 32 x 16
                nn.ReLU(),

                nn.MaxPool2d(2),  # 16 x 16 x 16

                nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, padding=1),  # 16 x 16 x 32
                nn.ReLU(),

                nn.MaxPool2d(2),  # 8 x 8 x 32

                nn.Flatten(),

                nn.Linear(8 * 8 * 32, 1024),
                nn.ReLU(),
                nn.Linear(1024, 128),
                nn.ReLU(),
                nn.Linear(128, 10)
            )

        def forward(self, x):
            return self.net(x)


    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

    print(device)
    print(torch.cuda.get_device_name())

    loss_fn = nn.CrossEntropyLoss()

    model = FirstModel().to(device)
    from torch.optim import Adam
    optimizer = Adam(model.parameters(), lr=1e-3)

    from torchvision.datasets import CIFAR10
    import torchvision.transforms as T

    dataset_train = CIFAR10('C:\\Users\\realn\\PycharmProjects\\ML_training_course\\05_DeepLearning\\datasets\\cifar',
                            train=True, transform=T.ToTensor())
    means = (dataset_train.data / 255).mean(axis=(0, 1, 2))
    stds = (dataset_train.data / 255).std(axis=(0, 1, 2))



    transforms = T.Compose(
        [
            T.ToTensor(),
            T.Normalize(mean=means, std=stds)
        ]
    )

    from torch.utils.data import DataLoader

    train_dataset = CIFAR10('C:\\Users\\realn\\PycharmProjects\\ML_training_course\\05_DeepLearning\\datasets\\cifar',
                            train=True, transform=transforms)
    valid_dataset = CIFAR10('C:\\Users\\realn\\PycharmProjects\\ML_training_course\\05_DeepLearning\\datasets\\cifar',
                            train=False, transform=transforms)

    train_loader = DataLoader(train_dataset, batch_size=128, shuffle=True, num_workers=8, pin_memory=True)
    valid_loader = DataLoader(valid_dataset, batch_size=128, shuffle=False, num_workers=8, pin_memory=True)

    predict_tta(model, valid_loader, device)