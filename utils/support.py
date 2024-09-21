from PIL import Image

def load_image(file_path : str) -> Image.Image:
    """
    Load an image from the specified file path.

    Args:
        file_path (str): The path to the image file to be loaded.

    Returns:
        Image.Image: An instance of PIL.Image representing the loaded image.

    Raises:
        FileNotFoundError: If the specified file path does not exist.
        IOError: If the image file cannot be opened.
    """
    img = Image.open(file_path)
    return img

