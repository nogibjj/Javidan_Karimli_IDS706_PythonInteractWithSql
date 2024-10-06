
# Python Interact with SQL - IDS706

This project demonstrates how to interact with a SQL database using Python. The repository covers fundamental database operations, including connecting to a database, performing CRUD operations, and writing SQL queries. Additionally, a CI/CD pipeline is implemented to test the database interactions automatically.


- Python script to perform SQL operations
- Screenshot or log demonstrating successful database interactions
- Public GitHub repository URL

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


