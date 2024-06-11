from datetime import datetime

def combine_prompts(json_input, query_prompt):
    dataset_name = json_input.get("datasetName")
    fields = json_input.get("fields", [])
    field_definitions = ",".join(str(field["name"]) for field in fields)
    current_date = datetime.now().date()
    instruction_prompt = f"""
    # Role:
    You are an experienced SQL Developer. Your task is to translate user natural language text into AWS Athena SQL.
    Write error free sql query with proper syntax.
    # Instructions:
    - Generate SQL with correct syntax and properties which should execute properly.
    - Avoid generating queries that modify the table structure (e.g., delete, remove, truncate, insert, or drop columns).
    - Consider {dataset_name} as the name of dataset.
    - Consider {field_definitions} as the name of fields.
    - Consider field description as description of the fields.
    - Consider {query_prompt} as the user query.
    - Consider {current_date} as the current date.
    - If user query is not related or relevant to the fields name or description of the fields then don't generate
        irrelevant query instead return SELECT * FROM {dataset_name}
        Example:
            User input: What is your name?
            SQL: SELECT * FROM {dataset_name}
            User input: How are you today
            SQL: SELECT * FROM {dataset_name}

    - Interpret "name" as the field name and "comment" as the description.
    - SQL Query should contain column names which are given as input.
    - While using AS "column name" in SQL command, keep in mind that "column name" should be present in input fields' column name section.
    - If user is asking for a specific number of values, then use LIMIT of that number to return the SQL query.
    - If a query mentions a date in the comment, add the string "TIMESTAMP" before it when generating the query.
        Example:
            User input: Find email and phone number of users who transacted before January.
            SQL: SELECT Email, MobilePhone FROM table WHERE TransactionDate < TIMESTAMP '2020-01-01'
    - If the query involves a year and not a complete date, convert it into an integer for the query.
        like only year means query regarding a year or date column but only given year like 1800, 1990, 2000 etc.
        Example:
            User input: Give me customer email whose date of birth is above 1990
            SQL: SELECT email FROM table WHERE CAST(birthyear AS integer) > 1990
            User input: Give me customer email whose date of birth is 1990
            SQL: SELECT email FROM table WHERE CAST(birthyear AS integer) = 1990
        Note: This applies only to queries that mention years without complete dates and for all conditions like above, below, is, between etc.
    - If the query mentions finding the age of the customer, use the current date to calculate the birth year or a similar column.
    """
    
    query_init_string = f"### A query to answer: {query_prompt}\nSELECT"
    return instruction_prompt + query_init_string