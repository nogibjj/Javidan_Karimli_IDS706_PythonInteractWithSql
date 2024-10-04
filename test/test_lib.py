import pytest
import sqlite3
from src.lib import ETLHelper, extract_csv
import os


@pytest.fixture
def connection():
    """Set up a fresh in-memory SQLite database before each test."""
    conn = sqlite3.connect(":memory:")
    yield conn
    conn.close()


@pytest.fixture
def setup_table(connection):
    """Create a sample table for testing."""
    cursor = connection.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS test_table (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER
        );
    """
    )
    connection.commit()


def test_insert(connection, setup_table):
    """Test the insert function."""
    values = {"name": "'Alice'", "age": "30"}

    inserted_id = ETLHelper.insert(connection, "test_table", values)
    assert inserted_id is not None

    # Verify the row has been inserted
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM test_table WHERE id = ?", (inserted_id,))
    row = cursor.fetchone()

    assert row is not None
    assert row[1] == "Alice"
    assert row[2] == 30


def test_read_by_id(connection, setup_table):
    """Test the read_by_id function."""
    # Insert test data
    cursor = connection.cursor()
    cursor.execute("INSERT INTO test_table (name, age) VALUES ('Bob', 25)")
    connection.commit()
    inserted_id = cursor.lastrowid

    result = ETLHelper.read_by_id(connection, "test_table", inserted_id)
    assert result["data"][1] == "Bob"
    assert result["data"][2] == 25


def test_read_all(connection, setup_table):
    """Test the read_all function."""
    # Insert test data
    cursor = connection.cursor()
    cursor.execute("INSERT INTO test_table (name, age) VALUES ('Charlie', 40)")
    cursor.execute("INSERT INTO test_table (name, age) VALUES ('Diana', 35)")
    connection.commit()

    result = ETLHelper.read_all(connection, "test_table")

    assert len(result["data"]) == 2
    assert result["data"][0][1] == "Charlie"
    assert result["data"][1][1] == "Diana"


def test_update(connection, setup_table):
    """Test the update function."""
    # Insert test data
    cursor = connection.cursor()
    cursor.execute("INSERT INTO test_table (name, age) VALUES ('Edward', 45)")
    connection.commit()
    inserted_id = cursor.lastrowid

    # Update the age of the inserted row
    update_values = {"age": "50"}
    ETLHelper.update(connection, "test_table", [inserted_id], update_values)

    # Verify the update
    result = ETLHelper.read_by_id(connection, "test_table", inserted_id)
    assert result["data"][2] == 50


def test_delete(connection, setup_table):
    """Test the delete function."""
    # Insert test data
    cursor = connection.cursor()
    cursor.execute("INSERT INTO test_table (name, age) VALUES ('Frank', 55)")
    connection.commit()
    inserted_id = cursor.lastrowid

    # Delete the row
    ETLHelper.delete(connection, "test_table", [inserted_id])

    # Verify the deletion
    result = ETLHelper.read_by_id(connection, "test_table", inserted_id)
    assert result["data"] is None


def test_load_csv_to_db(connection):
    """Test the load_csv_to_db function."""
    extract_csv(file_path="test.csv")

    # Load the CSV into the database
    success = ETLHelper.load_csv_to_db("data/test.csv", connection, "test_table")

    assert success

    # Verify the data has been loaded
    result = ETLHelper.read_all(connection, "test_table")

    assert len(result["data"]) == 932

    os.remove("data/test.csv")
