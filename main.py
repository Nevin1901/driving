import numpy as np
import torch


if __name__ == "__main__":
    device = "cuda" if torch.cuda.is_available() else "cpu"

    # first load training data