# TaskPulse - Mini Project
## Project Description
TaskPulse is a simple web page designed to help users manage their tasks efficiently. The application is built using Flask, a popular web framework in Python, and leverages SQLAlchemy for seamless integration with a MySQL database.

## Technologies Used
- `Flask:` The web framework used for building the application.
- `SQLAlchemy:` An SQL toolkit and Object-Relational Mapping (ORM) library used for database interactions.
- `MySQL:` The relational database system employed to store and manage task-related data.
- `Bootstrap:` A front-end framework for styling and responsiveness.
- `jQuery:` A fast, small, and feature-rich JavaScript library for client-side scripting.
- `HTML/CSS:` The standard markup language and style sheet language for designing the web interface.

## Dependencies
Ensure you have the following dependencies installed to run TaskPulse:

- **`Flask:`** pip install Flask
- **`Flask-SQLAlchemy:`** pip install Flask-SQLAlchemy
- **`Flask-Migrate:`** pip install Flask-Migrate
- **`MySQL:`** Install and configure a MySQL server, and create a database named tasklist.

## Setup Instructions
1. Clone the repository: `git clone https://github.com/yourusername/taskpulse.git`
2. Navigate to the project directory: `cd taskpulse`
3. Install dependencies: `pip install -r requirements.txt`
4. Update the database URI in app.py to match your MySQL configuration:
 - `app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://your_username:your_password@localhost/tasklist'`

5. Run database migrations:
   - flask db init
   - flask db migrate -m "Initial migration"
   - flask db upgrade
6. Run the application: `python app.py`
7. Access the application in your web browser at `http://localhost:5000`
