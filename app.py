import html
import joblib
import streamlit as st
import pandas as pd
import os

from src.pdf_parser import extract_resume_text
from src.preprocessing import clean_text
from src.skill_extractor import extract_skills
from src.similarity import calculate_similarity
from src.ats_analyzer import analyze_ats
from src.bullet_enhancer import enhance_bullet_points
from src.learning_roadmap import (
    generate_learning_roadmap,
    generate_weekly_timeline
)
from src.learning_pdf import generate_learning_pdf
# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="ResumeIQ",
    page_icon="📄",
    layout="wide"
)


# ==========================================
# 2. LOAD MODEL
# ==========================================

model = joblib.load("models/resume_match_model.pkl")


# ==========================================
# 3. SIDEBAR
# ==========================================

with st.sidebar:

    st.markdown("### 📄 ResumeIQ")
    st.caption("AI Career Intelligence")

    st.divider()

    st.markdown("### 🚀 Dashboard")
    st.write("Analyze your resume and discover your job match.")

    st.divider()

    st.markdown("### ✨ Features")
    st.markdown("""
    - 📄 Resume Analysis
    - 🎯 Skill Gap Detection
    - 🤖 AI Match Prediction
    - 📊 Analytics Dashboard
    - 🌿 Resume Strength Score
    """)

    st.divider()

    st.caption("ResumeIQ | Version 1.0")
    st.caption("Built with Python & Machine Learning")


# ==========================================
# 4. FIXED COLOUR PALETTE
# ==========================================

background = "#F7F2EA"          # warm ivory
secondary = "#FFFDFC"           # soft white
text_color = "#293630"          # deep charcoal-green
heading_color = "#29483D"       # forest green
border_color = "#E5D5C6"        # warm beige border
sidebar_background = "#EFE6DA"  # warm sand
input_background = "#FFFEFC"
placeholder_color = "#7D756D"
accent = "#B9683F"              # burnt copper
accent_dark = "#98502F"
copper = "#C47A50"
copper_light = "#F4E2D4"
green_soft = "#E4ECE5"
green = "#315C49"


# ==========================================
# 5. APPLICATION CSS
# ==========================================

