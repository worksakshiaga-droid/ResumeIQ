
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_similarity(resume_text, job_description):

    # Check for empty input
    if not resume_text.strip() or not job_description.strip():
        return 0.0

    # Convert text into TF-IDF vectors
    vectorizer = TfidfVectorizer(
        stop_words="english",
        ngram_range=(1, 2)
    )

    try:
        tfidf_matrix = vectorizer.fit_transform([
            resume_text,
            job_description
        ])

        # Calculate cosine similarity
        similarity = cosine_similarity(
            tfidf_matrix[0:1],
            tfidf_matrix[1:2]
        )[0][0]

        # Convert into percentage
        return round(float(similarity) * 100, 2)

    except ValueError:
        return 0.0
