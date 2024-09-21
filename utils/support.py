from PIL import Image

def load_image(file_path: str) -> Image.Image:
    """
    Load an image from the specified file path.

    Args:
        file_path (str): The path to the image file to be loaded.

    Returns:
        Image.Image: An instance of PIL.Image representing the loaded image.

    Raises:
        FileNotFoundError: If the specified file path does not exist.
        IOError: If the image file cannot be opened or read.
        ValueError: If the file path is empty.
    """
    if not file_path:
        raise ValueError("File path cannot be empty.")
    try:
        img = Image.open(file_path)
        img.verify()
        return img
    except FileNotFoundError:
        raise FileNotFoundError(f"The file at '{file_path}' was not found !")
    except IOError as e:
        raise IOError(f"An error occurred while opening the image file: {e} !")

def save_file(file_path: str, text: str) -> None:
    """
    Save the given text to a file at the specified file path.

    Args:
        file_path (str): The path to the file where the text will be saved.
        text (str): The text to write to the file.

    Raises:
        IOError: If an I/O error occurs while writing to the file.
        ValueError: If the file path is empty.
    """
    if not file_path:
        raise ValueError("File path cannot be empty !")
    try:
        with open(file_path, 'w') as file:
            file.write(text)
    except IOError as e:
        raise IOError(f"An error occurred while writing to the file: {e} !")
