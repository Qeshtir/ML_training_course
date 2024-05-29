from torch import nn


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


def create_advanced_skip_connection_conv_cifar():
    return FourthModel()
