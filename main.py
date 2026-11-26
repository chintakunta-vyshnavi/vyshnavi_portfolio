from pathlib import Path

from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


# -----------------------------------------
# APPLICATION CONFIGURATION
# -----------------------------------------

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(title="Vyshnavi Portfolio")

# Static files
app.mount(
    "/static",
    StaticFiles(directory=str(BASE_DIR / "static")),
    name="static"
)

# Templates
templates = Jinja2Templates(
    directory=str(BASE_DIR / "templates")
)


# -----------------------------------------
# PERSONAL INFORMATION
# -----------------------------------------

profile = {
    "name": "Chintakunta Vyshnavi",
    "role": "Aspiring Full Stack Developer",
    "location": "Kadapa, Andhra Pradesh",
    "email": "vyshnavireddychintakunta@gmail.com",
    "phone": "6XXXXXXX53",
    "linkedin": "https://www.linkedin.com/in/c-vyshnavi-reddy",
    "github": "https://github.com/chintakunta-vyshnavi",
    "about": (
        "I am a Computer Science Engineering student with an interest "
        "in Full Stack Development. I have knowledge of Python, FastAPI, "
        "HTML, CSS, JavaScript, SQL and MySQL. I enjoy developing "
        "web applications and exploring new technologies."
    )
}


# -----------------------------------------
# SKILLS
# -----------------------------------------

skills = [
    "HTML",
    "CSS",
    "JavaScript",
    "Python",
    "FastAPI",
    "OOPS",
    "SQL",
    "MySQL",
    "Git",
    "GitHub",
    "VS Code",
    "Excel"
]


# -----------------------------------------
# INTERNSHIPS
# -----------------------------------------

internships = [
    {
        "company": "Techno Hacks Solutions Pvt Ltd",
        "role": "Full Stack Development Intern",
        "duration": "May 2023 - June 2023",
        "description": (
            "Developed a To-Do CRUD application using HTML, CSS "
            "and JavaScript with database operations."
        )
    },
    {
        "company": "Main Flow Services and Technologies",
        "role": "Full Stack Development Intern",
        "duration": "June 2024 - July 2024",
        "description": (
            "Worked on a responsive landing page, login and signup "
            "form validation, and a Java Swing login application "
            "using MySQL and JDBC."
        )
    }
]


# -----------------------------------------
# EDUCATION
# -----------------------------------------

education = [
    {
        "degree": "B.Tech - Computer Science and Engineering",
        "institution": "Dhanalakshmi Srinivasan University",
        "duration": "September 2022 - June 2026",
        "score": "CGPA: 8.81"
    },
    {
        "degree": "Intermediate - MPC",
        "institution": "Sri Chaitanya Junior College",
        "duration": "July 2020 - May 2022",
        "score": "Percentage: 91.3%"
    },
    {
        "degree": "SSC",
        "institution": "S S V N High School",
        "duration": "June 2019 - March 2020",
        "score": "Percentage: 99.7%"
    }
]


# -----------------------------------------
# PROJECTS
# -----------------------------------------

projects = [
    {
        "title": "Product Display Application",
        "description": (
            "A web application for displaying product information."
        ),
        "tech": ["Python", "FastAPI", "HTML", "CSS"],
        "github": (
            "https://github.com/chintakunta-vyshnavi/product_displaying"
        )
    },
    {
        "title": "Task Manager",
        "description": (
            "A task management application for organizing "
            "and tracking daily activities."
        ),
        "tech": ["HTML", "CSS", "JavaScript"],
        "github": (
            "https://github.com/chintakunta-vyshnavi/task_manager"
        )
    },
    {
        "title": "Dental Web Page",
        "description": (
            "A responsive dental website interface."
        ),
        "tech": ["HTML", "CSS", "JavaScript"],
        "github": (
            "https://github.com/chintakunta-vyshnavi/dental_page"
        )
    },
    {
        "title": "Multiple Disease Prediction",
        "description": (
            "A machine learning project using SVM and Decision Tree "
            "algorithms for disease prediction."
        ),
        "tech": ["Python", "Machine Learning"],
        "github": "https://github.com/chintakunta-vyshnavi"
    },
    {
        "title": "Accident Prevention and Weather Monitoring",
        "description": (
            "An IoT-based project focused on accident prevention "
            "and weather monitoring."
        ),
        "tech": ["IoT", "Sensors"],
        "github": "https://github.com/chintakunta-vyshnavi"
    }
]


# -----------------------------------------
# CERTIFICATIONS
# -----------------------------------------

certifications = [
    "HTML, CSS and JavaScript - Udemy",
    "Python 101 for Data Science - IBM",
    "SQL - Scaler",
    "Blockchain Masterclass - BITSCRUNCH",
    "Front-End Software Engineering Simulation - Forage",
    "Ideathon Participation Certificate"
]


# -----------------------------------------
# HOME PAGE
# -----------------------------------------

@app.get("/")
async def home(request: Request, tech: str = None):

    # Get theme from browser cookie
    theme = request.cookies.get("theme", "light")

    # Initially display all projects
    filtered_projects = projects

    # Filter projects by technology
    if tech:
        filtered_projects = [
            project
            for project in projects
            if any(
                tech.lower() in technology.lower()
                for technology in project["tech"]
            )
        ]

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "request": request,
            "profile": profile,
            "skills": skills,
            "internships": internships,
            "education": education,
            "projects": filtered_projects,
            "certifications": certifications,
            "theme": theme,
            "tech": tech
        }
    )


# -----------------------------------------
# THEME SWITCHING
# -----------------------------------------

@app.post("/set-theme")
async def set_theme(request: Request):

    current_theme = request.cookies.get("theme", "light")

    if current_theme == "light":
        new_theme = "dark"
    else:
        new_theme = "light"

    response = RedirectResponse(
        url="/",
        status_code=303
    )

    response.set_cookie(
        key="theme",
        value=new_theme,
        max_age=2592000,
        httponly=True,
        samesite="lax"
    )

    return response


# -----------------------------------------
# CONTACT FORM
# -----------------------------------------

@app.post("/contact")
async def contact(
    name: str = Form(...),
    email: str = Form(...),
    message: str = Form(...)
):

    print("\nNew Contact Message")
    print("-------------------")
    print("Name:", name)
    print("Email:", email)
    print("Message:", message)

    return RedirectResponse(
        url="/#contact",
        status_code=303
    )


# -----------------------------------------
# RUN APPLICATION
# -----------------------------------------

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )