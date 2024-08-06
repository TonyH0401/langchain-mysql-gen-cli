# --------------------------
# Section: Import Libraries
# --------------------------
import os
# from dotenv import load_dotenv, dotenv_values
# from .mysql_schema_test import SCHEMA
# from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser
# load_dotenv()

# # --------------------------
# # Section: Load API
# # --------------------------
# GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# # --------------------------
# # Section: Define Model
# # --------------------------
# llm = ChatGoogleGenerativeAI(
#     google_api_key=GOOGLE_API_KEY, model="gemini-1.5-flash", temperature=0)

# # --------------------------
# # Section: Define Prompt
# # --------------------------
# template = """
#   You are a MySQL expert.
#   Your goal is to create syntactically correct MySQL query to run, then look at the results of the query and return the answer to the input question.

#   Given the MySQL database schemas: {schema}.
#   Generate MySQL "SELECT" query based on the following user input: {user_input}.

#   You strictly follow these goals and rules below. No yapping and do not make up information. DO NOT skip this step.
#   DO:
#   - ONLY displays minimum 3 and maximum 5 properties in the schema.
#   - The schema's primary key(s) must ALWAYS be used in "SELECT" query.
#   - ONLY use relevant tables to the user specifications or columns that are needed to answer user question.
#   - ALWAYS look at the tables in the database to see what you can query and use ONLY the column names you can see in the tables below.
#   - Pay attention to which column is in which table.
#   - Order the results to return the most informative data in the database.
#   - Use "JOIN" when joining multiple tables.
#   - Use 'LIMIT' to limit the output to 10 rows.
#   DO NOT:
#   - Use "*" when generating "SELECT" query.
#   - Make any DML statements (INSERT, UPDATE, DELETE, DROP etc.) to the database.
#   - Use "DISTINCT".
#   - Query for columns that do not exist.
# """
# prompt_template = ChatPromptTemplate.from_template(template=template)

# # --------------------------
# # Section: Define Output Parser
# # --------------------------
# parser = StrOutputParser()

# # --------------------------
# # Section: Define Chain, the "|" operator is the ".pipe()" method
# # --------------------------
# chain = prompt_template | llm | parser


# def create_mysql_query(question):
#     response = chain.invoke({"schema": SCHEMA, "user_input": question})
#     return response

from .schema_utils import read_sql_schema_file, convert_schemas_to_json, convert_json_to_markdown


def starting():
    filepath_1 = 'ZooDatabase.sql'
    filepath_2 = './mysql_db_qa_2/mysql_schemas/employee.sql'
    check_file = os.path.isfile(filepath_2)
    if check_file is False:
        print("> File path is incorrect! File does not exist!")
        return
    mysql_schemas = read_sql_schema_file(filepath=filepath_2)
    if mysql_schemas is None:
        print("> There are no data in SQL file!")
        return
    json_schema = convert_schemas_to_json(raw_db_schemas=mysql_schemas)
    json_markdown_schema = convert_json_to_markdown(json=json_schema)
    print(json_markdown_schema)
