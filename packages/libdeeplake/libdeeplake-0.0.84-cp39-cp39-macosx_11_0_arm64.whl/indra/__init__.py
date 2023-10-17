__all__ = [
    "__version__",
]

try:
    import torch
    torch.set_num_threads(1)
except ImportError:
    pass

__version__ = "0.0.84"
