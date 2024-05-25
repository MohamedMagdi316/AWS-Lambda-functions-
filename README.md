# AWS-Lambda-
**1. Description of Selected Problem and Algorithm**
   The selected problem is to create and manage AWS Lambda functions for reading data from a DynamoDB table named "Atmosfera." The used algorithm involves using Python scripts within Lambda functions to read temperatura and humidade values from the table.

**2. System Architecture and Specifications**
•	Architecture: Serverless architecture using AWS Lambda and API Gateway.
      •	Technologies:
      •	AWS Lambda for function execution.
      •	DynamoDB for data storage.
      •	API Gateway for creating HTTP endpoints.

**3. Performance Analysis and Discussion of Results**
  The Lambda functions efficiently read data from DynamoDB with minimal latency. The API Gateway successfully exposes the functions as HTTP endpoints, enabling easy access. Performance is adequate for real-time data retrieval.

**Implementation Details**
  •	Function Creation:
•	getTemperatura: Reads temperatura from DynamoDB.
•	getHumidade: Reads humidade from DynamoDB.

  **Complete Source Code / Scripts**
  
The script can be directly used within AWS Lambda to create the respective functions. For a ready-to-work setup:

**Create DynamoDB Table:**
Table Name: Atmosfera
      Attributes: sala (String, Primary Key), temperatura (Number), humidade (Number).
**Create Lambda Functions:**
      Use the provided code snippets for getTemperatura and getHumidade.
      Setup API Gateway:
      Create an API to trigger the Lambda functions and expose them via HTTP endpoints.
