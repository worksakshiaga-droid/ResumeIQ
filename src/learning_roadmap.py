
def make_skill(topics, practice, project, duration, resources):
    return {
        "topics": topics,
        "practice": practice,
        "project": project,
        "duration": duration,
        "resources": resources
    }


SKILL_DATABASE = {

    # PROGRAMMING
    "python": make_skill(
        ["Python syntax and data types", "Conditions and loops",
         "Functions and modules", "OOP concepts",
         "File handling and exception handling", "Libraries and packages"],
        "Solve Python coding exercises and work with files.",
        "Build a command-line expense tracker.",
        "2-3 weeks",
        ["Python Official Tutorial", "Kaggle Learn: Python"]
    ),

    "java": make_skill(
        ["Java syntax", "Classes and objects", "Inheritance and polymorphism",
         "Exception handling", "Collections Framework", "File handling"],
        "Write small programs using Java OOP.",
        "Build a library management system.",
        "3-4 weeks",
        ["Oracle Java Tutorials", "W3Schools Java"]
    ),

    "c++": make_skill(
        ["C++ fundamentals", "Functions and pointers", "OOP",
         "STL", "Data structures", "Memory management"],
        "Solve programming problems using C++.",
        "Build a student record management system.",
        "3-4 weeks",
        ["LearnCpp", "C++ Reference"]
    ),

    "javascript": make_skill(
        ["JavaScript fundamentals", "Variables and functions",
         "Arrays and objects", "DOM manipulation",
         "Asynchronous JavaScript", "APIs"],
        "Create interactive browser-based exercises.",
        "Build a task management web application.",
        "3-4 weeks",
        ["MDN JavaScript Guide", "JavaScript.info"]
    ),

    # MACHINE LEARNING AND AI
    "machine learning": make_skill(
        ["Supervised and unsupervised learning",
         "Regression and classification",
         "Decision trees and ensemble models",
         "Feature engineering", "Train-test split",
         "Model evaluation and cross-validation"],
        "Train and compare multiple ML models on a dataset.",
        "Build a student performance prediction system.",
        "4-6 weeks",
        ["Scikit-learn Documentation", "Google Machine Learning Crash Course"]
    ),

    "scikit-learn": make_skill(
        ["Scikit-learn fundamentals", "Data preprocessing",
         "Train-test split", "Regression models",
         "Classification models", "Pipelines and model evaluation"],
        "Train and evaluate different models using Scikit-learn.",
        "Create an end-to-end ML prediction application.",
        "2-3 weeks",
        ["Scikit-learn User Guide", "Kaggle Learn: Intro to Machine Learning"]
    ),

    "tensorflow": make_skill(
        ["TensorFlow fundamentals", "Tensors and operations",
         "Building neural networks", "Model training",
         "Loss functions and optimizers", "Model evaluation"],
        "Train a simple neural network using TensorFlow.",
        "Build an image classification model.",
        "3-4 weeks",
        ["TensorFlow Tutorials", "Google Colab"]
    ),

    "pytorch": make_skill(
        ["PyTorch tensors", "Autograd",
         "Neural network modules", "DataLoaders",
         "Training loops", "Model evaluation"],
        "Build and train a basic neural network.",
        "Create an image classification project.",
        "3-4 weeks",
        ["PyTorch Tutorials", "Google Colab"]
    ),

    "deep learning": make_skill(
        ["Neural network fundamentals", "Activation functions",
         "Forward and backward propagation", "Loss functions",
         "Optimizers", "CNN and RNN basics"],
        "Train a neural network and compare its performance.",
        "Build a handwritten digit recognition system.",
        "4-6 weeks",
        ["DeepLearning.AI", "TensorFlow Tutorials"]
    ),

    "nlp": make_skill(
        ["Text preprocessing", "Tokenization",
         "Stopword removal and stemming", "TF-IDF",
         "Word embeddings", "Transformer fundamentals"],
        "Clean and classify a collection of text data.",
        "Build a text sentiment analysis application.",
        "3-4 weeks",
        ["Hugging Face NLP Course", "NLTK Documentation"]
    ),

    "natural language processing": make_skill(
        ["Text preprocessing", "Tokenization",
         "TF-IDF and text vectorization",
         "Word embeddings", "Transformer fundamentals",
         "Text classification"],
        "Build a text classification experiment.",
        "Create a sentiment analysis application.",
        "3-4 weeks",
        ["Hugging Face NLP Course", "NLTK Documentation"]
    ),

    "computer vision": make_skill(
        ["Image processing basics", "Image augmentation",
         "Convolutional neural networks", "Image classification",
         "Object detection basics", "Model evaluation"],
        "Experiment with image datasets and classification.",
        "Build an image recognition application.",
        "4-6 weeks",
        ["OpenCV Documentation", "TensorFlow Computer Vision Tutorials"]
    ),

    # DATA SCIENCE AND ANALYTICS
    "data analysis": make_skill(
        ["Data collection", "Data cleaning",
         "Exploratory data analysis", "Pandas",
         "Data visualization", "Insight communication"],
        "Analyze a real-world dataset and identify patterns.",
        "Create an interactive data analysis dashboard.",
        "3-4 weeks",
        ["Kaggle Learn: Data Cleaning", "Pandas Documentation"]
    ),

    "pandas": make_skill(
        ["Series and DataFrames", "Reading datasets",
         "Filtering and sorting", "Handling missing values",
         "Grouping and aggregation", "Merging datasets"],
        "Clean and analyze a CSV dataset using Pandas.",
        "Build a complete exploratory data analysis report.",
        "1-2 weeks",
        ["Pandas Getting Started", "Kaggle Learn: Pandas"]
    ),

    "numpy": make_skill(
        ["NumPy arrays", "Array indexing",
         "Array operations", "Broadcasting",
         "Statistical functions", "Linear algebra basics"],
        "Perform numerical operations on a dataset.",
        "Build a small numerical data analysis toolkit.",
        "1-2 weeks",
        ["NumPy Quickstart", "NumPy Documentation"]
    ),

    "statistics": make_skill(
        ["Descriptive statistics", "Mean, median and mode",
         "Variance and standard deviation",
         "Probability", "Hypothesis testing",
         "Correlation and regression"],
        "Analyze a dataset using statistical methods.",
        "Create a statistical analysis report.",
        "2-3 weeks",
        ["Khan Academy Statistics", "OpenIntro Statistics"]
    ),

    "sql": make_skill(
        ["SELECT and WHERE", "Sorting and filtering",
         "GROUP BY and aggregate functions",
         "INNER and OUTER JOINs", "Subqueries",
         "Window functions"],
        "Solve SQL queries using a sample database.",
        "Build a student performance database.",
        "2-3 weeks",
        ["SQLBolt", "Mode SQL Tutorial"]
    ),

    "excel": make_skill(
        ["Excel formulas", "IF and lookup functions",
         "Sorting and filtering", "Pivot tables",
         "Charts and conditional formatting",
         "Data cleaning"],
        "Analyze a spreadsheet using formulas and pivot tables.",
        "Create an interactive sales analysis dashboard.",
        "1-2 weeks",
        ["Microsoft Excel Training", "Excel Easy"]
    ),

    "power bi": make_skill(
        ["Power BI interface", "Data loading",
         "Power Query", "Data modelling",
         "DAX fundamentals", "Dashboard design"],
        "Import and visualize a sample business dataset.",
        "Build an interactive business intelligence dashboard.",
        "3-4 weeks",
        ["Microsoft Learn: Power BI", "Power BI Documentation"]
    ),

    "tableau": make_skill(
        ["Tableau interface", "Connecting data sources",
         "Dimensions and measures", "Charts and visualizations",
         "Calculated fields", "Interactive dashboards"],
        "Create visualizations using a sample dataset.",
        "Build an interactive business analytics dashboard.",
        "2-3 weeks",
        ["Tableau Learning", "Tableau Help"]
    ),

    # DEVELOPMENT
    "flask": make_skill(
        ["Flask fundamentals", "Routing and templates",
         "Request handling", "Forms",
         "Database integration", "Building APIs"],
        "Create a small Flask application with multiple routes.",
        "Build a simple job application tracker.",
        "2-3 weeks",
        ["Flask Official Documentation", "MDN Web Docs"]
    ),

    "fastapi": make_skill(
        ["FastAPI fundamentals", "Path and query parameters",
         "Request and response models", "Pydantic",
         "API validation", "API documentation"],
        "Create and test REST API endpoints.",
        "Build an ML model prediction API.",
        "2-3 weeks",
        ["FastAPI Official Tutorial", "Pydantic Documentation"]
    ),

    "streamlit": make_skill(
        ["Streamlit fundamentals", "Widgets and inputs",
         "Session state", "Displaying data",
         "Charts and visualizations", "App deployment"],
        "Create an interactive data application.",
        "Build an AI-powered data analysis dashboard.",
        "1-2 weeks",
        ["Streamlit Documentation", "Streamlit Tutorials"]
    ),

    # TOOLS
    "git": make_skill(
        ["Version control fundamentals", "Git repositories",
         "Commits and branches", "Merging",
         "Resolving conflicts", "Remote repositories"],
        "Practice committing and branching in a sample project.",
        "Maintain a project using Git and GitHub.",
        "1-2 weeks",
        ["Git Official Book", "GitHub Skills"]
    ),

    "github": make_skill(
        ["Repositories", "README files",
         "Branches and pull requests", "Issues",
         "Collaboration", "Project documentation"],
        "Upload and document a personal project.",
        "Create a well-documented GitHub portfolio repository.",
        "1 week",
        ["GitHub Skills", "GitHub Docs"]
    ),

    "docker": make_skill(
        ["Container fundamentals", "Images and containers",
         "Dockerfiles", "Volumes",
         "Networking basics", "Docker Compose"],
        "Containerize a small Python application.",
        "Package and run an ML application using Docker.",
        "2-3 weeks",
        ["Docker Get Started", "Docker Documentation"]
    )
}


