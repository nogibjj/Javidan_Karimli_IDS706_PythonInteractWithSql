[![CI Pipeline](https://github.com/nogibjj/Javidan_Karimli_IDS706_PythonInteractWithSql/actions/workflows/main.yaml/badge.svg)](https://github.com/nogibjj/Javidan_Karimli_IDS706_PythonInteractWithSql/actions/workflows/main.yaml)

# Python Interact with SQL - IDS706

This project demonstrates how to interact with a SQL database using Python. The repository covers fundamental database operations, including connecting to a database, performing CRUD operations, and writing SQL queries. Additionally, a CI/CD pipeline is implemented to test the database interactions automatically.


## Project Structure
- `src/lib.py`: Python script that contain all  needed functions
- `src/main.py`: Python script based on the functions of the lib and perform analtyical operations
- `test/test_main.py`, `test/test_lib.py` : Contains tests to validate the operations.
- `.github/workflows/`: CI/CD pipeline configuration for automated testing.

## Requirements
- Python 3.x
- SQLite3 or other SQL database
- `sqlite3` library (comes with Python)
- `pytest` for testing
- `black` for formatting
- `ruff` for testing 
- GitHub Actions for CI/CD pipeline

## CRUD Operations

CRUD operations refer to the basic functions of persistent storage. In this project, the following operations are performed:

- **Create:** Insert new data into the database
- **Read:** Query data from the database
- **Update:** Modify existing data
- **Delete:** Remove data from the database

For more details on CRUD operations, visit the [Wikipedia page](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete).

## CI/CD Pipeline

A CI/CD pipeline has been set up to automatically run the tests for CRUD operations. The tests will verify that each operation works as expected and the SQLite `.db` file can be loaded and manipulated within the pipeline.

## Setup

1. Clone this repository:
   ```
   git clone https://github.com/nogibjj/Javidan_Karimli_IDS706_PythonInteractWithSql.git
   cd Javidan_Karimli_IDS706_PythonInteractWithSql
   ```

2. Install the required dependencies:
   ```
   make install
   ```

3. Format the code:
   ```
   make format
   ```

4. Lint the code:
   ```
   make lint
   ```

5. To test the scripts:
   ```
   make test_file
   ```

6. Run the Python script to connect to the SQL database and perform the operations:
   ```
   python src/main.py
   ```


## Database Operation Snaps

Create Table Operation
![Create Table Operation](https://github.com/nogibjj/Javidan_Karimli_IDS706_PythonInteractWithSql/blob/dc441a505960c3923d83f8f7a8f9525c6b602157/img/CreateTablequery.png)

Insert Operation
![Insert Operation](https://github.com/nogibjj/Javidan_Karimli_IDS706_PythonInteractWithSql/blob/dc441a505960c3923d83f8f7a8f9525c6b602157/img/InsertOperation.png)

Read Operation
![Read Operation](https://github.com/nogibjj/Javidan_Karimli_IDS706_PythonInteractWithSql/blob/dc441a505960c3923d83f8f7a8f9525c6b602157/img/ReadOperation.png)

Update Operation
![Update Operation](https://github.com/nogibjj/Javidan_Karimli_IDS706_PythonInteractWithSql/blob/dc441a505960c3923d83f8f7a8f9525c6b602157/img/UpdateOperation.png)

Delete Operation
![Delete Operation](https://github.com/nogibjj/Javidan_Karimli_IDS706_PythonInteractWithSql/blob/dc441a505960c3923d83f8f7a8f9525c6b602157/img/DeleteOperation.png)

First analtyical query performed
![First analtyical query performed](https://github.com/nogibjj/Javidan_Karimli_IDS706_PythonInteractWithSql/blob/dc441a505960c3923d83f8f7a8f9525c6b602157/img/AnalyticQuery1.png)

Second analtyical query performed
![Second analtyical query performed](https://github.com/nogibjj/Javidan_Karimli_IDS706_PythonInteractWithSql/blob/dc441a505960c3923d83f8f7a8f9525c6b602157/img/AnaylticQuery2.png)

