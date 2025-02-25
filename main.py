from modules.parser import extract_text_from_epub
from modules.translator import translate_text

def main():
    # Ruta al archivo EPUB de prueba
    file_path = 'tests/test_files/sample.epub'
    
    # Extraer texto del archivo EPUB
    try:
        text = extract_text_from_epub(file_path)
        print("Texto extraído del EPUB:")
        print(text)
    except Exception as e:
        print(f"Error al extraer texto del EPUB: {e}")
        return

    # Traducir el texto extraído
    target_language = 'es'
    try:
        translated_text = translate_text(text, target_language)
        print("\nTexto traducido:")
        print(translated_text)
    except Exception as e:
        print(f"Error al traducir el texto: {e}")

if __name__ == "__main__":
    main()