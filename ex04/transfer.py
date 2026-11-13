import torch


def main() -> None:
    """Train a new head on a frozen pretrained resnet18."""
    torch.manual_seed(42)


if __name__ == "__main__":
    main()
