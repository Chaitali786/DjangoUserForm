# DjangoUserForm

# UserForm

UserForm is a simple Django application for creating a form where users can input their first name, last name, and email address. The submitted data is then saved into a database.

## Table of Contents

- [About the Project](#about-the-project)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)


## About the Project

UserForm provides a basic form interface for collecting user information. It utilizes Django's built-in forms and models to handle form submission and data storage. This project is ideal for beginners who want to learn Django by building a simple web application.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following prerequisites installed:

- Python (version 3.x)
- Django (version 3.x)

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/UserForm.git
   ```

2. Navigate to the project directory:
   ```
   cd UserForm
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```
   python manage.py migrate
   ```

## Usage

1. Start the Django development server:
   ```
   python manage.py runserver
   ```

2. Access the UserForm application in your web browser at `http://127.0.0.1:8000/user_form/`.

3. Fill out the form fields with your information and click the Submit button.

4. Verify that the data is saved into the database by checking the Django admin interface at `http://127.0.0.1:8000/admin/`.



