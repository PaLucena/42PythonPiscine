import matplotlib.pyplot as plt
import numpy as np
from load_image import ft_load


def ft_zoom(pixels: np.ndarray, x0: int, x1: int, y0: int, y1: int):
    zoomed_image = pixels[y0:y1, x0:x1]
    grey_image = np.mean(zoomed_image, axis=2).astype(np.uint8)
    grey_image = np.expand_dims(grey_image, axis=-1)
    print(grey_image.shape) 
    print(grey_image) 
    plt.imshow(grey_image, cmap="gray")
    plt.xticks(np.arange(0, grey_image.shape[1], 50))
    plt.yticks(np.arange(0, grey_image.shape[0], 50))
    plt.show()
    plt.close()


def main():
    try:
        pixels = ft_load("./animal.jpeg")
        print(pixels)

        y_start = (pixels.shape[0] - 400) // 2
        y_end = y_start + 400
        x_start = (pixels.shape[1] - 400) // 2
        x_end = x_start + 400
        ft_zoom(pixels, x_start, x_end, y_start, y_end)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
