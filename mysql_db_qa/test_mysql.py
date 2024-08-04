# --------------------------
# Section: Import Libraries
# --------------------------
import os
from dotenv import load_dotenv, dotenv_values
from .mysql_schema_test import SCHEMA
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
load_dotenv()

# --------------------------
# Section: Load API
# --------------------------
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# --------------------------
# Section: Define Model
# --------------------------
llm = ChatGoogleGenerativeAI(
    google_api_key=GOOGLE_API_KEY, model="gemini-1.5-flash", temperature=0)

# --------------------------
# Section: Define Prompt
# --------------------------
prompt_template = ChatPromptTemplate.from_template("""
  Given the database schema: {schema}.
  Generate a SQL SELECT query for the following user input: {user_input}.
  
  DO NOT make any DML statements (INSERT, UPDATE, DELETE, DROP etc.) to the database.
  To start you should ALWAYS look at the tables in the database to see what you can query.
  Do NOT skip this step.

  DO NOT MAKE UP INFORMATION.
  If there are no tables or properties based on user's specifications say "The database do not have that information". 

  Do not use '*' when generating SELECT.
  Only displays minimum 3 and maximum 5 properties in the schema. The schema's primary key(s) must always be used in SELECT query.
  If there are tables need to be joined, always use 'JOIN' to join tables.
  Always use 'LIMIT' to limit the out to 50 rows.
""")

# --------------------------
# Section: Define Output Parser
# --------------------------
parser = StrOutputParser()

# --------------------------
# Section: Define Chain, the "|" operator is the ".pipe()" method
# --------------------------
chain = prompt_template | llm | parser


def create_mysql_query(question):
    response = chain.invoke({"schema": SCHEMA, "user_input": question})
    return response
