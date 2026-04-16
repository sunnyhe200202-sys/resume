try:
    import PyPDF2
    reader = PyPDF2.PdfReader('何瑞阳 T-STAR 简历.pdf')
    text = ''.join(page.extract_text() for page in reader.pages)
    with open('extracted.txt', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Extracted with PyPDF2")
except Exception as e:
    print("PyPDF2 failed:", e)
    try:
        import fitz
        doc = fitz.open('何瑞阳 T-STAR 简历.pdf')
        text = ''.join(page.get_text() for page in doc)
        with open('extracted.txt', 'w', encoding='utf-8') as f:
            f.write(text)
        print("Extracted with PyMuPDF")
    except Exception as e2:
        print("PyMuPDF failed:", e2)
