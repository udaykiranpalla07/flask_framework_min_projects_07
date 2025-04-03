# Flask Contact Form API

## Overview
This is a Flask-based web application that provides a simple contact form API. It allows users to submit their name, email, and message, which are then stored in a MySQL database.

## Features
- Uses **Flask** for the web framework
- **Flask-CORS** to handle Cross-Origin Resource Sharing (CORS)
- **Flask-SQLAlchemy** for ORM-based database interactions
- **MySQL** as the database backend
- Reads database credentials from a configuration file (`configuration.ini`)
- Automatically creates the database table before handling requests

## Installation
### Prerequisites
Ensure you have the following installed:
- Python 3
- MySQL Database
- MySQL ODBC Driver (`MySQL ODBC 9.2 ANSI Driver`)

### Setup
1. Clone the repository:
   ```sh
   git clone <repository_url>
   cd <repository_folder>
   ```
2. Install dependencies:
   ```sh
   pip install -U flask flask-CORS flask-sqlalchemy pyodbc configparser
   ```
3. Configure the database credentials:
   - Create a `configuration.ini` file with the following content:
     ```ini
     [connection]
     username = your_db_username
     password = your_db_password
     ```
4. Run the application:
   ```sh
   python app.py
   ```

## API Endpoints
### 1. Home Page
- **URL:** `/`
- **Method:** `GET`
- **Response:** Renders `index.html`

### 2. Submit Contact Form
- **URL:** `/submit`
- **Method:** `POST`
- **Request Body (JSON):**
  ```json
  {
    "name": "John Doe",
    "email": "john.doe@example.com",
    "message": "Hello, this is a test message."
  }
  ```
- **Response (JSON):**
  ```json
  {
    "message": "Thank You, John Doe your message is received"
  }
  ```

## Database Schema
**Table: `Contact`**
| Column  | Type         | Constraints     |
|---------|------------|----------------|
| id      | Integer    | Primary Key    |
| name    | String(255) | Not Null       |
| email   | String(255) | Not Null       |
| message | Text       | Not Null       |



