from ebooklib import epub

def create_sample_epub(file_path):
    book = epub.EpubBook()

    # Set metadata
    book.set_identifier('id123456')
    book.set_title('Sample Book')
    book.set_language('en')
    book.add_author('Author Name')

    # Create chapter
    c1 = epub.EpubHtml(title='Introduction', file_name='chap_01.xhtml', lang='en')
    c1.content = u'<h1>Introduction</h1><p>This is a sample book for testing purposes.</p>'

    # Add chapter
    book.add_item(c1)

    # Define Table Of Contents
    book.toc = (epub.Link('chap_01.xhtml', 'Introduction', 'intro'),)

    # Add default NCX and Nav file
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    # Create spine
    book.spine = ['nav', c1]

    # Write to the file
    epub.write_epub(file_path, book, {})

if __name__ == "__main__":
    create_sample_epub('tests/test_files/sample.epub')