import torch
from torch import nn
from torch.utils.data import DataLoader
from torch.optim import Adam
from torchvision.datasets import CIFAR10
import torchvision.transforms as T


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


if __name__ == "__main__":
    # take best model possible
    class FourthModel(nn.Module):
        def __init__(self):
            super().__init__()

            self.net = nn.Sequential(
                nn.Conv2d(in_channels=3, out_channels=32, kernel_size=3, padding=1),  # 32 x 32 x 32
                nn.BatchNorm2d(32),
                nn.ReLU(),

                nn.MaxPool2d(2),  # 16 x 16 x 32
                nn.Dropout2d(p=0.2),

                nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, padding=1),  # 16 x 16 x 64
                nn.BatchNorm2d(64),
                nn.ReLU(),

                nn.MaxPool2d(2),  # 8 x 8 x 32
                nn.Dropout2d(p=0.2),

                nn.Flatten(),

                nn.Linear(8 * 8 * 32 * 2, 512),
                nn.BatchNorm1d(512),
                nn.Dropout(p=0.3),
                nn.ReLU(),
                nn.Linear(512, 10)
            )

        def forward(self, x):
            return self.net(x)



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


    def whole_train_valid_cycle(model, num_epochs, title):
        train_loss_history, valid_loss_history = [], []
        train_accuracy_history, valid_accuracy_history = [], []

        for epoch in range(num_epochs):
            train_loss, train_accuracy = train(model)
            valid_loss, valid_accuracy = evaluate(model, valid_loader)

            train_loss_history.append(train_loss)
            valid_loss_history.append(valid_loss)

            train_accuracy_history.append(train_accuracy)
            valid_accuracy_history.append(valid_accuracy)

            clear_output()

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

    whole_train_valid_cycle(model, 20, 'Fourth super advanced model + best learned augmentations')

    print(predict(model, valid_loader, device))

    torch.save(predict(model, valid_loader, device), 'predict.pt')
