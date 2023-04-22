""" Tests for the `hook_utils` module"""

from typing import Callable
import torch

from algebraic_value_editing import hook_utils


# Test for front and back modifiers in hook_fn_from_activations()


def test_hook_fn_from_slice():
    """Test that we can selectively modify a portion of the residual stream."""
    input_tensor: torch.Tensor = torch.zeros((1, 2, 4))
    activations: torch.Tensor = 2 * torch.ones((1, 2, 4))

    # Modify these parts of the residual stream
    residual_stream_slice: slice = slice(1, 3)  # from 1 to 3 (exclusive)

    hook_fn: Callable = hook_utils.hook_fn_from_activations(
        activations=activations, res_stream_slice=residual_stream_slice
    )

    target_tens: torch.Tensor = torch.tensor([[[0, 2, 2, 0], [0, 2, 2, 0]]])
    result_tens: torch.Tensor = hook_fn(input_tensor)

    assert torch.eq(result_tens, target_tens).all(), "Slice test failed"


def test_hook_fn_from_activations():
    """Testing the front and back modifiers of the xvec_position"""
    pass  # TODO don't pass when merging back into dev (the function is not yet implemented on this branch)
    # input_tensor: torch.Tensor = torch.ones((1, 10, 1))
    # activations: torch.Tensor = 2 * torch.ones((1, 4, 1))

    # back_target: torch.Tensor = torch.tensor([[1, 1, 1, 1, 1, 1, 3, 3, 3, 3]])
    # back_target: torch.Tensor = back_target.unsqueeze(0).unsqueeze(-1)

    # hook_fxn: Callable = hook_utils.hook_fn_from_activations(activations=activations, "back")
    # result: torch.Tensor = hook_fxn(input_tensor)

    # assert torch.eq(result, back_target).all(), "xvec = back test failed"

    # # this needs to be repeated because it did replacements inpase
    # # TODO we should look into why this is?
    # input_tensor: torch.Tensor = torch.ones((1, 10, 1))
    # activations: torch.Tensor = 2 * torch.ones((1, 4, 1))

    # front_target: torch.Tensor = torch.tensor([[3, 3, 3, 3, 1, 1, 1, 1, 1, 1]])
    # front_target: torch.Tensor = front_target.unsqueeze(0).unsqueeze(-1)

    # hook_fxn: Callable = hook_utils.hook_fn_from_activations(activations=activations, "front")
    # result: torch.Tensor = hook_fxn(input_tensor)

    # assert torch.eq(result, front_target).all(), "xvec = front test failed"
