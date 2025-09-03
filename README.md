# Log_Monitoring_DashBoard

This project is a **containerized Kafka-based streaming application** built with Python. It simulates requests, produces logs, and consumes messages from Kafka topics, demonstrating a complete **producer-consumer workflow**.

---

## 🚀 Features

* Log producer for generating Kafka events
* Kafka consumer for processing messages
* Request simulation script for testing the pipeline
* Dockerized environment with `docker-compose`
* Modular design with separate producer, consumer, and app modules

---

## 📂 Project Structure

```
cc/
├── app.py               # Main application entry point
├── log_producer.py      # Kafka producer for logs
├── kafka_consumer.py    # Kafka consumer logic
├── simulate_requests.py # Request simulation utility
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker image definition
├── docker-compose.yml   # Multi-container orchestration
```

---

## 🛠️ Technologies Used

* **Python 3.8+**
* **Apache Kafka** – Event streaming platform
* **Docker & Docker Compose** – Containerization and orchestration

---

## ⚡ Getting Started

### Prerequisites

* Docker & Docker Compose installed
* Python 3.8+ (if running outside Docker)

### Setup with Docker

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/cc.git
   cd cc
   ```

2. Start the Kafka environment and app:

   ```bash
   docker-compose up --build
   ```

3. The producer and consumer services will start automatically.

### Run Locally (Without Docker)

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Start Kafka locally (ZooKeeper + Kafka broker).

3. Run the producer and consumer:

   ```bash
   python log_producer.py
   python kafka_consumer.py
   ```

4. Simulate requests:

   ```bash
   python simulate_requests.py
   ```

---

## 📖 Workflow

1. `simulate_requests.py` generates mock requests.
2. `log_producer.py` sends logs/messages to Kafka.
3. `kafka_consumer.py` listens to the Kafka topic and processes the messages.

---


