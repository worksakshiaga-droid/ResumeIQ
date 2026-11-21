
import re


def enhance_bullet_points(text):

    bullets = [
        line.strip().lstrip("•●▪◦-* ").strip()
        for line in text.splitlines()
        if line.strip()
    ]

    replacements = {
        "worked on": "Contributed to",
        "helped with": "Supported",
        "helped": "Assisted in",
        "responsible for": "Managed",
        "made": "Created",
        "used": "Applied",
        "did": "Completed",
        "was involved in": "Contributed to",
        "took part in": "Participated in",
        "learned": "Developed knowledge of",
        "worked with": "Collaborated with"
    }

    results = []

    for bullet in bullets:

        original = bullet

        # Remove first-person wording
        bullet = re.sub(
            r"^(I|My)\s+",
            "",
            bullet,
            flags=re.IGNORECASE
        )

        # Remove unnecessary spaces
        bullet = re.sub(r"\s+", " ", bullet).strip()

        enhanced = bullet
        changed = False

        # Improve weak starting phrases
        for phrase, replacement in replacements.items():

            pattern = r"^" + re.escape(phrase) + r"\b"

            if re.match(pattern, enhanced, flags=re.IGNORECASE):

                enhanced = re.sub(
                    pattern,
                    replacement,
                    enhanced,
                    count=1,
                    flags=re.IGNORECASE
                )

                changed = True
                break

        # Capitalize first character
        if enhanced:
            enhanced = enhanced[0].upper() + enhanced[1:]

        # Ensure sentence punctuation
        if enhanced and enhanced[-1] not in ".!?":
            enhanced += "."

        # Improvement notes
        notes = []

        if len(original.split()) < 6:
            notes.append(
                "Add more detail about what you actually did."
            )

        if not re.search(r"\d+%|\d+|\b\d+\s*(users|clients|projects|hours)\b",
                         original, re.IGNORECASE):
            notes.append(
                "Consider adding a measurable result if you have verified data."
            )

        if not changed:
            notes.append(
                "Consider using a more specific action verb where appropriate."
            )

        results.append({
            "original": original,
            "enhanced": enhanced,
            "changed": changed,
            "notes": notes
        })

    return results
