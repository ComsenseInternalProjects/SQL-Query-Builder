import os
import re
import logging
from openai import OpenAI

from prompt import combine_prompts

logging.basicConfig(level=logging.INFO)
openai_api_key = os.environ['OPENAI_API_KEY']



def get_sql(nlp_text, json_input):
    logging.info("Query builder started.")
    try:
        client = OpenAI(api_key=openai_api_key)
        response = client.completions.create(
            model="gpt-3.5-turbo-instruct-0914",
            prompt=combine_prompts(json_input, nlp_text),
            temperature=0,
            max_tokens=2000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=["#", ";"]
        )

        if hasattr(response, 'choices') and response.choices:
            first_choice_text = response.choices[0].text.strip()
            if first_choice_text.startswith(" "):
                first_choice_text = "SELECT" + first_choice_text
        else:
            first_choice_text = "No choices found in the response."

        return first_choice_text

    except Exception as e:
        logging.error(f"OpenAI API request failed: {e}")
        return "ERROR"

def post_process_query(json_input, generated_query):
    unwanted_keywords = ["DELETE", "REMOVE", "DROP", "UPDATE", "TRUNCATE", "INSERT", "ERROR"]
    for keyword in unwanted_keywords:
        if keyword in generated_query:
            dataset_name = json_input.get("datasetName")
            return False, f"SELECT * FROM {dataset_name}"

    if 'TIMESTAMP' not in generated_query:
        date_formats = r"('\d{2}-\d{2}-\d{4}'|'\d{1}-\d{1}-\d{4}'|'\d{4}-\d{2}-\d{2}'|'\d{4}/\d{2}/\d{2}'|'\d{1}/\d{1}/\d{4}'|'\d{2}/\d{2}/\d{4}')"
        generated_query = re.sub(date_formats, r'TIMESTAMP \1', generated_query)

    # Validate field names
    fields = [field["name"] for field in json_input.get("fields", [])]
    sql_keywords = {
    "SELECT", "FROM", "WHERE", "AND", "OR", "BETWEEN", "LIKE", "IN", "JOIN", "ON", "AS", "NOT", "NULL", "GROUP", "BY", "ORDER", "LIMIT", "DISTINCT", "UNION", "ALL", "EXCEPT", "INTERSECT", "HAVING", "COUNT", "SUM", "AVG", "MIN", "MAX", "TIMESTAMP", "CREATE", "ALTER", "DROP", "INSERT", "UPDATE", "DELETE", "TRUNCATE", "GROUP_CONCAT", "CASE", "EXISTS", "UNIQUE", "PRIMARY KEY", "FOREIGN KEY", "CASCADE", "INNER JOIN", "LEFT JOIN", "RIGHT JOIN", "FULL JOIN", "HAVING",
    "DESC"}

    
    query_words = re.findall(r'\b\w+\b', generated_query)
    invalid_fields = [word for word in query_words if word.isidentifier() and word.upper() not in sql_keywords and word not in fields and word != json_input.get("datasetName")]

    if invalid_fields:
        return False, f"Column name(s) not present: {', '.join(set(invalid_fields))}"

    generated_query = ' '.join(generated_query.split())
    if not generated_query.startswith("SELECT"):
        generated_query = f"SELECT {generated_query}"
        
    logging.info("Post-processing query executed.")
    return True, generated_query

def main(query_prompt, json_input):
    try:
        generated_query = get_sql(query_prompt, json_input)
        success_flag, processed_query = post_process_query(json_input, generated_query)
        
        if success_flag:
            return {"status": 200, "data": processed_query}
        else:
            return {"status": 400, "data": processed_query}
    
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        return {"status": 400, "data": "An unexpected error occurred"}



if __name__ == "__main__":
    json_input = {
  "datasetName": "ecom",
  "fields": [
                {
                    "name": "TransactionNo",
                    "description": "Transaction number",
                    "dataType": "STRING"
                },
                {
                    "name": "ReceiptNo",
                    "description": "Unique Bill number for each transection",
                    "dataType": "STRING"
                },
                {
                    "name": "CustomerId",
                    "description": "Unique identifier for customer",
                    "dataType": "STRING"
                },
                {
                    "name": "NetAmount",
                    "description": "Net Invoice Amount",
                    "dataType": "DOUBLE"
                },
                {
                    "name": "GrossAmount",
                    "description": "Invoice gross amount",
                    "dataType": "DOUBLE"
                },
                {
                    "name": "Payment",
                    "description": "Invoice gross amount",
                    "dataType": "DOUBLE"
                },
                {
                    "name": "TotalDiscount",
                    "description": "Discount given in a bill",
                    "dataType": "DOUBLE"
                },
                {
                    "name": "ItemId",
                    "description": "Product id purchased",
                    "dataType": "STRING"
                },
                {
                    "name": "NoOfItems",
                    "description": "Qty sold",
                    "dataType": "DOUBLE"
                },
                {
                    "name": "IsReturnSale",
                    "description": "Sales or Return Sale Flag",
                    "dataType": "INTEGER"
                },
                {
                    "name": "StartingPointBalance",
                    "description": "Loyalty point balance at the start of the transaction",
                    "dataType": "DOUBLE"
                },
                {
                    "name": "MobileNumber",
                    "description": "Customer Phone number",
                    "dataType": "STRING"
                },
                {
                    "name": "LoyaltyAccountId",
                    "description": "Loyalty Account ID of a customer",
                    "dataType": "STRING"
                },
                {
                    "name": "OrderDate",
                    "description": "order date format DD-MM-YYYY",
                    "dataType": "DATE"
                },
                {
                    "name": "Email",
                    "description": "email",
                    "dataType": "STRING"
                },
                {
                    "name": "AddressId",
                    "description": "Delivery Address details of the customer",
                    "dataType": "STRING"
                },
                {
                    "name": "State",
                    "description": "state",
                    "dataType": "STRING"
                },
                {
                    "name": "ReturnQuantity",
                    "description": "ct return quantity",
                    "dataType": "DOUBLE"
                },
                {
                    "name": "ItemPrice",
                    "description": "Item Price",
                    "dataType": "DOUBLE"
                },
                {
                    "name": "OrderStatus",
                    "description": "ct order status",
                    "dataType": "STRING"
                },
                {
                    "name": "LoyaltyMobileNo",
                    "description": "Mobile number associated with loyalty",
                    "dataType": "STRING"
                },
                {
                    "name": "LoyaltyId",
                    "description": "Loyalty ID of the customer",
                    "dataType": "STRING"
                }
            ]

}
    try:
        print(main("Find transaction data",json_input))
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
