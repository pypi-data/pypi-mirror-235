
import jax
from jax import nn
from functools import wraps
from dataclasses import dataclass


MixedPrecisionContext

def __getattr__(name):
    nn_attr = getattr(nn, name)

    if not callable(nn_attr):
        return nn_attr

    @wraps(nn_attr)
    def wrapped_fn
        
    def wrap(*args, **kwargs):
