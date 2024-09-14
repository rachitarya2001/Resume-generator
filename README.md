# LinkedIn Resume Generator

## Overview

This project involves creating a web application that converts a LinkedIn PDF download into an HTML resume using OpenAI's API. The application allows users to upload their LinkedIn PDFs, extracts text from these PDFs, and then uses OpenAI's API to generate a formatted HTML resume.

## Approach

### 1. **Project Setup**

- **Create Project Directory:**
  - Initiated a new project folder named `linkedin-resume-generator` to keep all project files organized.

- **Set Up Virtual Environment:**
  - Created a Python virtual environment to manage project dependencies and ensure an isolated development environment:
    ```bash
    python -m venv venv
    ```
  - Activated the virtual environment:
    - **Windows:**
      ```bash
      venv\Scripts\activate
      ```
    - **Mac/Linux:**
      ```bash
      source venv/bin/activate
      ```

- **Install Required Packages:**
  - Installed necessary Python libraries:
    - `Flask` for the web framework.
    - `PyPDF2` for PDF text extraction.
    - `openai` for interacting with OpenAI's API:
      ```bash
      pip install flask PyPDF2 openai
      ```

### 2. **Developing the Flask Application**

- **Create Flask App:**
  - Developed a Flask application to handle file uploads and generate HTML resumes. Created a file named `app.py` containing the application logic.

- **File Upload Handling:**
  - Implemented a route for handling PDF file uploads. Used `PyPDF2` to extract text from the uploaded PDF files.

- **Integrate OpenAI API:**
  - Configured OpenAI's API to convert the extracted text into an HTML format. Added the OpenAI API key in `app.py` and set up a prompt to format the resume.

- **Return HTML Resume:**
  - The application generates and returns the HTML resume to the user as a response.

### 3. **Creating HTML Templates**

- **Upload Form:**
  - Created an HTML file named `index.html` within a `templates` folder to provide a user interface for file uploads.

- **Display HTML Resume:**
  - Ensured the application correctly renders the generated HTML resume in the browser.

### 4. **Testing the Application**

- **Local Testing:**
  - Ran the Flask application locally to ensure that file uploads, text extraction, and resume generation functions work as expected.

### 5. **Deployment**

- **Deploy to Vercel:**
  - Deployed the application using Vercel for hosting. Followed Vercel’s deployment process to upload the project and obtain a deployment URL.
  
  - **Commands Used:**
    ```bash
    npm install -g vercel
    vercel
    ```

- **Alternative Deployment on GitHub Pages:**
  - As an alternative deployment option, pushed the code to GitHub and configured GitHub Pages to serve the application.
  
  - **GitHub Pages Setup:**
    - Go to repository **Settings**.
    - Under **Pages**, set the source to the `main` branch and the root directory.

### 6. **README.md File**

- **Documentation:**
  - Created a `README.md` file to provide an overview of the project, setup instructions, deployment details, and usage instructions. Included information on how to run the application and where to find it deployed.

## Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/rachitarya2001/Resume-generator.git
   cd Resume-generator
