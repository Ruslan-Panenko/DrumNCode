# Project Documentation

## Running with Docker

### Creating a `.env` File

To configure the environment with Docker, you can create a `.env` file in the root directory of the project. Example content:

env.example
```
SECRET_KEY=secret_key

DEBUG=True

POSTGRES_DB=postgres_db
POSTGRES_USER=postgres_user
POSTGRES_PASSWORD=postgres_password
```


### Running the Project with Docker Compose

1. Ensure that Docker and Docker Compose are installed. You can download and install them from the [official Docker website](https://www.docker.com/products/docker-desktop).

2. Navigate to the root directory of the project where the `docker-compose.yml` file is located.

3. Start the containers using the following command:
   ```
   docker-compose up --build
    ```
This command will build and start all the required containers (e.g., Django and PostgreSQL) based on the configuration in docker-compose.yml.

4. To run the containers in the background, use the -d flag:

```
docker-compose up -d --build
```

# Swagger Documentation

The project comes with a built-in Swagger documentation.

```
http://0.0.0.0:8000/swagger/
```

### Creating a Superuser
After starting the containers, run the following command to create a superuser:

```
docker-compose exec web python manage.py createsuperuser
```

Follow the on-screen instructions to enter the username and password.


### Running Tests
To run tests inside the container, use the command:
```
docker-compose exec web python manage.py test
```

# Endpoints

### List Books
- URL: /books/
- Method: GET
- Description: Retrieve a list of all books.
- Response:
200 OK: Successful request. Returns a list of books in JSON format.


### Create Book
- URL: /books/
- Method: POST
- Description: Create a new book.
- Request Body:
```
{
    "title": "Book Title",
    "author": "Author Name",
    "published_date": "2023-01-01",
    "isbn": "1234567890123",
    "pages": 200,
    "cover": "http://example.com/cover.jpg",
    "language": "English"
}
```
- Response:
201 Created: Successful request. Returns the newly created book in JSON format.

### Book Details
- URL: /books/{id}/
- Method: GET
- Description: Retrieve a specific book by its ID.
- Response:
200 OK: Successful request. Returns the book in JSON format.

### Update Book
- URL: /books/{id}/
- Method: PUT
- Description: Update a specific book by its ID.
- Request Body:
```
{
    "title": "Updated Book Title",
    "author": "Updated Author Name",
    "published_date": "2023-01-01",
    "isbn": "1234567890123",
    "pages": 200,
    "cover": "http://example.com/cover.jpg",
    "language": "English"
}
```
- Response:
200 OK: Successful request. Returns the updated book in JSON format.

### Delete Book
- URL: /books/{id}/
- Method: DELETE
- Description: Delete a specific book by its ID.
- Response:
204 No Content: Successful request. No content is returned.
