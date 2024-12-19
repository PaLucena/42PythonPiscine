from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """
    Load an image from drive, prints it's format and RGB content,
    and manages errors.

    Params:
    path (str): Route to the image to change.

    Returns:
    np.ndarray: Numpy matrix as the image's RGB content.
    """
    try:
        with Image.open(path) as img:
            img_format = img.format
            if img_format not in ['JPEG', 'JPG']:
                raise ValueError(f"Format not supported: {img_format}.\
                                  Only JPG and JPEG.")
            img_rgb = img.convert("RGB")
            pixels = np.array(img_rgb)

            return pixels
    except FileNotFoundError:
        raise FileNotFoundError(f"Image not found in route: {path}")
    except Exception as e:
        raise RuntimeError(f"Error loading image: {e}")


def main():
    try:
        pixels = ft_load("./animal.jpeg")
        print(pixels)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
