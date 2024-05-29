from torch import nn


def create_advanced_conv_cifar() -> nn.Sequential:
    net = nn.Sequential(
            nn.Conv2d(in_channels=3, out_channels=64, kernel_size=3, padding=1),  # 32 x 32 x 64
            nn.BatchNorm2d(64),
            nn.ReLU(),

            nn.Conv2d(in_channels=64, out_channels=64, kernel_size=3, padding=1),  # 32 x 32 x 64
            nn.BatchNorm2d(64),
            nn.ReLU(),

            nn.MaxPool2d(2, stride=2),  # 16 x 16 x 64
            nn.Dropout2d(p=0.25),


            nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3, padding=1),  # 16 x 16 x 128
            nn.BatchNorm2d(128),
            nn.ReLU(),


            nn.Conv2d(in_channels=128, out_channels=128, kernel_size=3, padding=1),  # 16 x 16 x 128
            nn.BatchNorm2d(128),
            nn.ReLU(),


            nn.MaxPool2d(2, stride=2),  # 8 x 8 x 128
            nn.Dropout2d(p=0.25),

            nn.Conv2d(in_channels=128, out_channels=256, kernel_size=3, padding=1),  # 8 x 8 x 256
            nn.BatchNorm2d(256),
            nn.ReLU(),


            nn.Conv2d(in_channels=256, out_channels=256, kernel_size=3, padding=1),  # 8 x 8 x 256
            nn.BatchNorm2d(256),
            nn.ReLU(),


            nn.Conv2d(in_channels=256, out_channels=256, kernel_size=3, padding=1),  # 8 x 8 x 256
            nn.BatchNorm2d(256),
            nn.ReLU(),

            nn.Conv2d(in_channels=256, out_channels=256, kernel_size=3, padding=1),  # 8 x 8 x 256
            nn.BatchNorm2d(256),
            nn.ReLU(),

            nn.MaxPool2d(2, stride=2),  # 4 x 4 x 256
            nn.Dropout2d(p=0.25),

            nn.Flatten(),

            nn.Linear(4 * 4 * 128 * 2, 1024),
            nn.BatchNorm1d(1024),
            nn.Dropout(p=0.5),
            nn.ReLU(),


            nn.Linear(1024, 1024),
            nn.BatchNorm1d(1024),
            nn.Dropout(p=0.5),
            nn.ReLU(),
            nn.Linear(1024, 10)
        )
    return net
