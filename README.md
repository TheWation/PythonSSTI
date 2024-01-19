# FastAPI with Jinja2 SSTI Vulnerable Lab

[![made-with-python](http://forthebadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![built-with-love](http://forthebadge.com/images/badges/built-with-love.svg)](https://gitHub.com/TheWation/)

This repository provides a simple example of a FastAPI application with a Server-Side Template Injection (SSTI) vulnerability using Jinja2's `from_string` method.

## Prerequisites

- Python 3.7 or later
- `pip` package manager

## Installation

1. Clone this repository:

```bash
git clone https://github.com/TheWation/PythonSSTI.git
cd PythonSSTI
```

2. Install the required dependencies:
```
pip install -r requirements.txt
```

## Run the FastAPI Application
Run the FastAPI application with the following command:
```bash
uvicorn main:app --reload
```

The application will be running at `http://127.0.0.1:8000/`.

## Test SSTI Vulnerability

Access the application in your browser or through tools like curl or Postman, providing the username parameter in the query string. For example:

`http://127.0.0.1:8000/?username={{ 10 * 10 }}`

Replace "test" with the payload you want to inject for testing SSTI.

## Disclaimer
This application is intentionally vulnerable to demonstrate Server-Side Template Injection. Do not use it in a production environment.

## License

`PythonSSTI` is made with ♥  by [Wation](https://github.com/TheWation) and it's released under the `MIT` license.