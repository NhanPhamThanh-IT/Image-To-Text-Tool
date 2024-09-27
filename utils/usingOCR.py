import torch
import easyocr
from utils.support import load_image
from utils.language_detection_and_text_checker import remove_misspelled

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
        Extracts text from an image using Tesseract OCR with Vietnamese language detection. If Tesseract fails to extract 
        any text, EasyOCR is used as a fallback method. After extraction, the text is processed to remove misspelled words.

        Args:
            pytesseract: The Tesseract OCR module used for text extraction from the image.

        Returns:
            str: The cleaned and extracted text from the image using either Tesseract or EasyOCR.

        Raises:
            Exception: If both Tesseract and EasyOCR fail to extract text from the image.
        """
        text = pytesseract.image_to_string(self.img, lang='vie')
        if not text:
            reader = easyocr.Reader(['vi'], gpu=torch.cuda.is_available())
            results = reader.readtext(self.path)
            text = ' '.join([result[1] for result in results])
        text = remove_misspelled(text)
        return text