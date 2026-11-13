from pathlib import Path
import matplotlib.pyplot as plt

import torch
import torchvision
from torchvision.transforms import v2
from torch.utils.data import DataLoader

ROOT = f"{Path.home()}/sgoinfre"


def main() -> None:
    """Load FashionMNIST and print its sizes."""
    torch.manual_seed(42)
    training_data = torchvision.datasets.FashionMNIST(
        root=ROOT,
        train=True,
        download=True,
        transform=v2.Compose([
            v2.ToImage(),
            v2.ToDtype(torch.float32, scale=True),
        ]),
    )

    test_data = torchvision.datasets.FashionMNIST(
        root=ROOT,
        train=False,
        download=True,
        transform=v2.Compose([
            v2.ToImage(),
            v2.ToDtype(torch.float32, scale=True),
        ]),
    )
    train_dataloader = DataLoader(training_data, batch_size=64, shuffle=True)
    test_dataloader = DataLoader(test_data, batch_size=64, shuffle=True)

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
        sample_idx = torch.randint(len(training_data), size=(1,)).item()
        img, label = training_data[sample_idx]
        figure.add_subplot(rows, cols, i)
        plt.title(labels_map[label])
        plt.axis("off")
        plt.imshow(img.squeeze(), cmap="gray")
    plt.show()

    # Display image and label.
    train_features, train_labels = next(iter(train_dataloader))
    print(f"Feature batch shape: {train_features.size()}")
    print(f"Labels batch shape: {train_labels.size()}")
    img = train_features[0].squeeze()
    label = train_labels[0]
    plt.imshow(img, cmap="gray")
    plt.show()
    print(f"Label: {label}")


if __name__ == "__main__":
    main()
