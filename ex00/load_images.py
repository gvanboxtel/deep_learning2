from pathlib import Path
import matplotlib.pyplot as plt

import torch
import torchvision
from torchvision.transforms import v2

ROOT = f"{Path.home()}/Documents"


def load_datasets() -> tuple[torchvision.datasets.FashionMNIST,
                             torchvision.datasets.FashionMNIST]:
    """Load the FashionMNIST training and test sets as float tensors.

    Returns:
        The training set and the test set.
    """
    transform = v2.Compose([
        v2.ToImage(),
        v2.ToDtype(torch.float32, scale=True),
    ])
    training_data = torchvision.datasets.FashionMNIST(
        root=ROOT, train=True, download=True, transform=transform,
    )
    test_data = torchvision.datasets.FashionMNIST(
        root=ROOT, train=False, download=True, transform=transform,
    )
    return training_data, test_data


def save_samples(dataset: torchvision.datasets.FashionMNIST) -> None:
    """Save a 3x3 grid of random images with their labels."""
    labels_map = {
        0: "T-Shirt",
        1: "Trouser",
        2: "Pullover",
        3: "Dress",
        4: "Coat",
        5: "Sandal",
        6: "Shirt",
        7: "Sneaker",
        8: "Bag",
        9: "Ankle Boot",
    }
    figure = plt.figure(figsize=(8, 8))
    cols, rows = 3, 3
    for i in range(1, cols * rows + 1):
        sample_idx = int(torch.randint(len(dataset), size=(1,)).item())
        img, label = dataset[sample_idx]
        figure.add_subplot(rows, cols, i)
        plt.title(labels_map[label])
        plt.axis("off")
        plt.imshow(img.squeeze(), cmap="gray")
    figure.savefig("Nice_clothes")


def main() -> None:
    """Load FashionMNIST, print its sizes and save sample images."""
    torch.manual_seed(42)
    training_data, test_data = load_datasets()

    print(f'training data num: {len(training_data)}')
    print(f'test data num: {len(test_data)}')

    print(f"shape of a single image: {training_data[0][0].shape}")
    print(f"Number of classes: {len(training_data.classes)}")

    save_samples(training_data)


if __name__ == "__main__":
    main()
