import re
import json


def read_sql_schema_file(filepath):
    result = None
    try:
        fd = open(filepath, 'r')
        sqlFile = fd.read()
        result = sqlFile
        fd.close()
    except Exception as e:
        print(f"> Exception message: {e}")
    return result


def convert_schemas_to_json(raw_db_schemas):
    split_alled_schemas = [re.sub(r'\s+', ' ', part.replace(
        "\n", "").strip()) for part in raw_db_schemas.split(";")]
    split_schemas = [part for part in split_alled_schemas if re.search(
        r'create table', part, re.IGNORECASE)]

    # print(split_schemas[0])
    # for schema in split_schemas:
    #     print(">", schema)
    # ====================
    # Use regex to find column definitions
    sql_statement = split_schemas[1]
    # Extract table name
    table_name_match = re.search(r'CREATE TABLE (\w+)', sql_statement, re.IGNORECASE)
    table_name = table_name_match.group(1) if table_name_match else 'unknown_table'

    # Extract column definitions
    columns_section = re.search(r'\((.*)\)', sql_statement, re.DOTALL).group(1)
    columns = re.findall(r'(\w+)\s+([\w\s\(\),\'"]+?)(?=,\s*\w+\s+|$)', columns_section)

    # Convert to JSON format
    columns_dict = {col[0]: col[1].strip() for col in columns if 'PRIMARY KEY' not in col[0]}

    # Prepare the final JSON object
    json_object = {table_name: columns_dict}

    # Print JSON
    json_output = json.dumps(json_object, indent=4)
    print(json_output)

    return 0
