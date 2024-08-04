# --------------------------
# Section: Import Library
# --------------------------
from langchain_core.prompts import PromptTemplate
from langchain_community.utilities import SQLDatabase
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import create_sql_query_chain
import os
from dotenv import load_dotenv, dotenv_values
load_dotenv()

# --------------------------
# Section: Import Constant and API
# --------------------------
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# --------------------------
# Section: Define Model
# --------------------------
llm = ChatGoogleGenerativeAI(
    google_api_key=GOOGLE_API_KEY, model="gemini-1.5-flash", temperature=0)


def create_sqlite_query(question):
    # Connectto database
    db_file_path = "chinook_sqlite_db_qa/Chinook.db"
    db_path = "sqlite:///" + db_file_path
    db = SQLDatabase.from_uri(db_path)
    # Check for db's dialect
    # print(db.dialect)
    # Get available table names
    print(db.get_usable_table_names())
    # Create sql query chain
    chain = create_sql_query_chain(llm, db)
    # We can inspect the full prompt of create_sql_query_chain() like so
    # print(chain.get_prompts()[0].pretty_print())
    # Invoke for a response
    reponse = chain.invoke({"question": question})
    # Reformat the response
    extracted = reponse.strip("```sqlite").replace("\n", "")
    # Execute the reformated query, technically you will use an sql execution tool but because of the format you can't
    executed = db.run(extracted)
    # Return the data
    return extracted, executed


def create_sqlite_query_2(question):
    # Connectto database
    db_file_path = "chinook_sqlite_db_qa/Chinook.db"
    db_path = "sqlite:///" + db_file_path
    db = SQLDatabase.from_uri(db_path)
    # Get available table names
    print(db.get_usable_table_names())
    # Create a template, there is also a template over in the docs
    template = """
    You are an SQLite expert.
    
    Your goal is to create syntactically correct SQLite query to run, then look at the results of the query and return the answer to the input question.

    You strictly follow these goals and rules below. No yapping.
    DO:
    - Query only the columns that are needed to answer the question.
    - Wrap each column name in double quotes (") to denote them as delimited identifiers.
    - Query for at most 5 results using the LIMIT clause as per SQLite (unless the user specifies in the question a specific number of examples to obtain). 
    - Order the results to return the most informative data in the database.
    - Pay attention to use only the column names you can see in the tables below.
    - Pay attention to which column is in which table.
    - Pay attention to use date('now') function to get the current date, if the question involves "today".
    - Use "JOIN" when joining multiple tables.
    DO NOT:
    - Query for all columns from a table. 
    - Use "SELECT *".
    - Use "DISTINCT".
    - Query for columns that do not exist.

    Use the following format:
    Question: "Question here"
    SQLQuery: "SQL Query to run"
    SQLResult: "Result of the SQLQuery"
    Answer: "Final answer here"

    Only use the following tables: {table_info}
    Question: {input}
    The number of results per select statement: {top_k}
    """
    # Create a prompt
    prompt = PromptTemplate.from_template(template=template)
    # Create a chain
    chain = create_sql_query_chain(llm, db, prompt)
    # Custom prompt needs "table_info", "input" and "top_k"; the "input" is called the "question", "top_k" is the LIMIT
    reponse = chain.invoke(
        {"question": question, "table_info": db.get_context()["table_info"], "top_k": 5})
    # Reformat the response, has tendency to be wrong
    extracted = reponse.strip("```sqlite").replace("\n", "")
    # Execute the reformated query
    executed = db.run(extracted)
    # Return the data
    return extracted, executed


# def extract_sqlite_query(input):
#     extracted = input.strip("```sqlite").replace("\n", "")
#     return extracted
