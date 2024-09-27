from PIL import Image, ImageFilter, ImageOps
import os

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
        img = Image.open(file_path).convert('RGB')
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

def allowed_file(filename : str) -> bool:
    """
    Check if a given filename has an allowed extension.

    This function verifies if the file extension of the provided filename
    is one of the allowed types (png, jpg, jpeg, gif). The check is case-insensitive.

    Args:
        filename (str): The name of the file to check.

    Returns:
        bool: True if the file extension is allowed, False otherwise.
    """
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def remove_directories(folder_path: str) -> None:
    """
    Recursively deletes all files and subdirectories within a given root directory,
    then removes the root directory itself.

    Args:
        folder_path (str): The path to the directory that needs to be deleted.

    Returns:
        None

    Raises:
        FileNotFoundError: If the directory or file does not exist.
        PermissionError: If there are insufficient permissions to delete files or directories.
        OSError: If any error occurs while removing files or directories.
    """
    try:
        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)
            if os.path.isfile(item_path):
                try:
                    os.remove(item_path)
                except PermissionError as e:
                    print(f"Unable to delete file {item_path}: {e}")
                except OSError as e:
                    print(f"Error while deleting file {item_path}: {e}")
            else:
                remove_directories(item_path)
        os.removedirs(folder_path)
    except FileNotFoundError as e:
        print(f"Directory or file not found: {e}")
    except PermissionError as e:
        print(f"Insufficient permissions to delete the directory: {e}")
    except OSError as e:
        print(f"System error while deleting directory {folder_path}: {e}")