st.markdown(f"""
<style>

/* Overall application */
.stApp,
[data-testid="stAppViewContainer"],
[data-testid="stMain"] {{
    background-color: {background} !important;
    color: {text_color} !important;
}}

/* Main text */
.stApp [data-testid="stMarkdownContainer"],
.stApp [data-testid="stMarkdownContainer"] p,
.stApp [data-testid="stMarkdownContainer"] li,
.stApp .stText,
.stApp .stCaption,
.stApp [data-testid="stMetricLabel"],
.stApp [data-testid="stMetricValue"] {{
    color: {text_color} !important;
}}

/* Headings */
.stApp h1,
.stApp h2,
.stApp h3,
.stApp h4 {{
    color: {heading_color} !important;
    font-weight: 700 !important;
}}

/* Hero: forest green with a visible copper glow */
.hero {{
    background: linear-gradient(115deg, #233F35 0%, #315C49 58%, #A85F3C 100%);
    padding: 38px 40px;
    border-radius: 20px;
    border: 1px solid #C47A50;
    margin-bottom: 28px;
    box-shadow: 0 10px 28px rgba(72, 54, 39, 0.12);
}}
.hero h1 {{
    color: #FFFFFF !important;
    font-size: 44px;
    font-weight: 800;
    margin-bottom: 6px;
}}
.hero p {{
    color: #F8EDE4 !important;
    font-size: 17px;
}}
.hero-tag {{
    color: #F2BD96 !important;
    font-size: 12px;
    letter-spacing: 2.2px;
    font-weight: 800;
}}

/* Sidebar */
[data-testid="stSidebar"] {{
    background-color: {sidebar_background} !important;
    border-right: 1px solid {border_color};
}}
[data-testid="stSidebar"] .stMarkdown p,
[data-testid="stSidebar"] .stMarkdown li,
[data-testid="stSidebar"] .stCaptionContainer p,
[data-testid="stSidebar"] label {{
    color: {text_color} !important;
}}
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {{
    color: {heading_color} !important;
}}

/* Metric cards: warm copper tint, not green */
[data-testid="stMetric"] {{
    background: linear-gradient(145deg, #FFFDFC, #F8E9DD) !important;
    border: 1px solid #E4C5AE !important;
    border-radius: 16px;
    padding: 18px;
    box-shadow: 0 4px 14px rgba(86, 60, 40, 0.06);
}}
[data-testid="stMetricLabel"],
[data-testid="stMetricValue"],
[data-testid="stMetricDelta"] {{
    color: {text_color} !important;
}}

/* Text inputs */
.stTextArea textarea,
.stTextInput input {{
    background-color: {input_background} !important;
    color: {text_color} !important;
    -webkit-text-fill-color: {text_color} !important;
    border: 1px solid #DCC8B7 !important;
    border-radius: 12px !important;
    caret-color: {text_color} !important;
}}
.stTextArea textarea:focus,
.stTextInput input:focus {{
    border: 1px solid {copper} !important;
    box-shadow: 0 0 0 1px {copper} !important;
}}
.stTextArea textarea::placeholder,
.stTextInput input::placeholder {{
    color: {placeholder_color} !important;
    -webkit-text-fill-color: {placeholder_color} !important;
    opacity: 1 !important;
}}

/* File uploader: warm peach surface */
[data-testid="stFileUploader"] {{
    background-color: {copper_light} !important;
    border: 1px dashed {copper} !important;
    border-radius: 16px !important;
    padding: 15px !important;
}}
[data-testid="stFileUploaderDropzone"] {{
    background-color: #FFFAF5 !important;
    border: 1px dashed {copper} !important;
    border-radius: 12px !important;
}}
[data-testid="stFileUploaderDropzone"] * {{
    color: {text_color} !important;
}}
[data-testid="stFileUploaderDropzone"] button {{
    background-color: {accent} !important;
    color: #FFFFFF !important;
    border: none !important;
}}
[data-testid="stFileUploaderFile"] {{
    background-color: #FFFDFC !important;
    border: 1px solid {border_color} !important;
    border-radius: 10px !important;
}}
[data-testid="stFileUploaderFile"] * {{
    color: {text_color} !important;
    opacity: 1 !important;
}}

/* Expanders and Streamlit alerts */
[data-testid="stExpander"],
[data-testid="stAlert"] {{
    background-color: #FFFDFC !important;
    border: 1px solid {border_color} !important;
    border-radius: 12px !important;
}}
[data-testid="stExpander"] *,
[data-testid="stAlert"] * {{
    color: {text_color} !important;
    -webkit-text-fill-color: {text_color} !important;
}}
[data-testid="stExpanderDetails"] {{
    background-color: #FFFDFC !important;
}}

/* Buttons: copper primary */
.stButton > button,
.stDownloadButton > button {{
    background: linear-gradient(100deg, #B9683F, #CC8054) !important;
    color: #FFFFFF !important;
    -webkit-text-fill-color: #FFFFFF !important;
    border: 1px solid #A95D38 !important;
    border-radius: 11px !important;
    font-weight: 700 !important;
    padding: 0.55rem 1.15rem !important;
    box-shadow: 0 4px 10px rgba(169, 93, 56, 0.16);
}}
.stButton > button:hover,
.stDownloadButton > button:hover {{
    background: {accent_dark} !important;
    border-color: {accent_dark} !important;
    color: #FFFFFF !important;
    -webkit-text-fill-color: #FFFFFF !important;
}}

/* Radio labels, dividers and progress */
[data-testid="stRadio"] label,
[data-testid="stRadio"] p {{
    color: {text_color} !important;
}}
hr {{
    border-color: {border_color} !important;
}}
.stProgress > div > div > div {{
    background: linear-gradient(90deg, #315C49, #C47A50) !important;
}}

</style>
""", unsafe_allow_html=True)

