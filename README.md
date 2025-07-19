HELLOOOOOOOOOOOOOO

# Job Applicant Dashboard

This project is a Django web application that serves as a Job Applicant Dashboard for the "Junior Developer" position. It allows you to manage applicants, view their portfolios, and delete their records.

## Features

* **Applicant Listing:** A table displaying the first name, last name, email, and action buttons for each applicant.
* **Applicant Portfolio Detail:** A dedicated page to view the detailed portfolio of an applicant, including their personal information, portfolio title and description, and associated project details.
* **Delete Functionality:** Ability to delete an applicant, which also removes their associated portfolio and project from the database.
* **Django Admin Integration:** All data can be managed through the Django admin interface.
* **Bootstrap Styling:** The entire dashboard is styled using Bootstrap, hosted as a static CDN.

## Project Structure
Quiz2/

├── portfolio/              # Django app for portfolio and applicant management
├── Quiz2/                  # Main Django project settings
├── static/                 # Directory for static files (Bootstrap CSS/JS)
├── templates/              # Base template directory, containing app-specific subdirectories
│   └── portfolio/
├── .gitignore              # Excludes virtual environment and database from Git
├── manage.py               # Django's command-line utility
└── requirements.txt        # Python dependencies

SETUP INSTRUCTIONS
1. Get the Code (Clone Repository)
First, you need to download the project files.

Open your terminal or command prompt.

Navigate to the folder where you want to save your project (e.g., cd Documents/Projects).

Run this command to copy the project from GitHub:

Bash

git clone <your-github-repo-url>
(Replace <your-github-repo-url> with the actual URL of your GitHub repository).

Move into your new project folder:

Bash

cd Quiz2
2. Set Up a Python Environment (Virtual Environment)
It's best practice to create a virtual environment. Think of it as an isolated space for your project's Python packages, so they don't conflict with other projects on your computer.

Create the virtual environment:

Bash

python -m venv venv
This creates a folder named venv inside your project directory.

Activate the virtual environment:

On Windows (Command Prompt):

Bash

.\venv\Scripts\activate
On macOS/Linux (Bash/Zsh):

Bash

source venv/bin/activate
You'll know it's active when you see (venv) at the beginning of your terminal prompt.

3. Install Required Software (Python Packages)
Now, install all the necessary Python libraries that your Django project needs. These are listed in a file called requirements.txt.

Make sure your virtual environment is active (Step 2).

Run this command:

Bash

pip install -r requirements.txt
This will install Django and any other dependencies.

(Your requirements.txt file should simply contain Django~=5.0)

4. Prepare the Database (Migrations)
Django uses a database to store all your data (like applicant information). These commands tell Django to create the necessary tables in your database based on your project's models.

Generate migration files:

Bash

python manage.py makemigrations portfolio
This command detects changes in your portfolio app's models and creates small Python files describing those changes.

Apply migrations to the database:

Bash

python manage.py migrate
This command executes all pending migrations for your entire project, setting up the database tables.

5. Create an Admin User (Superuser)
You'll need an administrator account to access Django's built-in admin panel. This panel is where you can easily add, edit, and delete applicants, portfolios, and projects.

Run this command:

Bash

python manage.py createsuperuser
Follow the prompts:

Enter a username (e.g., admin).

Enter an email address.

Enter and confirm a password. (It won't show on the screen as you type).

6. Start the Web Application (Run Server)
Finally, launch the Django development server to see your dashboard in action!

Run this command:

Bash

python manage.py runserver
Open your web browser and go to http://127.0.0.1:8000/. You should see the junior developer .

You can also access the Django Admin Panel at http://127.0.0.1:8000/admin/ using the superuser credentials you created.
