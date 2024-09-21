from PIL import Image
import pytesseract

class OCR:
    """
    A class to perform Optical Character Recognition (OCR) on images.

    Attributes:
        img (Image.Image): The image to be processed for text extraction.
    """

    def __init__(self, img : Image.Image) -> None:
        """
        Initializes the OCR class with an image.

        Args:
            img (Image.Image): The image to be processed for OCR.
        """
        self.img = img
    
    def get_text(self, pytesseract) -> str:
        """
        Extracts text from the image using the specified Tesseract OCR engine.

        Args:
            pytesseract: The Tesseract OCR module used for text extraction.

        Returns:
            str: The extracted text from the image.

        Raises:
            Exception: If an error occurs during text extraction.
        """
        return pytesseract.image_to_string(self.img, lang='vie')