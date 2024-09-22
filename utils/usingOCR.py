from PIL import Image
import torch
import easyocr
from utils.support import load_image

class OCR:
    """
    A class to perform Optical Character Recognition (OCR) on images using either Tesseract or EasyOCR.

    Attributes:
        path (str): The file path to the image to be processed.
        img (Image.Image): The loaded image to be processed for text extraction.
    """

    def __init__(self, path: str) -> None:
        """
        Initializes the OCR class with the path to an image.

        Args:
            path (str): The file path to the image to be processed for OCR.
        """
        self.path = path
        self.img = load_image(path)
    
    def get_text(self, pytesseract) -> str:
        """
        Extracts text from the image using Tesseract OCR. If Tesseract fails to extract text, 
        EasyOCR is used as a fallback method.

        Args:
            pytesseract: The Tesseract OCR module used for text extraction.

        Returns:
            str: The extracted text from the image using Tesseract or EasyOCR.

        Raises:
            Exception: If an error occurs during text extraction or if neither engine can extract text.
        """
        text = pytesseract.image_to_string(self.img, lang='vie')

        if not text:
            reader = easyocr.Reader(['vi', 'en'], gpu=torch.cuda.is_available())
            results = reader.readtext(self.path)
            text = ' '.join([result[1] for result in results])
        
        return text