import torchvision.transforms as T


def get_augmentations(train: bool = True) -> T.Compose:
    means = (0.49139968, 0.48215841, 0.44653091)
    stds = (0.24703223, 0.24348513, 0.26158784)

    if train:
        transforms = T.Compose(
            [
                T.Resize((224, 224)),
                T.AutoAugment(T.AutoAugmentPolicy.CIFAR10),
                T.ToTensor(),
                T.Normalize(mean=means, std=stds),

            ]
        )
        return transforms
    else:
        transforms = T.Compose(
            [
                T.Resize((224, 224)),
                T.ToTensor(),
                T.Normalize(mean=means, std=stds),

            ]
        )
        return transforms


if __name__ == "__main__":
    from torchvision.datasets import CIFAR10

    train_dataset = CIFAR10('../datasets/cifar', train=True)
    valid_dataset = CIFAR10('../datasets/cifar', train=False)

    means = (train_dataset.data / 255).mean(axis=(0, 1, 2))
    stds = (train_dataset.data / 255).std(axis=(0, 1, 2))