import requests

def translate_text(text, target_language):
    """
    Traduce el texto dado al idioma objetivo utilizando LibreTranslate.

    :param text: Texto a traducir.
    :param target_language: Código del idioma objetivo (por ejemplo, 'es' para español).
    :return: Texto traducido.
    """
    url = "https://libretranslate.com/translate"
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    params = {
        'q': text,
        'source': 'auto',
        'target': target_language,
        'format': 'text'
    }
    try:
        response = requests.post(url, data=params, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        raise ValueError(f"Error al traducir el texto: {e}")

    
    return response.json().get('translatedText')
