
import pymupdf


def extract_resume_text(pdf_bytes):

    try:
        # Open uploaded PDF from memory
        document = pymupdf.open(
            stream=pdf_bytes,
            filetype="pdf"
        )

        extracted_text = ""

        # Extract text from every page
        for page in document:
            extracted_text += page.get_text("text") + "\n"

        document.close()

        # Check whether text was extracted
        if not extracted_text.strip():
            return None

        return extracted_text.strip()

    except Exception as e:
        print("PDF extraction error:", e)
        return None
