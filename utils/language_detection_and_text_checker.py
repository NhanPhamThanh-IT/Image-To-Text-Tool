from langdetect import detect
from spellchecker import SpellChecker
import re

def clean_text(text: str) -> str:
    """
    Cleans the input text by removing special characters and punctuation marks.

    This function uses a regular expression to remove the following characters from the text:
    `.,/;|\\{}`~!@#$%^&*():?><"`

    Args:
        text (str): The input string that needs to be cleaned.

    Returns:
        str: The cleaned string with special characters removed.
    """
    return re.sub(r'[.,/;|\\{}`~!@#$%^&*():?><"]', '', text.lower())


def detect_language(text: str) -> str:
    """
    Detects the language of the input text.

    This function uses the langdetect library to analyze the input text and return
    the detected language code (e.g., 'en' for English, 'fr' for French).

    Args:
        text (str): The input text whose language needs to be detected.

    Returns:
        str: A language code representing the detected language of the text.
    """
    language = detect(text)
    return language


def get_misspelled_words(text: str, language: str = 'en') -> list:
    """
    Identifies misspelled words in the input text based on the specified language.

    This function cleans the input text by removing special characters, splits the text into
    individual words, and then checks for misspelled words using a spell checker for the given language.

    Args:
        text (str): The input text to be checked for spelling errors.
        language (str, optional): The language of the text. Defaults to 'en' (English).

    Returns:
        list: A list of misspelled words found in the text. If no misspelled words are found, the list will be empty.
    """
    text = clean_text(text)
    spell = SpellChecker(language=language)
    words = text.split()
    misspelled = spell.unknown(words)
    return list(misspelled)


def remove_misspelled(text: str) -> str:
    """
    Removes misspelled words from the input text.

    This function first identifies the misspelled words in the input text and then constructs
    a new string that contains only the correctly spelled words.

    Args:
        text (str): The input text from which misspelled words should be removed.

    Returns:
        str: The text with all misspelled words removed, preserving the original spacing of correctly spelled words.
    """
    misspelled = get_misspelled_words(text)
    return ' '.join(word for word in text.split() if clean_text(word) not in misspelled)