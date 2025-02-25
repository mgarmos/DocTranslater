from ebooklib import epub, ITEM_DOCUMENT
from bs4 import BeautifulSoup

def extract_text_from_epub(file_path):
    """
    Extrae el texto de un archivo EPUB.

    :param file_path: Ruta al archivo EPUB.
    :return: Texto extraído.
    """
    try:
        book = epub.read_epub(file_path)
    except Exception as e:
        raise ValueError(f"Error al leer el archivo EPUB: {e}")

    text = []

    for item in book.get_items():
        if item.get_type() == ITEM_DOCUMENT:
            soup = BeautifulSoup(item.get_content(), 'html.parser')
            text.append(soup.get_text())

    return '\n'.join(text)