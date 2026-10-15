# AWS Event-Driven Data Ingestion Pipeline

## 1. Project Overview

This project aims to build a scalable, event-driven data ingestion pipeline using AWS services and Python. The system is designed to capture e-commerce order events, store them, process them asynchronously, and make them available for downstream analytics.

The main goal is to understand how modern data engineering systems handle real-time events, reliable message delivery, and scalable processing using cloud services.

**Project Status:** In Progress

## 2. Business Problem

E-commerce applications generate order events continuously. Processing every event synchronously can increase response times and make systems harder to scale.

This project addresses these challenges by designing an event-driven architecture that separates event creation, storage, processing, and notification.

## 3. Project Objectives

- Generate and validate e-commerce order events using Python.
- Store order data in Amazon DynamoDB.
- Capture table changes using DynamoDB Streams.
- Process events automatically using AWS Lambda.
- Use Amazon SNS to distribute event notifications.
- Use Amazon SQS to buffer messages for asynchronous processing.
- Implement retries, duplicate-event handling, and dead-letter queues.
- Monitor processing activity and errors using Amazon CloudWatch.
- Maintain code, tests, and documentation in GitHub.

## 4. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Generate and validate order events |
| Amazon DynamoDB | Store order records |
| DynamoDB Streams | Capture database changes |
| AWS Lambda | Process events automatically |
| Amazon SNS | Publish notifications |
| Amazon SQS | Queue events for asynchronous processing |
| Amazon CloudWatch | Monitor logs and errors |
| Git | Track source-code changes |
| GitHub | Store and document the project |

## 5. Architecture and Workflow

The planned data flow is:

1. **Event Generation:** A Python producer creates an order event containing order ID, customer ID, product ID, quantity, amount, and status.
2. **Data Storage:** The producer writes the order to an Amazon DynamoDB table.
3. **Change Capture:** DynamoDB Streams captures new or updated order records.
4. **Event Processing:** AWS Lambda reads stream records and validates the event.
5. **Event Publishing:** Lambda publishes valid order events to an Amazon SNS topic.
6. **Message Queuing:** SNS delivers messages to an Amazon SQS queue.
7. **Downstream Processing:** A queue consumer processes the messages for further business logic or analytics.
8. **Monitoring and Recovery:** CloudWatch captures logs and errors, while retries and a dead-letter queue help handle failures.

### Architecture Diagram

```text
Python Order Producer
         |
         v
   Amazon DynamoDB
         |
         v
  DynamoDB Streams
         |
         v
    AWS Lambda
         |
         v
     Amazon SNS
         |
         v
     Amazon SQS
         |
         v
  Queue Consumer
         |
         v
 Downstream Analytics

CloudWatch: Logs and Monitoring
Dead-Letter Queue: Failed Messages
```

## 6. Sample Order Event

Example JSON event:

```json
{
  "event_id": "evt-1001",
  "event_type": "ORDER_CREATED",
  "order_id": "ORD-1001",
  "customer_id": "CUST-101",
  "product_id": "PROD-501",
  "quantity": 2,
  "amount": 1499.00,
  "status": "CREATED"
}
```

The event ID identifies the event, while the order ID identifies the business order. This distinction is useful when implementing duplicate-event handling.

## 7. Current Project Structure

```text
aws-event-driven-ingestion/
├── .gitignore
├── README.md
├── src/
│   └── producer.py
├── events/
│   └── sample_order.json
├── tests/
└── docs/
```

- `src/producer.py` — Initial Python producer program.
- `events/sample_order.json` — Sample e-commerce order event.
- `tests/` — Planned automated tests.
- `docs/` — Planned architecture and implementation documentation.
- `.gitignore` — Excludes local and unnecessary files.
- `README.md` — Project overview and implementation guide.

## 8. Implementation Progress

### Completed

- Created the project folder and directory structure.
- Created the initial Python producer file.
- Verified that Python code runs using the Python launcher.
- Created a sample order event in JSON.
- Added a `.gitignore` file.
- Initialized Git and committed the initial project files.
- Created a public GitHub repository and pushed the `main` branch.

### In Progress / Planned

- Implement Python event generation and validation.
- Configure AWS account access and cost controls.
- Create the DynamoDB table.
- Enable DynamoDB Streams.
- Implement the Lambda stream processor.
- Configure SNS and SQS integration.
- Add retries, idempotency, and a dead-letter queue.
- Configure CloudWatch monitoring.
- Add automated tests and end-to-end validation.

## 9. Reliability and Security

The project will incorporate the following practices:

- Validate incoming event fields before processing.
- Handle duplicate event deliveries safely through idempotent processing.
- Configure retries and a dead-letter queue for repeated failures.
- Apply least-privilege IAM permissions to AWS resources.
- Never commit AWS credentials, access keys, or secrets to GitHub.
- Monitor failures and queue backlogs using CloudWatch.
- Review AWS costs and remove resources when they are no longer needed.

## 10. How to Run the Current Local Demo

Prerequisite: Python must be installed and available through the Windows Python launcher.

From the project root, run:

```powershell
py src/producer.py
```

The current program prints a project confirmation message. It is an initial local demo and does not yet connect to AWS.

## 11. Future Enhancements

- Add configurable order-event generation.
- Integrate the producer with DynamoDB using Boto3.
- Deploy the event-processing architecture.
- Add unit and integration tests.
- Measure processing latency and failure rates.
- Extend downstream processing to an analytics destination.
- Document deployment and cleanup procedures.

## 12. Repository

GitHub: https://github.com/Erantikarthik/aws-event-driven-ingestion

## 13. Learning Outcomes

This project is intended to demonstrate practical understanding of:

- Event-driven architecture.
- Cloud-based data ingestion.
- Change data capture and stream processing.
- Asynchronous messaging and decoupled services.
- Fault tolerance and idempotent processing.
- AWS monitoring, security, and cost awareness.
- Git-based version control and project documentation.