# Handle different spellings of common skill names
ALIASES = {
    "sklearn": "scikit-learn",
    "scikit learn": "scikit-learn",
    "ml": "machine learning",
    "ai": "artificial intelligence",
    "natural language processing": "nlp",
    "powerbi": "power bi",
    "js": "javascript",
    "cv": "computer vision"
}


def generate_learning_roadmap(missing_skills):

    roadmap = []

    for skill in missing_skills:

        skill_name = skill.strip().lower()
        skill_name = ALIASES.get(skill_name, skill_name)

        details = SKILL_DATABASE.get(skill_name)

        if details:

            roadmap.append({
                "skill": skill,
                **details,
                "custom": False
            })

        else:

            roadmap.append({
                "skill": skill,
                "topics": [
                    f"Introduction to {skill}",
                    f"Core concepts of {skill}",
                    f"Important tools used in {skill}",
                    f"Practical applications of {skill}",
                    f"Best practices in {skill}"
                ],
                "practice": f"Complete beginner exercises related to {skill}.",
                "project": f"Build a small practical project using {skill}.",
                "duration": "To be determined",
                "resources": [
                    "Search for official documentation",
                    "Look for beginner tutorials and guided exercises"
                ],
                "custom": True
            })

    return roadmap

def generate_weekly_timeline(roadmap):

    weeks = {
        "Week 1 - Fundamentals": [],
        "Week 2 - Core Concepts": [],
        "Week 3 - Hands-on Practice": [],
        "Week 4 - Mini Projects": []
    }

    week_names = list(weeks.keys())

    for item in roadmap:

        skill = item["skill"]
        topics = item.get("topics", [])

        # Distribute learning topics across 3 weeks
        for index, topic in enumerate(topics):

            if index < len(topics) / 3:
                week_index = 0
            elif index < (2 * len(topics)) / 3:
                week_index = 1
            else:
                week_index = 2

            weeks[week_names[week_index]].append(
                f"{skill}: {topic}"
            )

        # Practice task in Week 3
        weeks["Week 3 - Hands-on Practice"].append(
            f"{skill}: {item.get('practice', 'Complete practical exercises.')}"
        )

        # Project in Week 4
        weeks["Week 4 - Mini Projects"].append(
            f"{skill}: {item.get('project', 'Build a small practical project.')}"
        )

    return weeks
