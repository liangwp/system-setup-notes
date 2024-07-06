import torch
import torchvision

print(f'cuda available: {torch.cuda.is_available()}')
print(f'torch version: {torch.__version__}')
print(f'torchvision version: {torchvision.__version__}')
print(f'cuda version: {torch.version.cuda}')
try:
    print(f'cudnn version: {torch.backends.cudnn.version()}')
except Exception as e:
    print('cudnn not available')
    print(e)

x = torch.rand(5, 3)
print(x)
