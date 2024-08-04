def read_sql_schema_file(filepath):
    result = None
    try:
        fd = open(filepath, 'r')
        sqlFile = fd.read()
        result = sqlFile
        fd.close()
    except Exception as e:
        print(f">> Exception message: {e}")
    return result

def convert_schema_to_json(schema):
    
    return 0