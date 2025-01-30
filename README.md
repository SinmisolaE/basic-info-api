# Basic Information API

This project provides a simple API endpoint that returns basic information, including an email address, the current date and time, and a GitHub URL.  It's designed to demonstrate a basic API structure and handle Cross-Origin Resource Sharing (CORS) correctly.

## Description

This API exposes a single GET endpoint that returns data in JSON format. The data includes:

*   Your registered email address (obtained from an environment variable).
*   The current date and time in ISO 8601 format (UTC).
*   The GitHub URL of the project's codebase (obtained from an environment variable).

This API is built using the Flask framework in Python and utilizes the `flask-cors` library for handling CORS, which is essential for allowing web applications hosted on different domains to access the API.

## Setup Instructions

To run this project locally, follow these steps:

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/SinmisolaE/basic-info-api.git
    cd basic-info-api  
    ```


2.  **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    # OR install directly
    pip install Flask flask-cors
    ```

5.  **Set environment variables:**

    You must set the `EMAIL_ADDRESS` and `GITHUB_URL` environment variables.  The best way to do this for local development is to create a `.env` file in the project directory:

    ```
    EMAIL_ADDRESS="your_email@example.com"  # Replace with your actual email
    GITHUB_URL="[https://github.com/yourusername/yourrepository](https://github.com/yourusername/yourrepository)" # Replace with your repo URL
    ```

    Then, install `python-dotenv` and load the variables:

    ```bash
    pip install python-dotenv
    ```

    And in your `app.py` file:

    ```python
    import os
    from dotenv import load_dotenv

    load_dotenv()  # Load environment variables from .env file

    EMAIL_ADDRESS = os.environ.get("EMAIL_ADDRESS")
    GITHUB_URL = os.environ.get("GITHUB_URL")
    ```

    **Important:**  For production deployment, set these environment variables through your hosting platform's settings (Heroku, Render, AWS, etc.).  Do *not* include a `.env` file in your production deployment.

6.  **Run the Flask app:**

    ```bash
    python app.py
    ```

7.  **Access the API:**

    The API will be running at `http://127.0.0.1:5000/` (or the port specified by your hosting provider). You can access it using your browser, `curl`, Postman, or any other HTTP client.

## API Endpoint

**GET /**

Returns a JSON response with the email address, current date and time, and GitHub URL.

**Example Response:**

```json
{
  "email": "sinmisolaajao@gmail.com",
  "current_time": "2024-10-30T12:34:56.789Z",
  "github_url": "https://github.com/SinmisolaE/basic-info-api"
}

Flask Official Documentation: https://flask.palletsprojects.com/