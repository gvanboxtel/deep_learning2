from pathlib import Path
import torch
import torchvision

ROOT = f'{Path.home()}/sgoinfre'

def main() -> None:
    """Load FashionMNIST and print its sizes."""
    torch.manual_seed(42)
    mnist_dataset = torchvision.datasets.FashionMNIST(root=ROOT, train=True, download=True)

    data_loader = torch.utils.data.DataLoader(mnist_dataset,
                                          batch_size=4,
                                          shuffle=True)


if __name__ == "__main__":
    main()
