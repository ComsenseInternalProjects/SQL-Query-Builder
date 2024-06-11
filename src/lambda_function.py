from src.text2sql import main

def lambda_handler(event, context):
    try:
        # Get User Input
        query_prompt = event["userInput"]
        dataset_name = event["datasetName"]
        fields = event["fields"]

        json_input = {"datasetName": dataset_name, "fields": fields}

        output = main(query_prompt, json_input)
        return output

    except Exception as e:
        response = {
            "status": 400,
            "data": f"An unexpected error occurred: {e}"
        }
        return response


if __name__ == "__main__":
    test_user_ip = {
        "userInput":"give me total transaction data",
        "datasetName": "svoc",
        "fields":[
    {
        "name": "ID",
        "dataType": "string",
        "comment": "Customer Profile ID"
    },
    {
        "name": "CustomerId",
        "dataType": "string",
        "comment": "Customer External ID"
    },
    {
        "name": "Email",
        "dataType": "string",
        "comment": "Customer Email"
    },
    {
        "name": "CourtesyTitle",
        "dataType": "string",
        "comment": "Courtesy Title eg. Doctor"
    },
    {
        "name": "FirstName",
        "dataType": "string",
        "comment": "Customer First name"
    },
    {
        "name": "FullName",
        "dataType": "string",
        "comment": "Customer Full name"
    },
    {
        "name": "LastName",
        "dataType": "string",
        "comment": "Customer Last name"
    },
    {
        "name": "MiddleName",
        "dataType": "string",
        "comment": "Customer Middle name"
    },
    {
        "name": "Suffix",
        "dataType": "string",
        "comment": "Customer Suffix"
    },
    {
        "name": "MobilePhone",
        "dataType": "string",
        "comment": "Customer MobilePhone"
    },
    {
        "name": "BirthDate",
        "dataType": "string",
        "comment": "Customer BirthDate"
    },
    {
        "name": "Gender",
        "dataType": "string",
        "comment": "Customer Gender"
    },
    {
        "name": "MaritalStatus",
        "dataType": "string",
        "comment": "Customer MaritalStatus"
    },
    {
        "name": "SecondaryEmail",
        "dataType": "string",
        "comment": "Customer SecondaryEmail"
    },
    {
        "name": "BirthDayMonth",
        "dataType": "string",
        "comment": "Birthday Month"
    },
    {
        "name": "BirthYear",
        "dataType": "string",
        "comment": "Birthday Year"
    },
    {
        "name": "Nationality",
        "dataType": "string",
        "comment": "Nationality"
    },
    {
        "name": "Type",
        "dataType": "string",
        "comment": "Type"
    },
    {
        "name": "BirthCountry",
        "dataType": "string",
        "comment": "Birth Country"
    },
    {
        "name": "BirthTown",
        "dataType": "string",
        "comment": "Birth Town"
    },
    {
        "name": "AdditionalNationality",
        "dataType": "string",
        "comment": "Additional Nationality"
    },
    {
        "name": "City",
        "dataType": "string",
        "comment": "Customer City"
    },
    {
        "name": "Country",
        "dataType": "string",
        "comment": "Customer Country"
    },
    {
        "name": "CountryCode",
        "dataType": "string",
        "comment": "Customer Country Code"
    },
    {
        "name": "PostalCode",
        "dataType": "string",
        "comment": "Address Postal Code"
    },
    {
        "name": "Region",
        "dataType": "string",
        "comment": "Region"
    },
    {
        "name": "State",
        "dataType": "string",
        "comment": "Address State"
    },
    {
        "name": "StateProvince",
        "dataType": "string",
        "comment": "StateProvince"
    },
    {
        "name": "Street1",
        "dataType": "string",
        "comment": "Address Street Line 1"
    },
    {
        "name": "Street2",
        "dataType": "string",
        "comment": "Address Street Line 2"
    },
    {
        "name": "TotalRetailTransaction",
        "dataType": "double",
        "comment": "Total Retail Transactions"
    },
    {
        "name": "TotalRetailTransactionAmount",
        "dataType": "double",
        "comment": "Total Retail Transaction Amount"
    },
    {
        "name": "TotalRetailDiscount",
        "dataType": "double",
        "comment": "Total Retail Discount Amount"
    },
    {
        "name": "RetailFirstTransactionDate",
        "dataType": "string",
        "comment": "Retail First Transaction Date"
    },
    {
        "name": "RetailLastTransactionDate",
        "dataType": "string",
        "comment": "Retail Last Transaction Date"
    },
    {
        "name": "TotalRetailItemsPurchased",
        "dataType": "double",
        "comment": "Total Retail Items Purchased"
    },
    {
        "name": "RetailAOV",
        "dataType": "double",
        "comment": "Retail AVO"
    },
    {
        "name": "RetailUPT",
        "dataType": "double",
        "comment": "Retail UPT"
    },
    {
        "name": "AvgDaysBetweenRetailTransaction",
        "dataType": "double",
        "comment": "Average Days between Transactions"
    },
    {
        "name": "TotalEcomTransaction",
        "dataType": "double",
        "comment": "Total Ecom Transactions"
    },
    {
        "name": "TotalEcomTransactionAmount",
        "dataType": "double",
        "comment": "Total Ecom Transaction Amount"
    },
    {
        "name": "TotalEcomDiscount",
        "dataType": "double",
        "comment": "Total Ecom Discount"
    },
    {
        "name": "EcomFirstTransactionDate",
        "dataType": "string",
        "comment": "Ecom First Transaction Date"
    },
    {
        "name": "EcomLastTransactionDate",
        "dataType": "string",
        "comment": "Ecom Last Transaction Date"
    },
    {
        "name": "TotalEcomItemsPurchased",
        "dataType": "double",
        "comment": "Total Ecom Items Purchased"
    },
    {
        "name": "EcomAOV",
        "dataType": "double",
        "comment": "Ecom AOV"
    },
    {
        "name": "EcomUPT",
        "dataType": "double",
        "comment": "Ecom UPT"
    },
    {
        "name": "AvgDaysBetweenEcomTransaction",
        "dataType": "double",
        "comment": "Avg days between ecom transactions"
    },
    {
        "name": "TotalTransaction",
        "dataType": "double",
        "comment": "Total overall #Transaction Till Date"
    },
    {
        "name": "TotalTransactionAmount",
        "dataType": "double",
        "comment": "Total Overall #Transaction Amount"
    },
    {
        "name": "TotalDiscount",
        "dataType": "double",
        "comment": "Total Overall Discount Till Date"
    },
    {
        "name": "TotalAOV",
        "dataType": "double",
        "comment": "Total AOV"
    },
    {
        "name": "TotalUPT",
        "dataType": "double",
        "comment": "Total UPT"
    },
    {
        "name": "LastModified",
        "dataType": "string",
        "comment": "Last Modified Timestamp"
    },
    {
        "name": "SecondaryPhone",
        "dataType": "string",
        "comment": "Secondary Phone"
    },
    {
        "name": "WeddingAnniversary",
        "dataType": "string",
        "comment": "Wedding Anniversary"
    },
    {
        "name": "EmailConsent",
        "dataType": "string",
        "comment": "Email Consent"
    },
    {
        "name": "SMSConsent",
        "dataType": "string",
        "comment": "SMS Consent"
    }
    ]
    }
    generated_query = lambda_handler(test_user_ip, None)
    print(generated_query)
