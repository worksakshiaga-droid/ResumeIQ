
import re

# Technical skills and their alternative names
SKILL_DICTIONARY = {
    "Python": ["python"],
    "Java": ["java"],
    "C++": ["c++"],
    "SQL": ["sql", "structured query language"],
    "Machine Learning": [
        "machine learning",
        "ml"
    ],
    "Deep Learning": ["deep learning", "dl"],
    "NLP": [
        "nlp",
        "natural language processing"
    ],
    "Pandas": ["pandas"],
    "NumPy": ["numpy"],
    "TensorFlow": ["tensorflow"],
    "Scikit-learn": [
        "scikit-learn",
        "sklearn"
    ],
    "PyTorch": ["pytorch"],
    "OpenCV": ["opencv"],
    "Data Analysis": ["data analysis"],
    "Data Visualization": [
        "data visualization"
    ],
    "HTML": ["html"],
    "CSS": ["css"],
    "JavaScript": ["javascript"],
    "Git": ["git"],
    "Excel": ["excel"]
}


def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill, aliases in SKILL_DICTIONARY.items():

        for alias in aliases:

            pattern = (
                r"(?<![a-z0-9])"
                + re.escape(alias)
                + r"(?![a-z0-9])"
            )

            if re.search(pattern, text):

                found_skills.append(skill)
                break

    return found_skills
