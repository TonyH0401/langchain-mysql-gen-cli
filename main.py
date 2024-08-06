# --------------------------
# Section:
# --------------------------
from chinook_sqlite_db_qa.test_chinook import create_sqlite_query, create_sqlite_query_2
from mysql_db_qa.test_mysql import create_mysql_query
from mysql_db_qa_2.test_mysql_2 import load_schemas_from_file, convert_schemas_to_json_markdown, create_mysql_query_2, create_mysql_query_2_2


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
    question_2 = "How many event are there?"
    # Test 1
    result_1 = create_mysql_query(question=question_2)
    print(result_1)


def mysql_main_2():
    # List of question
    question_1 = "List the top 10 employees with the highest salaries"
    question_2 = "How many employees are there?"
    # Load the schemas from file
    raw_schemas = load_schemas_from_file()
    # Test 1
    # json_markdown_schemas = convert_schemas_to_json_markdown(
    #     mysql_schemas=raw_schemas)
    # result_1 = create_mysql_query_2(
    #     schema=json_markdown_schemas, question=question_1)
    # print(result_1)
    # Test 2
    result_2 = create_mysql_query_2_2(raw_schemas, question_2)
    print(result_2)


if __name__ == "__main__":
    try:
        print(">> Hello World Main")
        # chinook_main()
        # mysql_main()
        mysql_main_2()
    except Exception as e:
        print(f">> Exception message: {e}")
