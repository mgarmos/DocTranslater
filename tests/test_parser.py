import unittest
from modules.parser import extract_text_from_epub

class TestParser(unittest.TestCase):

    def test_extract_text_from_epub(self):
        # Ruta a un archivo EPUB de prueba
        file_path = 'tests/test_files/sample.epub'
        
        # Llamar a la función para extraer texto
        text = extract_text_from_epub(file_path)
        
        # Imprimir el texto extraído
        print("Texto extraído del EPUB:")
        print(text)

        # Verificar que el texto extraído no esté vacío
        self.assertTrue(len(text) > 0)

if __name__ == '__main__':
    unittest.main()