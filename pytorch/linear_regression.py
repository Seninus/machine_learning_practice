import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from torch.utils.data import DataLoader, TensorDataset


# step 1, Define the model & train device
class LinearRegression(nn.Module):
    def __init__(self, input_dim, output_dim):
        super(LinearRegression, self).__init__()
        self.linear = nn.Linear(input_dim, output_dim)

    def forward(self, x):
        return self.linear(x)


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# step 2, setup dataset
x_train = x_train = torch.tensor([i for i in range(1, 21)], dtype=torch.float32, requires_grad=True).reshape(-1, 1)
y_train = x_train + torch.randn(20, 1)
train_ds = TensorDataset(x_train, y_train)

batch_size = 5
data_loader = DataLoader(train_ds, batch_size=batch_size, shuffle=True)

# step 3, define criterion
criterion = F.mse_loss

# step 4, create model and train
model = LinearRegression(1, 1)

# step 5, define optimizer
learning_rate = 0.001
optimizer = optim.SGD(model.parameters(), lr=learning_rate)

# step 6, train the model
epochs = 100
for epoch in range(epochs):
    for (bx, by) in data_loader:
        bx = bx.to(device=device)
        by = by.to(device=device)

        pred = model.forward(bx)
        loss = criterion(pred, by)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        print("Epoch  {}, loss {}".format(epoch + 1, loss.item()))

preds = model(x_train)
print(preds)
