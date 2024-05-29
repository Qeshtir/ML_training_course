from torch import nn


def create_simple_conv_cifar() -> nn.Sequential:
    net = nn.Sequential(
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
    return net
