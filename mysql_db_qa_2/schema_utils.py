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


""" 
- Original method: Code the 

There is another way which is using LLM + output_parser_structure, 
the llm will read the schemas and output will return the structure 

- https://python.langchain.com/v0.2/docs/how_to/structured_output/ (gotta read it all, I stopped at Few-shot)
- https://python.langchain.com/v0.2/docs/how_to/#output-parsers.
-> we have to pre-defined the properties we want to take out

Another method is to ask the LLM to extract it basically let it do all the work but high chance of hallucination.


"""


def convert_schemas_to_json(raw_db_schemas):
    split_alled_schemas = [re.sub(r'\s+', ' ', part.replace(
        "\n", "").strip()) for part in raw_db_schemas.split(";")]
    split_schemas = [part for part in split_alled_schemas if re.search(
        r'create table', part, re.IGNORECASE)]
    json_schemas_str = ""
    # sql_statement = split_schemas[3]
    for schema in split_schemas:
        # Use regex to find column definitions
        # Extract table name
        table_name_match = re.search(
            r'CREATE TABLE (\w+)', schema, re.IGNORECASE)
        table_name = table_name_match.group(
            1) if table_name_match else 'unknown_table'
        # Extract column definitions
        columns_section = re.search(r'\((.*)\)', schema, re.DOTALL).group(1)
        columns = re.findall(
            r'(\w+)\s+([\w\s\(\),\'"]+?)(?=,\s*\w+\s+|$)', columns_section)
        # Convert to JSON format
        columns_dict = {col[0]: col[1].strip()
                        for col in columns if 'PRIMARY KEY' not in col[0]}
        # Prepare the final JSON object
        json_object = {table_name: columns_dict}
        # Print JSON
        json_output = json.dumps(json_object, indent=4)
        json_schemas_str = json_schemas_str + json_output + ","
    return json_schemas_str


def convert_json_to_markdown(json):
    return f"""```sql\n {json} \n```"""