def show_custom_alert(message):
    st.markdown(
        f"""
        <div style="
            background: linear-gradient(100deg, #FFF8F1, #F7E5D8);
            color: #293630;
            -webkit-text-fill-color: #293630;
            border: 1px solid #E4C5AE;
            border-left: 5px solid #B9683F;
            border-radius: 12px;
            padding: 14px 18px;
            margin: 8px 0;
            font-size: 16px;
            font-weight: 500;
        ">
            {html.escape(str(message))}
        </div>
        """,
        unsafe_allow_html=True
    )


# ==========================================
# 6. HERO SECTION
# ==========================================

st.markdown("""
<div class="hero">
    <div class="hero-tag">AI POWERED CAREER INTELLIGENCE</div>
    <h1>📄 ResumeIQ</h1>
    <p>Your intelligent resume analyzer and job matching assistant.</p>
</div>
""", unsafe_allow_html=True)


# ==========================================
# 7. RESUME UPLOAD
# ==========================================

st.header("1. Upload Your Resume")

uploaded_file = st.file_uploader(
    "Choose your resume (PDF)",
    type=["pdf"],
    key="resume_upload"
)

# Separate visible filename card

if uploaded_file is not None:

    st.markdown(
        f"""
        <div style="
            background: linear-gradient(100deg, #315C49, #A85F3C);
            color: white;
            padding: 14px 18px;
            border-radius: 12px;
            margin-top: 10px;
            margin-bottom: 15px;
            border: 1px solid #D49A75;
            font-weight: 600;
        ">
            📄 Uploaded File: {html.escape(uploaded_file.name)}
        </div>
        """,
        unsafe_allow_html=True
    )


# ==========================================
# 8. JOB DESCRIPTION
# ==========================================

st.header("2. Enter Job Description")

job_description = st.text_area(
    "Paste the job description here",
    height=200,
    placeholder="Enter job requirements and responsibilities..."
)


# ==========================================
# 9. RESUME ANALYSIS
# ==========================================


