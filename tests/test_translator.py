import unittest
from unittest.mock import patch
from modules.translator import translate_text

class TestTranslator(unittest.TestCase):

    @patch('modules.translator.requests.post')
    def test_translate_text_success(self, mock_post):
        # Configurar el mock para simular una respuesta exitosa de la API
        mock_response = mock_post.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {'translatedText': 'Hola Mundo'}

        # Llamar a la función con el mock
        result = translate_text('Hello World', 'es')
        self.assertEqual(result, 'Hola Mundo')

    @patch('modules.translator.requests.post')
    def test_translate_text_failure(self, mock_post):
        # Configurar el mock para simular una respuesta fallida de la API
        mock_response = mock_post.return_value
        mock_response.status_code = 400

        # Verificar que se lanza una excepción en caso de error
        with self.assertRaises(Exception):
            translate_text('Hello World', 'es')

if __name__ == '__main__':
    unittest.main()