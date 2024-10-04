try:
    from lib import SQL, ETLHelper
except Exception:
    from src.lib import SQL, ETLHelper

CSV_FILE_PATH = "data/chess_transfers.csv"
TABLE_NAME = "ChessTransfer"
TABLE_NAME_AFTER_TRANSFORMATION = "ChessTransfersFormatted"


def perform_elt():
    status = None
    # Connnect to database
    connection = ETLHelper.connect_db(
        type_of_database="sqllite", database_conn="data/sqlitedb"
    )

    # Load CSV file to database
    status = ETLHelper.load_csv_to_db(
        csv_file_path=CSV_FILE_PATH, conn=connection, table_name=TABLE_NAME
    )
    # Drop the destination table before creating it
    status = ETLHelper.execute_query(
        connection, query=f"DROP TABLE IF EXISTS {TABLE_NAME_AFTER_TRANSFORMATION}"
    )

    # Create a transformed table
    status = ETLHelper.execute_query(
        connection,
        query=SQL.read_sql(
            "src/sql/transform.sql", table_name=TABLE_NAME_AFTER_TRANSFORMATION
        ),
    )

    return bool(status)


def crud_operations():

    status = None
    connection = ETLHelper.connect_db(
        type_of_database="sqllite", database_conn="data/sqlitedb"
    )

    # Read operation
    random_id_data = ETLHelper.read_by_id(
        connection, TABLE_NAME_AFTER_TRANSFORMATION, id=66200458
    )
    print(f"Retrieved result - {random_id_data}")
    # Create (Insert) operation
    inserted_row_id = ETLHelper.insert(
        connection, TABLE_NAME_AFTER_TRANSFORMATION, {"ID": "1"}
    )
    inserted_row_id2 = ETLHelper.insert(
        connection, TABLE_NAME_AFTER_TRANSFORMATION, {"ID": "2"}
    )

    print(f"Inserted Row Ids:{inserted_row_id}, {inserted_row_id2}")

    # Update operation
    status = ETLHelper.update(
        connection,
        table_name=TABLE_NAME_AFTER_TRANSFORMATION,
        ids=[1],
        update_values={"Federation": "AZE", "Form_Fed": "USA"},
    )
    updated_id_data = ETLHelper.read_by_id(
        connection, TABLE_NAME_AFTER_TRANSFORMATION, id=1
    )
    print(updated_id_data)

    # Delete operation

    status = ETLHelper.delete(
        connection, table_name=TABLE_NAME_AFTER_TRANSFORMATION, ids=[2]
    )

    return bool(status)


def perform_analytics():
    connection = ETLHelper.connect_db(
        type_of_database="sqllite", database_conn="data/sqlitedb"
    )

    cursor = connection.cursor()

    cursor.execute(SQL.read_sql(query="src/sql/analytical_query.sql"))

    result = cursor.fetchall()

    print(result)
    print("-" * 60)
    cursor.execute(SQL.read_sql(query="src/sql/analytical_query2.sql"))

    result2 = cursor.fetchall()

    print(result2)

    cursor.close()

    return True


if __name__ == "__main__":
    print(perform_elt())
    print(crud_operations())
    perform_analytics()