if uploaded_file is not None:

    resume_text = extract_resume_text(
        uploaded_file.getvalue()
    )

    if resume_text:

        st.success("Resume uploaded successfully!")

        # ==========================================
        # ATS COMPATIBILITY SIMULATOR
        # ==========================================

        st.divider()
        st.header("3. ATS Compatibility Simulator")

        ats_result = analyze_ats(resume_text)

        ats_col1, ats_col2 = st.columns(2)

        with ats_col1:
            st.metric(
                "ATS Compatibility Score",
                f"{ats_result['score']}/100"
            )

        with ats_col2:
            st.metric(
                "ATS Status",
                ats_result["status"]
            )

        st.progress(ats_result["score"])

        st.caption(
            "This is a rule-based compatibility estimate, "
            "not a guarantee of passing any company's ATS."
        )

        st.subheader("ATS Checklist")

        for check, passed in ats_result["checks"]:

            if passed:
                st.success(f"✓ {check}")
            else:
                st.warning(f"⚠ {check}")

        st.subheader("Detected Resume Sections")

        if ats_result["detected_sections"]:
            st.write(", ".join(ats_result["detected_sections"]))
        else:
            st.info("No standard resume sections detected.")

        st.subheader("ATS Improvement Suggestions")

        if ats_result["suggestions"]:

            for suggestion in ats_result["suggestions"]:
                st.write(f"• {suggestion}")

        else:
            st.success("All current ATS checks passed!")

        with st.expander("View ATS Text Analysis"):
            st.write(f"Word count: {ats_result['word_count']}")
            st.write(f"Bullet points: {ats_result['bullet_count']}")
            st.write("Visual PDF formatting: Not checked")

        # Continue existing resume analysis

        cleaned_resume = clean_text(resume_text)


        # ==========================================
        # SMART BULLET POINT ENHANCER
        # ==========================================

        st.divider()
        st.header("4. Smart Bullet Point Enhancer")

        st.write(
            "Improve your resume bullet points with clearer, "
            "more professional wording."
        )

        bullet_input = st.text_area(
            "Paste your resume bullet points (one per line)",
            height=160,
            placeholder=(
                "Worked on a Python project.\n"
                "Helped with data analysis.\n"
                "Used SQL to manage data."
            ),
            key="bullet_enhancer_input"
        )

        if st.button("✨ Enhance My Bullet Points"):

            if bullet_input.strip():

                enhanced_results = enhance_bullet_points(
                    bullet_input
                )

                st.subheader("Your Improved Bullet Points")

                for index, result in enumerate(enhanced_results, 1):

                    with st.container(border=True):

                        st.markdown(f"**Bullet Point {index}**")

                        st.caption("ORIGINAL")
                        st.write(result["original"])

                        st.caption("ENHANCED")
                        st.success(result["enhanced"])

                        if result["notes"]:

                            st.caption("SUGGESTIONS")

                            for note in result["notes"]:
                                st.write(f"• {note}")

                enhanced_text = "\n".join(
                    result["enhanced"]
                    for result in enhanced_results
                )

                st.download_button(
                    "Download Enhanced Bullet Points",
                    data=enhanced_text,
                    file_name="ResumeIQ_Enhanced_Bullets.txt",
                    mime="text/plain"
                )

            else:

                st.warning(
                    "Please enter at least one bullet point."
                )

        resume_skills = extract_skills(cleaned_resume)

        # SECTION 3

        st.subheader("3. Resume Skills")

        if resume_skills:
            st.write(", ".join(resume_skills))
        else:
            st.info("No recognized skills found.")

        if job_description.strip():

            cleaned_job = clean_text(job_description)

            job_skills = extract_skills(cleaned_job)

            matched_skills = [
                skill for skill in job_skills
                if skill in resume_skills
            ]

            missing_skills = [
                skill for skill in job_skills
                if skill not in resume_skills
            ]

            # SECTION 4

            st.divider()
            st.header("4. Skill Gap Analysis")

            col1, col2 = st.columns(2)

            with col1:
                st.subheader("Matched Skills")

                if matched_skills:
                    show_custom_alert(", ".join(matched_skills))
                else:
                    show_custom_alert("No matching skills found.")

            with col2:
                st.subheader("Missing Skills")

                if missing_skills:
                    show_custom_alert(", ".join(missing_skills))
                else:
                    show_custom_alert("All listed skills matched!")
