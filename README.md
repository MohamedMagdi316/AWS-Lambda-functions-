# AWS-Lambda-
. Description of Selected Problem and Algorithm
The selected problem is to create and manage AWS Lambda functions for reading data from a DynamoDB table named "Atmosfera." The used algorithm involves using Python scripts within Lambda functions to read temperatura and humidade values from the table.
2. System Architecture and Specifications
•	Architecture: Serverless architecture using AWS Lambda and API Gateway.
•	Technologies:
•	AWS Lambda for function execution.
•	DynamoDB for data storage.
•	API Gateway for creating HTTP endpoints.
3. Performance Analysis and Discussion of Results
The Lambda functions efficiently read data from DynamoDB with minimal latency. The API Gateway successfully exposes the functions as HTTP endpoints, enabling easy access. Performance is adequate for real-time data retrieval.
Implementation Details
•	Function Creation:
•	getTemperatura: Reads temperatura from DynamoDB.
•	getHumidade: Reads humidade from DynamoDB.
•	Code for getTemperatura Function

