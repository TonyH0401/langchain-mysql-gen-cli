# --------------------------
# Section: Import Library
# --------------------------
from langchain.chains import create_sql_query_chain
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.utilities import SQLDatabase
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


def connect_chinook_db():
    db_file_path = "chinook_sqlite_db_qa/Chinook.db"
    db_path = "sqlite:///" + db_file_path
    db = SQLDatabase.from_uri(db_path)
    return db


def get_db_dialect(db):
    return db.dialect


def get_db_table_names(db):
    return db.get_usable_table_names()


def execute_query(db, query):
    return db.run(query)


def create_sqlite_query(db, question):
    chain = create_sql_query_chain(llm, db)
    reponse = chain.invoke({"question": question})
    return reponse

def create_sqlite_query_custom_prompt(db, question):
    return 0


def extract_sqlite_query(input):
    extracted = input.strip("```sqlite").replace("\n","")
    return extracted
