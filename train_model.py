import torch
import torch.nn as nn
import pandas as pd

# Load data
data = pd.read_csv("data/human_data.csv", header=None)

X = torch.tensor(data.iloc[:, :4].values, dtype=torch.float32)
y = torch.tensor(data.iloc[:, 4].values, dtype=torch.long)

# Simple neural network
model = nn.Sequential(
    nn.Linear(4, 32),
    nn.ReLU(),
    nn.Linear(32, 4)
)

loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# Training loop
for epoch in range(50):
    optimizer.zero_grad()
    outputs = model(X)
    loss = loss_fn(outputs, y)
    loss.backward()
    optimizer.step()

    if epoch % 10 == 0:
        print(f"Epoch {epoch} | Loss: {loss.item():.4f}")

# Save model
torch.save(model.state_dict(), "model/imitation_model.pth")
print("Model saved successfully.")
