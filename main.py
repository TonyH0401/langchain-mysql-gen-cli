# --------------------------
# Section:
# --------------------------
from chinook_sqlite_db_qa.test_chinook import create_sqlite_query, create_sqlite_query_2
from mysql_db_qa.test_mysql import create_mysql_query


def chinook_main():
    # List of questions
    question_1 = "How many employees are there?"
    question_2 = "List customers with last name start with the letter J"
    question_3 = "List most popular album"
    # Test 1
    result_1 = create_sqlite_query(question=question_1)
    print(result_1)
    # Test 2
    # result_2 = create_sqlite_query_2(question=question_2)
    # print(result_2)


def mysql_main():
    # List of question
    question_1 = "Listing popular Ticket types that customers bought this year"
    # Test 1
    result_1 = create_mysql_query(question=question_1)
    print(result_1)


if __name__ == "__main__":
    try:
        print(">> Hello World Main")
        # chinook_main()
        mysql_main()
    except Exception as e:
        print(f">> Exception message: {e}")
