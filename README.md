# Flask Learning Lab

A beginner-friendly Python Flask project for learning web development, HTTP requests, dynamic routes, and JSON APIs.

## 1. Project Overview

This project is a small Flask application developed as part of my Python web development learning.

The purpose is to understand how a Flask application receives HTTP requests, matches URLs to Python functions, processes input data, and returns responses to clients.

The project currently contains one Python file: `app.py`.

## 2. Current Features

### 2.1 Home Page

**Route:** `GET /`

Returns a simple HTML message:

```html
<p>Hello, Flask!</p>
```

Concepts:
- Flask application initialization
- URL routing
- View functions
- HTTP GET requests
- Returning HTML content

### 2.2 Goodbye Page

**Route:** `GET /bye`

Returns:

```html
<p>Bye, Flask!</p>
```

This route demonstrates how multiple URLs can map to different Python functions in the same Flask application.

### 2.3 POST JSON API

**Route:** `POST /api/greet`

This endpoint receives JSON data from a client and returns a JSON response.

Example request:

```json
{
    "name": "Richard"
}
```

Example response:

```json
{
    "message": "Hello, Richard!",
    "success": true
}
```

Concepts:
- HTTP POST requests
- JSON request bodies
- `request.get_json()`
- Python dictionaries
- `jsonify()`
- REST API fundamentals

The current implementation is a basic learning example. Input validation and error handling can be added in a later exercise.

### 2.4 Dynamic Username Route

**Route:** `GET /username/<name>`

Example:

```text
http://127.0.0.1:5000/username/Alex
```

Expected response:

```text
Alex is learning Flask
```

This demonstrates how a URL path parameter is passed to a Python function.

### 2.5 Integer User ID Route

**Route:** `GET /username/<int:id>`

Example:

```text
http://127.0.0.1:5000/username/123
```

Expected response:

```text
User ID is 123
```

The `int` converter restricts the parameter to an integer.

The username and user ID routes use similar URL patterns but different converters. Testing both routes helps explain Flask's URL matching rules.

## 3. Project Structure

Current structure:

```text
FlaskLearningLab/
├── app.py
└── README.md
```

The project currently keeps all routes and application logic in one Python file to make the examples easier to follow.

As the project grows, the code can be divided into modules.

## 4. Requirements

- Python 3
- pip
- Flask
- A terminal or command-line tool
- A web browser
- Optional: Postman or curl for testing APIs

## 5. Installation

### Step 1: Open the Project Directory

Open the project folder in VS Code and open its integrated terminal.

### Step 2: Create a Virtual Environment

```bash
python3 -m venv venv
```

On Windows, you may use:

```powershell
py -m venv venv
```

### Step 3: Activate the Virtual Environment

macOS or Linux:

```bash
source venv/bin/activate
```

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 4: Install Flask

```bash
python -m pip install flask
```

## 6. Run the Application

Start the Flask development server:

```bash
python app.py
```

The application should be available at:

```text
http://127.0.0.1:5000
```

The current application uses:

```python
if __name__ == "__main__":
    app.run(debug=True)
```

The debug option is useful during local development because it enables debugging support and automatic reloading.

**Security note:** Debug mode must not be enabled on a publicly accessible production server.

## 7. Test the GET Routes

Open the following URLs in a browser.

| URL | Expected result |
|---|---|
| `http://127.0.0.1:5000/` | Hello, Flask! |
| `http://127.0.0.1:5000/bye` | Bye, Flask! |
| `http://127.0.0.1:5000/username/Alex` | Alex is learning Flask |
| `http://127.0.0.1:5000/username/123` | User ID is 123 |

These tests demonstrate static routes and dynamic routes.

## 8. Test the POST JSON API

A browser address bar normally sends GET requests. To test the POST endpoint, use curl or Postman.

### Using curl

Keep the Flask server running, then open a second terminal.

macOS or Linux:

```bash
curl -X POST http://127.0.0.1:5000/api/greet \
  -H "Content-Type: application/json" \
  -d '{"name": "Richard"}'
```

Windows PowerShell:

```powershell
curl.exe -X POST http://127.0.0.1:5000/api/greet `
  -H "Content-Type: application/json" `
  -d '{"name": "Richard"}'
```

Expected response:

```json
{
    "message": "Hello, Richard!",
    "success": true
}
```

### Using Postman

1. Select the `POST` method.
2. Enter `http://127.0.0.1:5000/api/greet`.
3. Open **Body → raw → JSON**.
4. Enter:

   ```json
   {
       "name": "Richard"
   }
   ```

5. Click **Send**.
6. Check the JSON response.

## 9. Key Concepts Learned

### Flask Basics
- Creating a Flask application with `Flask(__name__)`
- Defining routes with `@app.route()`
- Writing view functions
- Starting a local development server

### HTTP
- GET and POST methods
- URL paths and path parameters
- HTTP request and response
- The difference between browser navigation and POST requests

### JSON API
- Reading JSON request data with `request.get_json()`
- Returning JSON with `jsonify()`
- Using Python dictionaries to represent structured data

### Python Programming
- Functions and parameters
- String formatting with f-strings
- Conditional logic and type conversion
- Separating request handling from business logic

### Development Skills
- Running Python applications from the terminal
- Using curl and Postman
- Inspecting HTTP responses
- Diagnosing route and request errors

## 10. Known Limitations

The current project is intentionally simple and has not yet implemented:

- JSON input validation
- Consistent error responses
- Automated unit tests
- HTML templates and external CSS
- Logging and application configuration
- Database operations
- Authentication and authorization

The `/api/greet` endpoint assumes that the client sends a valid JSON object. Invalid JSON or a missing request body may result in an error.

These limitations provide useful opportunities for future exercises.

## 11. Future Learning Roadmap

### Exercise 1: Improve JSON Validation
- Handle missing or invalid JSON.
- Check whether the `name` field exists.
- Reject invalid input.
- Return appropriate HTTP status codes, such as 400.

### Exercise 2: Learn Query Parameters
- Read query parameters using `request.args`.
- Build a simple search endpoint.

Example:

```text
GET /api/greet?name=Richard
```

### Exercise 3: Learn HTML Templates
- Create a `templates/` directory.
- Use `render_template()`.
- Pass Python data to HTML using Jinja.

### Exercise 4: Learn Unit Testing
- Use Python's `unittest` module.
- Create a Flask test client.
- Test routes, response bodies, and status codes.

### Exercise 5: Organize the Project
- Separate routes and business logic.
- Learn Flask application configuration.
- Add a `requirements.txt` file.
- Keep code readable and maintainable.

### Exercise 6: Build a CRUD API
- Connect the application to SQLite.
- Create, read, update, and delete records.
- Practice data validation and error handling.

## 12. Summary

Flask Learning Lab starts with simple web routes and gradually introduces JSON APIs.

The main learning objective is to understand the complete request-response cycle:

1. A client sends an HTTP request.
2. Flask matches the URL and HTTP method.
3. A Python function processes the request.
4. Flask returns an HTML or JSON response.
5. The client receives and interprets the response.

This project provides a foundation for learning REST APIs and building larger Python web applications.