# Note Search API

This is a simple API for searching notes. It's built with Django and Django Rest Framework.

## Choice of Framework/DB/3rd Party Tools

- **Django**: Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. It's free and open source.

- **Django Rest Framework**: Django Rest Framework, or DRF, is a powerful and flexible toolkit for building Web APIs. It's used for creating the API endpoints.

- **SQLite**: SQLite is a C library that provides a lightweight disk-based database. It doesn't require a separate server process and allows accessing the database using a nonstandard variant of the SQL query language. It's used as the database for this project.

## How to Run the Code

1. Clone the repository:
    ```
    git clone https://github.com/vtf05/notesearchapi.git
    ```

2. Navigate to the project directory:
    ```
    cd notesearchapi
    ```

3. Install the requirements:
    ```
    pipenv shell
    pipenv install
    ```

4. Run the migrations:
    ```
    python manage.py migrate
    ```

5. Run the server:
    ```
    python manage.py runserver
    ```



## Setup Files or Scripts

The project uses a `Pipfile`  to manage dependencies. You can install all the required packages with the command `pipenv shell and pipenv install `.

The project uses SQLite as the database, so no additional setup is required for the database.
We can also use PostgreSQL for this project because In PostgreSQL, you define a schema for your data. This can be beneficial for a note-taking application where each note will likely have a consistent structure , PostgreSQL is fully ACID-compliant (Atomicity, Consistency, Isolation, Durability), ensuring data integrity and consistency even in the event of system failures. PostgreSQL has robust built-in support for full-text search, which is a key requirement for your note-taking application.
I have used SQLite 3 to avoid any additional setup

The project uses Django's built-in server, so no additional setup is required for the server.