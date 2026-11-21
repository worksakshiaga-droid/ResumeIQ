
import re


def analyze_ats(resume_text):

    text = resume_text.strip()

    # ----------------------------------
    # 1. BASIC TEXT ANALYSIS
    # ----------------------------------

    words = text.split()
    word_count = len(words)

    lines = [
        line.strip()
        for line in text.splitlines()
        if line.strip()
    ]

    # ----------------------------------
    # 2. CONTACT INFORMATION
    # ----------------------------------

    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'

    phone_pattern = (
        r'(?<!\d)(?:\+?\d{1,3}[-.\s]?)?'
        r'(?:\d[-.\s]?){9,12}\d(?!\d)'
    )

    has_email = bool(re.search(email_pattern, text))
    has_phone = bool(re.search(phone_pattern, text))

    has_linkedin = "linkedin.com" in text.lower()
    has_github = "github.com" in text.lower()

    # ----------------------------------
    # 3. SECTION DETECTION
    # ----------------------------------

    section_patterns = {
        "Education": [
            "education",
            "academic background",
            "educational qualification"
        ],
        "Skills": [
            "skills",
            "technical skills",
            "core competencies"
        ],
        "Projects": [
            "projects",
            "academic projects",
            "personal projects"
        ],
        "Experience": [
            "experience",
            "work experience",
            "professional experience",
            "internship",
            "internships"
        ],
        "Certifications": [
            "certifications",
            "certificates",
            "courses"
        ],
        "Achievements": [
            "achievements",
            "accomplishments",
            "awards"
        ]
    }

    normalized_lines = [
        re.sub(r'[^a-z0-9 ]', '', line.lower()).strip()
        for line in lines
    ]

    detected_sections = []

    for section, patterns in section_patterns.items():

        found = any(
            any(
                line == pattern or
                line.startswith(pattern + " ")
                for pattern in patterns
            )
            for line in normalized_lines
        )

        if found:
            detected_sections.append(section)

    # ----------------------------------
    # 4. BULLET POINT ANALYSIS
    # ----------------------------------

    bullet_count = sum(
        1 for line in lines
        if re.match(r'^[•●▪◦\-*]\s+', line)
    )

    # ----------------------------------
    # 5. SCORING
    # ----------------------------------

    score = 0
    checks = []

    # Contact information: 20 points

    if has_email:
        score += 10
        checks.append(("Email address detected", True))
    else:
        checks.append(("Email address missing", False))

    if has_phone:
        score += 10
        checks.append(("Phone number detected", True))
    else:
        checks.append(("Phone number missing", False))

    # Resume sections: 40 points

    important_sections = [
        "Education",
        "Skills",
        "Projects",
        "Experience"
    ]

    for section in important_sections:

        if section in detected_sections:
            score += 10
            checks.append((f"{section} section detected", True))
        else:
            checks.append((f"{section} section not detected", False))

    # Resume content: 20 points

    if word_count >= 150:
        score += 10
        checks.append(("Resume contains sufficient text", True))
    else:
        checks.append(("Resume text appears too short", False))

    if bullet_count >= 2:
        score += 10
        checks.append(("Bullet points detected", True))
    else:
        checks.append(("Few or no bullet points detected", False))

    # Professional links: 10 points

    if has_linkedin:
        score += 5
        checks.append(("LinkedIn profile detected", True))
    else:
        checks.append(("LinkedIn profile not detected", False))

    if has_github:
        score += 5
        checks.append(("GitHub profile detected", True))
    else:
        checks.append(("GitHub profile not detected", False))

    # Text extraction: 10 points

    if word_count >= 50:
        score += 10
        checks.append(("Readable text extracted from PDF", True))
    else:
        checks.append(("Insufficient readable text extracted", False))

    # ----------------------------------
    # 6. IMPROVEMENT SUGGESTIONS
    # ----------------------------------

    suggestions = []

    if not has_email:
        suggestions.append(
            "Add a professional email address."
        )

    if not has_phone:
        suggestions.append(
            "Add a valid contact phone number."
        )

    for section in important_sections:

        if section not in detected_sections:
            suggestions.append(
                f"Add a clearly labelled {section} section if relevant."
            )

    if not has_linkedin:
        suggestions.append(
            "Consider adding your LinkedIn profile."
        )

    if not has_github:
        suggestions.append(
            "Consider adding your GitHub profile, especially for technical roles."
        )

    if word_count < 150:
        suggestions.append(
            "Your resume contains limited text. Add relevant details about your education, projects and skills."
        )

    if bullet_count < 2:
        suggestions.append(
            "Use clear bullet points to describe projects, responsibilities and achievements."
        )

    # ----------------------------------
    # 7. RESULT
    # ----------------------------------

    if score >= 80:
        status = "Strong"
    elif score >= 60:
        status = "Moderate"
    else:
        status = "Needs Improvement"

    return {
        "score": score,
        "status": status,
        "word_count": word_count,
        "bullet_count": bullet_count,
        "detected_sections": detected_sections,
        "has_email": has_email,
        "has_phone": has_phone,
        "has_linkedin": has_linkedin,
        "has_github": has_github,
        "checks": checks,
        "suggestions": suggestions
    }