# ==========================================

                # ==========================================
                # PERSONALIZED LEARNING ROADMAP
                # ==========================================

                st.divider()
                st.header("Personalized Skill Gap Learning Roadmap")

                st.write(
                    "Turn your missing skills into a structured learning plan."
                )

                if missing_skills:

                    roadmap = generate_learning_roadmap(missing_skills)

                    for index, item in enumerate(roadmap, 1):

                        with st.container(border=True):

                            st.subheader(f"{index}. {item['skill']}")

                            st.markdown("**Topics to Learn**")

                            for topic in item["topics"]:
                                st.write(f"• {topic}")

                            st.markdown("**Practice Task**")
                            st.write(item["practice"])

                            st.markdown("**Mini Project**")
                            st.write(item["project"])
                            st.markdown("**Suggested Duration**")
                            st.write(item.get("duration", "To be determined"))

                            st.markdown("**Learning Resources**")
                            for resource in item.get("resources", ["Official documentation and beginner tutorials"]):
                                st.write(f"• {resource}")

                            if item.get("custom", False):
                                st.caption(
                                    "General starter roadmap — this skill "
                                    "is not yet in the curated database."
                                )

                    

                                                 # ==========================================
                                      # ==========================================
                    # 4-WEEK LEARNING TIMELINE
                    # ==========================================

                    st.divider()
                    st.subheader("Your 4-Week Learning Timeline")

                    weekly_timeline = generate_weekly_timeline(roadmap)

                    for week, tasks in weekly_timeline.items():
                        with st.expander(week):
                            for task in tasks:
                                st.write(f"• {task}")

                    # ==========================================
                    # DOWNLOAD LEARNING ROADMAP PDF
                    # ==========================================

                    learning_pdf = generate_learning_pdf(
                        roadmap,
                        weekly_timeline
                    )

                    st.download_button(
                        label="Download My Learning Plan PDF",
                        data=learning_pdf,
                        file_name="ResumeIQ_Learning_Roadmap.pdf",
                        mime="application/pdf",
                        use_container_width=True,
                        key="learning_roadmap_pdf_download"
                    )  

                else:
                    st.success(
                        "Amazing! No missing skills detected for this job description."
                    )

            if job_skills:

                coverage = (
                    len(matched_skills) / len(job_skills)
                ) * 100

                st.metric(
                    "Required Skill Coverage",
                    f"{coverage:.2f}%"
                )

            # SIMILARITY

            similarity_score = calculate_similarity(
                cleaned_resume,
                cleaned_job
            )

            # ML PREDICTION

            combined_text = (
                "resume " + cleaned_resume +
                " job " + cleaned_job
            )

            prediction = model.predict([combined_text])[0]

            # SECTION 5

            st.divider()
            st.header("5. AI Resume Match Prediction")

            if prediction == "Good Fit":
                st.success("AI Prediction: Good Fit")

            elif prediction == "Potential Fit":
                st.warning("AI Prediction: Potential Fit")

            else:
                st.error("AI Prediction: No Fit")

            # SECTION 6

            st.divider()
            st.header("6. Resume Improvement Suggestions")

            skill_tips = {
                "Python": "Practise Python basics, functions, OOP and small projects.",
                "SQL": "Learn SELECT, JOIN, GROUP BY and subqueries.",
                "Machine Learning": "Study regression, classification and model evaluation.",
                "Deep Learning": "Learn neural networks and build a basic deep learning project.",
                "NLP": "Explore text preprocessing, tokenization and text classification.",
                "Pandas": "Practise data cleaning, filtering and data manipulation.",
                "NumPy": "Learn arrays, indexing and numerical operations.",
                "Scikit-learn": "Practise training, testing and evaluating ML models.",
                "Data Analysis": "Work on a dataset and practise extracting insights.",
                "Data Visualization": "Create charts and dashboards using Python."
            }

            if missing_skills:

                st.write(
                    "Here are some areas you can work on "
                    "to better match the job requirements:"
                )

                for skill in missing_skills:

                    tip = skill_tips.get(
                        skill,
                        f"Study {skill} and practise it through a small project."
                    )

                    with st.expander(f"Improve: {skill}"):
                        st.write(tip)

            else:

                st.success(
                    "Great! No missing skills were identified "
                    "from our current skill dictionary."
                )

            st.info(
                "Tip: Only add a skill to your resume when "
                "you have genuinely learned and practised it."
            )

            # SECTION 7

            st.divider()
            st.header("7. Resume Analytics Dashboard")

            if job_skills:

                dashboard_col1, dashboard_col2 = st.columns(2)

                with dashboard_col1:

                    st.metric(
                        "Total Required Skills",
                        len(job_skills)
                    )

                with dashboard_col2:

                    st.metric(
                        "Missing Skills",
                        len(missing_skills)
                    )

                chart_data = pd.DataFrame({
                    "Skill Status": ["Matched", "Missing"],
                    "Number of Skills": [
                        len(matched_skills),
                        len(missing_skills)
                    ]
                })

                st.subheader("Skill Match Breakdown")

                st.bar_chart(
                    chart_data.set_index("Skill Status")
                )

            else:

                st.info(
                    "No recognized job skills available "
                    "to generate the dashboard."
                )

            # CONFUSION MATRIX

            st.subheader("Model Evaluation - Confusion Matrix")

            confusion_matrix_path = "models/confusion_matrix.png"

            if os.path.exists(confusion_matrix_path):

                st.image(
                    confusion_matrix_path,
                    caption="ResumeIQ Model Confusion Matrix",
                    use_container_width=True
                )

            else:

                st.info(
                    "Confusion matrix image not found. "
                    "Please run src/train_model.py first."
                )

            # SECTION 8

            st.divider()
            st.header("8. Download Analysis Report")

            report_text = f"""
RESUMEIQ - RESUME ANALYSIS REPORT
=================================

RESUME SKILLS:
{', '.join(resume_skills) if resume_skills else 'None found'}

REQUIRED JOB SKILLS:
{', '.join(job_skills) if job_skills else 'None found'}

MATCHED SKILLS:
{', '.join(matched_skills) if matched_skills else 'None'}

MISSING SKILLS:
{', '.join(missing_skills) if missing_skills else 'None'}

SUGGESTIONS:
"""

            if missing_skills:

                for skill in missing_skills:

                    tip = skill_tips.get(
                        skill,
                        f"Study {skill} and practise it through a small project."
                    )

                    report_text += f"\n- {skill}: {tip}"

            else:

                report_text += (
                    "\nYour resume covers all recognized required skills."
                )

            st.download_button(
                label="Download Analysis Report",
                data=report_text,
                file_name="ResumeIQ_Analysis_Report.txt",
                mime="text/plain"
            )

            # SECTION 9

            if job_skills:

                skill_coverage_score = (
                    len(matched_skills) / len(job_skills)
                ) * 100

            else:

                skill_coverage_score = 0

            resume_strength_score = round(
                skill_coverage_score * 0.60
                + similarity_score * 0.40,
                2
            )

            st.divider()
            st.header("9. Resume Strength Score")

            st.metric(
                "Overall Resume Strength",
                f"{resume_strength_score}/100"
            )

            st.progress(
                int(max(0, min(100, resume_strength_score)))
            )

            st.metric(
                "Resume-Job Text Similarity",
                f"{similarity_score}%"
            )

        else:

            st.info(
                "Please enter a job description "
                "to compare your skills."
            )

    else:

        st.error(
            "Unable to extract readable text from this PDF."
        )

