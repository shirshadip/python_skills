import torch

# Check version
print("PyTorch version:", torch.__version__)

# Create a tensor
x = torch.tensor([2, 4, 6])
print("Tensor x:", x)

# Perform a simple operation
y = x * 3
print("Tensor y:", y)

# Check if CUDA (GPU) is available
print("CUDA available:", torch.cuda.is_available())
