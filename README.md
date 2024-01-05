# Note Search API

This is a simple API for searching notes. It's built with Django and Django Rest Framework.

## Choice of Framework/DB/3rd Party Tools

- **Django**: Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. It's free and open source.

- **Django Rest Framework**: Django Rest Framework, or DRF, is a powerful and flexible toolkit for building Web APIs. It's used for creating the API endpoints.

- **SQLite**: SQLite is a C library that provides a lightweight disk-based database. It doesn't require a separate server process and allows accessing the database using a nonstandard variant of the SQL query language. It's used as the database for this project.

## How to Run the Code

1. Clone the repository:
    ```
    git clone https://github.com/yourusername/notesearchapi.git
    ```

2. Navigate to the project directory:
    ```
    cd notesearchapi
    ```

3. Install the requirements:
    ```
    pip install -r requirements.txt
    ```

4. Run the migrations:
    ```
    python manage.py migrate
    ```

5. Run the server:
    ```
    python manage.py runserver
    ```

## How to Run the Tests

To run the tests, use the following command:
