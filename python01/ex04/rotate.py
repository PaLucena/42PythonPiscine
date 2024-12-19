import matplotlib.pyplot as plt
import numpy as np
from load_image import ft_load


def ft_zoom(pixels: np.ndarray, x0: int, x1: int, y0: int,
            y1: int) -> np.ndarray:
    """
    Zooms into a region of the image based on
    slicing indices and displays it with scaling axis.
    Turns image grey.
    """
    zoomed_image = pixels[y0:y1, x0:x1]
    grey_image = np.mean(zoomed_image, axis=2).astype(np.uint8)
    grey_image = np.expand_dims(grey_image, axis=-1)
    print("The shape of image is:", grey_image.shape,
          "or", np.squeeze(grey_image, axis=-1).shape)
    return (grey_image)


def ft_rotate(image: np.ndarray):
    """
    Rotates an image 90 degrees counterclockwise
    and mirrors it horizontally.
    """
    rows, cols, channel = image.shape
    rotated_image = np.zeros((rows, cols, channel), dtype=image.dtype)
    
    for row in range(rows):
        for col in range(cols):
            rotated_image[col, row] = image[row, col]

    rotated_image = np.squeeze(rotated_image, axis=-1)
    print("New shape after Transpose:", rotated_image.shape)
    print(rotated_image)
    plt.imshow(rotated_image, cmap="gray")
    plt.show()
    plt.close()


def main():
    try:
        pixels = ft_load("./animal.jpeg")

        y_start = (pixels.shape[0] - 400) // 2
        y_end = y_start + 400
        x_start = (pixels.shape[1] - 400) // 2
        x_end = x_start + 400
        image = ft_zoom(pixels, x_start, x_end, y_start, y_end)
        print(image)
        ft_rotate(image)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
