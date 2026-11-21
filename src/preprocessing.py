
import re


def clean_text(text):

    # Convert text into lowercase
    text = text.lower()

    # Remove unnecessary special characters
    text = re.sub(r"[^\w\s+#./-]", " ", text)

    # Remove extra spaces and newlines
    text = re.sub(r"\s+", " ", text)

    return text.strip()
