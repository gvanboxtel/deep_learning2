import torch
from torchvision import tv_tensors
from torch import nn
from ex00.load_images import load_datasets

def apply_convolution(image: tv_tensors._image.Image) -> torch.Tensor:
    """Apply a 3x3 convolution with 4 output channels and print the shape.

    Args:
        image: Batch of grayscale images, shape (N, 1, H, W).

    Returns:
        The feature maps, shape (N, 4, H - 2, W - 2).
    """
    convolution: nn.Conv2d = nn.Conv2d(1, 4, 3)
    conv_image = convolution(image)
    print(f"After conv: {conv_image.shape}")
    return conv_image


def apply_pool(conv_image: torch.Tensor) -> None:
    """Apply 2x2 max pooling to the feature maps and print the shape."""
    pool = nn.MaxPool2d(2)
    print(f"After pool: {pool(conv_image).shape}")


def main() -> None:
    """Print the shape of an image through a convolution and a pooling."""
    torch.manual_seed(42)
    train, test = load_datasets()
    image: tv_tensors._image.Image = train[0][0].unsqueeze(0)
    print(f"input shape: {image.shape}")
    conv_image = apply_convolution(image)
    apply_pool(conv_image)





if __name__ == "__main__":
    main()
