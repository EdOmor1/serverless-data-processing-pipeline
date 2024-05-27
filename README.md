# serverless-data-processing-pipeline

Use Case: A streaming analytics platform for e-commerce companies. The platform ingests real-time data from various sources such as website visits, purchases, and customer interactions. The data is then transformed and analyzed to provide insights into customer behavior, product performance, and marketing effectiveness. The processed data is stored in an RDS database for further analysis and reporting.

## Repository Structure

- `src/`: Contains the source code and diagrams for the project.
  - `lambda/`: Contains the Python code for Lambda functions responsible for ingestion, transformation, and analysis.
  - `cloudformation/`: Contains CloudFormation templates for deploying Lambda functions, RDS database, and IAM roles.
  - `diagrams/`: Contains architectural and data flow diagrams for better understanding of the project.
- `README.md`: Documentation for setting up and using the project.
- `LICENSE`: License information for the project.

## Setup

1. Clone the repository.
2. Deploy the CloudFormation stacks located in the `src/cloudformation` directory.
3. Follow the instructions in each Lambda function's directory to deploy the functions.


