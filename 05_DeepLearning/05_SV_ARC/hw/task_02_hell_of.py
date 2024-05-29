import torch
from torch import nn
from torch.utils.data import DataLoader
from torch.optim import Adam
from torchvision.datasets import CIFAR10
import torchvision.transforms as T
from torch.optim.lr_scheduler import StepLR, ReduceLROnPlateau


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
    # take best model possible
    class FourthModel(nn.Module):
        def __init__(self):
            super().__init__()

            self.layer1 = nn.Sequential(
                nn.Conv2d(in_channels=3, out_channels=64, kernel_size=3, padding=1),  # 32 x 32 x 32
                nn.BatchNorm2d(64),
                nn.ReLU()
            )

            self.layer2 = nn.Sequential(
                nn.Conv2d(in_channels=64, out_channels=64, kernel_size=3, padding=1),  # 32 x 32 x 32
                nn.BatchNorm2d(64),
                nn.ReLU(),


            )

            self.layer3 = nn.Sequential(
                nn.MaxPool2d(2, stride=2),  # 16 x 16 x 32
                nn.Dropout2d(p=0.25),
                nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3, padding=1),  # 16 x 16 x 64
                nn.BatchNorm2d(128),
                nn.ReLU(),
            )

            self.layer4 = nn.Sequential(
                nn.Conv2d(in_channels=128, out_channels=128, kernel_size=3, padding=1),  # 16 x 16 x 64
                nn.BatchNorm2d(128),
                nn.ReLU(),


            )

            self.layer5 = nn.Sequential(
                nn.MaxPool2d(2, stride=2),  # 8 x 8 x 32
                nn.Dropout2d(p=0.25),
                nn.Conv2d(in_channels=128, out_channels=256, kernel_size=3, padding=1),  # 8 x 8 x 128
                nn.BatchNorm2d(256),
                nn.ReLU(),
            )
            self.layer6 = nn.Sequential(
                nn.Conv2d(in_channels=256, out_channels=256, kernel_size=3, padding=1),  # 8 x 8 x 128
                nn.BatchNorm2d(256),
                nn.ReLU(),
            )

            self.layer7 = nn.Sequential(
                nn.Conv2d(in_channels=256, out_channels=256, kernel_size=3, padding=1),  # 8 x 8 x 128
                nn.BatchNorm2d(256),
                nn.ReLU(),
            )

            self.layer8 = nn.Sequential(
                nn.Conv2d(in_channels=256, out_channels=256, kernel_size=3, padding=1),  # 8 x 8 x 128
                nn.BatchNorm2d(256),
                nn.ReLU(),


            )

            self.layer9 = nn.Sequential(
                nn.MaxPool2d(2, stride=2),  # 4 x 4 x 128
                nn.Dropout2d(p=0.25),
                nn.Flatten(),

                nn.Linear(4 * 4 * 128 * 2, 1024),
                nn.BatchNorm1d(1024),
                nn.Dropout(p=0.5),
                nn.ReLU(),
            )

            self.layer10 = nn.Sequential(
                nn.Linear(1024, 1024),
                nn.BatchNorm1d(1024),
                nn.Dropout(p=0.5),
                nn.ReLU(),
                nn.Linear(1024, 10)
            )

        def forward(self, x):
            x = self.layer1(x)
            x = self.layer2(x) + x
            x = self.layer3(x)
            x = self.layer4(x) + x
            x = self.layer5(x)
            x = self.layer6(x) + x
            x = self.layer7(x) + x
            x = self.layer8(x) + x
            x = self.layer9(x)
            x = self.layer10(x)

            return x


    device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')

    print(device)
    print(torch.cuda.get_device_name())

    loss_fn = nn.CrossEntropyLoss()

    from tqdm import tqdm


    def train(model) -> float:
        model.train()

        train_loss = 0
        total = 0
        correct = 0

        for x, y in tqdm(train_loader, desc='Train'):
            x, y = x.to(device), y.to(device)

            optimizer.zero_grad()

            output = model(x)

            loss = loss_fn(output, y)

            train_loss += loss.item()

            loss.backward()

            optimizer.step()

            _, y_pred = torch.max(output, 1)
            total += y.size(0)
            correct += (y_pred == y).sum().item()

        train_loss /= len(train_loader)
        accuracy = correct / total

        return train_loss, accuracy


    @torch.inference_mode()
    def evaluate(model, loader) -> tuple[float, float]:
        model.eval()

        total_loss = 0
        total = 0
        correct = 0

        for x, y in tqdm(loader, desc='Evaluation'):
            x, y = x.to(device), y.to(device)

            output = model(x)

            loss = loss_fn(output, y)

            total_loss += loss.item()

            _, y_pred = torch.max(output, 1)
            total += y.size(0)
            correct += (y_pred == y).sum().item()

        total_loss /= len(loader)
        accuracy = correct / total

        return total_loss, accuracy


    @torch.inference_mode()
    def evaluate(model, loader) -> tuple[float, float]:
        model.eval()

        total_loss = 0
        total = 0
        correct = 0

        for x, y in tqdm(loader, desc='Evaluation'):
            x, y = x.to(device), y.to(device)

            output = model(x)

            loss = loss_fn(output, y)

            total_loss += loss.item()

            _, y_pred = torch.max(output, 1)
            total += y.size(0)
            correct += (y_pred == y).sum().item()

        total_loss /= len(loader)
        accuracy = correct / total

        return total_loss, accuracy


    from IPython.display import clear_output

    import matplotlib.pyplot as plt
    def plot_stats(
            train_loss: list[float],
            valid_loss: list[float],
            train_accuracy: list[float],
            valid_accuracy: list[float],
            title: str
    ):
        plt.figure(figsize=(16, 8))

        plt.title(title + ' loss')

        plt.plot(train_loss, label='Train loss')
        plt.plot(valid_loss, label='Valid loss')
        plt.legend()
        plt.grid()

        plt.show()

        plt.figure(figsize=(16, 8))

        plt.title(title + ' accuracy')

        plt.plot(train_accuracy, label='Train accuracy')
        plt.plot(valid_accuracy, label='Valid accuracy')
        plt.legend()
        plt.grid()

        plt.show()


    def whole_train_valid_cycle_with_scheduler(model, num_epochs, title):
        train_loss_history, valid_loss_history = [], []
        train_accuracy_history, valid_accuracy_history = [], []

        for epoch in range(num_epochs):
            train_loss, train_accuracy = train(model)
            valid_loss, valid_accuracy = evaluate(model, valid_loader)
            print(valid_accuracy)

            train_loss_history.append(train_loss)
            valid_loss_history.append(valid_loss)

            train_accuracy_history.append(train_accuracy)
            valid_accuracy_history.append(valid_accuracy)

            clear_output()

            scheduler1.step()

        plot_stats(
           train_loss_history, valid_loss_history,
           train_accuracy_history, valid_accuracy_history,
           title
        )

    dataset_train = CIFAR10('C:\\Users\\realn\\PycharmProjects\\ML_training_course\\05_DeepLearning\\datasets\\cifar',
                            train=True, transform=T.ToTensor())
    means = (dataset_train.data / 255).mean(axis=(0, 1, 2))
    stds = (dataset_train.data / 255).std(axis=(0, 1, 2))

    train_transforms = T.Compose(
        [
            T.AutoAugment(T.AutoAugmentPolicy.CIFAR10),
            T.ToTensor(),
            T.Normalize(mean=means, std=stds)
        ]
    )

    test_transforms = T.Compose(
        [
            T.ToTensor(),
            T.Normalize(mean=means, std=stds)
        ]
    )

    train_dataset = CIFAR10('C:\\Users\\realn\\PycharmProjects\\ML_training_course\\05_DeepLearning\\datasets\\cifar', train=True, transform=train_transforms)
    valid_dataset = CIFAR10('C:\\Users\\realn\\PycharmProjects\\ML_training_course\\05_DeepLearning\\datasets\\cifar', train=False, transform=test_transforms)

    train_loader = DataLoader(train_dataset, batch_size=128, shuffle=True, num_workers=8, pin_memory=True)
    valid_loader = DataLoader(valid_dataset, batch_size=128, shuffle=False, num_workers=8, pin_memory=True)

    model = FourthModel().to(device)

    optimizer = Adam(model.parameters(), lr=1e-3)
    scheduler1 = StepLR(optimizer, step_size=25)

    whole_train_valid_cycle_with_scheduler(model, 40,
                                           'Fourth super advanced model + best learned augmentations + lr schedule')

    print(predict_tta(model, valid_loader, device))

    torch.save(predict_tta(model, valid_loader, device), 'predict_04.pt')
