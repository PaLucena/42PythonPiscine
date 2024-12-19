import numpy as np
from numpy import ndarray as array
from load_image import display_image


def ft_invert(array) -> array:
    """Inverts the color of the image received."""
    inverted = 255 - array
    display_image(inverted)
    return inverted


def ft_red(array) -> array:
    """
    RED filter
    """
    red = array.copy()
    red[:, :, 1] = 0
    red[:, :, 2] = 0
    display_image(red)
    return red


def ft_green(array) -> array:
    """
    GREEN filter
    """
    green = array.copy()
    green[:, :, 0] = 0
    green[:, :, 2] = 0
    display_image(green)
    return green

def ft_blue(array) -> array:
    """
    BLUE filter
    """
    blue = array.copy()
    blue[:, :, 0] = 0
    blue[:, :, 1] = 0
    display_image(blue)
    return blue


def ft_grey(array) -> array:
    """
    GREY filter
    """
    grey = np.mean(array, axis=2).astype(np.uint8)
    grey = np.expand_dims(grey, axis=-1)
    display_image(grey, "grey")
    return grey
