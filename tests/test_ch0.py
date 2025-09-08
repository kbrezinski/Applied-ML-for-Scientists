
import pytest
import numpy as np
import pandas as pd
import torch


def test_environment_setup():
    """Test that core dependencies are properly installed and working."""
    # Test numpy
    assert np.__version__ >= "1.26"
    arr = np.array([1, 2, 3])
    assert arr.sum() == 6

    # Test pandas
    assert pd.__version__ >= "2.2"
    df = pd.DataFrame({"a": [1, 2, 3]})
    assert len(df) == 3

    # Test PyTorch
    assert torch.__version__ >= "2.3"
    tensor = torch.tensor([1., 2., 3.])
    assert tensor.sum().item() == 6.


def test_simple_math():
    """A simple test to verify pytest is working."""
    assert 1 + 1 == 2
    assert 2 * 2 == 4