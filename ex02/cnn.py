import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision.datasets import FashionMNIST

from ex00.load_images import load_datasets


class ConvNet(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.net = nn.Sequential(
            nn.Conv2d(1, 8, 3),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(8, 16, 3),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Flatten(),
            nn.Linear(400, 10),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.net(x)


def get_dataloader(
    train_dataset: FashionMNIST, test_dataset: FashionMNIST, batch_size: int
) -> tuple[DataLoader, DataLoader]:
    train_loader = torch.utils.data.DataLoader(
        train_dataset, batch_size=batch_size, shuffle=True
    )

    test_loader = torch.utils.data.DataLoader(
        test_dataset, batch_size=batch_size, shuffle=False
    )
    return train_loader, test_loader


def train_model(
    train_loader, test_loader, learning_rate, device=torch.device("cpu")
):
    num_epochs = 10
    model = ConvNet().to(device)
    model.train()

    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=learning_rate)

    n_total_steps = len(train_loader)
    for epoch in range(num_epochs):
        for i, (images, labels) in enumerate(train_loader):
            images = images.to(device)
            labels = labels.to(device)

            # Forward pass
            outputs = model(images)
            loss = criterion(outputs, labels)

            # Backward and optimize
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            if (i + 1) % 450 == 0:
                print(
                    f"Epoch [{epoch + 1}/{num_epochs}], Step [{i + 1}/{n_total_steps}], Loss: {loss.item():.4f}"
                )

        accuracy = test_model(model, test_loader, device)
        print(
            f"Epoch [{epoch + 1}/{num_epochs}], Test accuracy: {accuracy:.4f}"
        )
        model.train()

    print("Finished Training")
    return model


def test_model(model, test_loader, device=torch.device("cpu")) -> float:
    """Return the accuracy of the model on the test set."""
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for images, labels in test_loader:
            images = images.to(device)
            labels = labels.to(device)

            outputs = model(images)
            predicted = outputs.argmax(dim=1)
            correct += (predicted == labels).sum().item()
            total += labels.size(0)

    return correct / total


def main() -> None:
    """Train a CNN on FashionMNIST and print its test accuracy."""
    torch.manual_seed(42)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    learning_rate = 0.1
    batch_size = 16
    train_dataset, test_dataset = load_datasets()
    train_loader, test_loader = get_dataloader(
        train_dataset, test_dataset, batch_size
    )
    classes = (
        "T-Shirt",
        "Trouser",
        "Pullover",
        "Dress",
        "Coat",
        "Sandal",
        "Shirt",
        "Sneaker",
        "Bag",
        "Ankle Boot",
    )
    # print(train_loader)
    model = train_model(train_loader, test_loader, learning_rate, device)
    accuracy = test_model(model, test_loader, device)
    print(f"Test accuracy: {accuracy:.4f}")


if __name__ == "__main__":
    main()
