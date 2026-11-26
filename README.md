# 🌐 Personal Portfolio Website – FastAPI

## 📌 Project Overview

This project is a personal portfolio website developed using Python and the FastAPI framework. It showcases personal information, technical skills, educational qualifications, internship experience, projects, and certifications.

The website uses Server-Side Rendering (SSR) with Jinja2 templates to dynamically display portfolio information. It also includes a responsive design and cookie-based Dark/Light theme functionality.

## 🚀 Features

- **About Me:** Introduction and professional profile.
- **Technical Skills:** Displays programming languages, frameworks, and tools.
- **Education:** Academic qualifications and achievements.
- **Internship Experience:** Details of professional internship experience.
- **Projects:** Showcases projects with descriptions and GitHub links.
- **Certifications:** Displays completed courses and certifications.
- **Contact Form:** Allows visitors to submit contact information.
- **Dark/Light Mode:** Switches between light and dark themes.
- **Cookie Persistence:** Saves theme preferences using HTTP cookies.
- **Project Filtering:** Filters projects based on technologies.
- **Responsive Design:** Supports desktop, tablet, and mobile screens.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| FastAPI | Web framework |
| Jinja2 | Server-side rendering |
| HTML5 | Webpage structure |
| CSS3 | Styling and responsive design |
| Uvicorn | ASGI server |
| Cookies | Theme preference persistence |

## 📂 Project Structure

```text
portfolio_app/
│
├── main.py
├── requirements.txt
│
├── templates/
│   ├── base.html
│   └── index.html
│
└── static/
    └── css/
        └── style.css
```

## 💻 Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the Project Folder

```bash
cd portfolio_app
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate Virtual Environment

For Windows PowerShell:

```powershell
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Application

```bash
uvicorn main:app --reload
```

### 7. Open in Browser

```text
http://127.0.0.1:8000
```

## ⚙️ Application Functionality

### 1. Server-Side Rendering

Jinja2 templates dynamically display portfolio information using backend Python data.

### 2. Static File Handling

FastAPI StaticFiles serves CSS files from the static directory.

### 3. Theme Switching

The application provides Dark and Light themes using a POST `/set-theme` endpoint.

### 4. Cookie Management

Theme preferences are stored using HTTP cookies with:

- Max Age: 2592000 seconds
- HttpOnly: True
- SameSite: Lax

### 5. Project Filtering

Visitors can filter projects using technology names through the query parameter.

Example:

```text
http://127.0.0.1:8000/?tech=Python#projects
```

### 6. Contact Form

The contact form uses FastAPI POST handling to process submitted information and redirect visitors.

Note: The current implementation demonstrates form submission but does not send emails or save messages to a database.

## 🔗 My GitHub Projects

1. **Product Displaying Application**

   https://github.com/chintakunta-vyshnavi/product_displaying

2. **Task Manager Application**

   https://github.com/chintakunta-vyshnavi/task_manager

3. **Dental Website**

   https://github.com/chintakunta-vyshnavi/dental_page

## 🎯 Learning Outcomes

- Understanding FastAPI application development.
- Implementing Jinja2 template inheritance.
- Working with static files and dynamic URL generation.
- Understanding HTTP methods and redirections.
- Managing cookies and user preferences.
- Building responsive web applications.
- Organizing full-stack application structures.

## 👩‍💻 Author

**Chintakunta Vyshnavi**

- Location: Kadapa, Andhra Pradesh
- Email: vyshnavireddychintakunta@gmail.com
- LinkedIn: https://www.linkedin.com/in/c-vyshnavi-reddy
- GitHub: https://github.com/chintakunta-vyshnavi

---

⭐ Thank you for visiting my portfolio project!
