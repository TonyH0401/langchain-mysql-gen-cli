# --------------------------
# Section:
# --------------------------
from chinook_sqlite_db_qa.test_chinook import connect_chinook_db, get_db_dialect, get_db_table_names, execute_query, create_sqlite_query, extract_sqlite_query


# --------------------------
# Section:
# --------------------------

def chinook_main():
    # Connect to sqlite database
    db = connect_chinook_db()
    # Get SQL dialect (it is sqlite)
    dialect = get_db_dialect(db=db)
    print("> SQL Dialect:\n\t", dialect)
    # Get all Tables
    table_names = get_db_table_names(db=db)
    print("> SQL Tables:\n\t", table_names)
    # Execute sample query
    # sample_query = "SELECT * FROM Artist LIMIT 10;"
    # executed_query = execute_query(db=db, query=sample_query)
    # print("> Executed Query:\n\t", executed_query)
    # Test generating query
    question_1 = "How many employees are there?"
    question_2 = "List customers with last name start with the letter J"
    raw_reponse = create_sqlite_query(db=db, question=question_2)
    print("> Query:\n\t", raw_reponse)
    extracted_response = extract_sqlite_query(raw_reponse)
    test = execute_query(db=db, query=extracted_response)
    print("> Execute Generated:\n\t", test)


if __name__ == "__main__":
    try:
        print(">> Hello World Main")
        chinook_main()
    except Exception as e:
        print(f">> Exception message: {e}")