# ==========================================
# 10. PROJECT SHOWCASE
# ==========================================

st.divider()

st.header("About ResumeIQ")

st.write(
    """
    ResumeIQ is an AI-powered resume analysis platform designed
    to help students and job seekers understand how well their
    resumes match job descriptions.

    It analyzes resume skills, identifies skill gaps, evaluates
    resume-job similarity, and generates personalized learning
    recommendations.
    """
)

# TECHNOLOGY STACK

st.subheader("Technology Stack")

tech_col1, tech_col2, tech_col3 = st.columns(3)

with tech_col1:
    st.markdown("**Programming**")
    st.write("• Python")
    st.write("• Pandas")
    st.write("• NumPy")

with tech_col2:
    st.markdown("**AI / ML**")
    st.write("• Scikit-learn")
    st.write("• NLP")
    st.write("• TF-IDF / Similarity")

with tech_col3:
    st.markdown("**Development**")
    st.write("• Streamlit")
    st.write("• ReportLab")
    st.write("• Git & GitHub")

# KEY FEATURES

st.subheader("Key Features")

features = [
    "PDF Resume Parsing",
    "Automated Skill Extraction",
    "Resume and Job Description Matching",
    "Machine Learning Based Match Prediction",
    "ATS Compatibility Simulation",
    "Smart Bullet Point Enhancement",
    "Personalized Skill Gap Roadmap",
    "Four-Week Learning Timeline",
    "Downloadable Learning Plan PDF",
    "Resume Analytics Dashboard"
]

for feature in features:
    st.write(f"✓ {feature}")

# WORKFLOW

st.subheader("How ResumeIQ Works")

workflow = [
    "Upload your resume in PDF format.",
    "Enter the target job description.",
    "Extract and analyze resume information.",
    "Identify matched and missing skills.",
    "Calculate resume-job similarity.",
    "Generate improvement suggestions and a learning roadmap.",
    "Download your personalized learning plan."
]

for index, step in enumerate(workflow, 1):
    st.write(f"**Step {index}:** {step}")

st.info(
    "ResumeIQ is a portfolio project demonstrating "
    "Python, NLP, machine learning and application development."
)
# ==========================================
# 10. FOOTER
# ==========================================

st.divider()
st.caption("ResumeIQ | AI/ML Portfolio Project")


