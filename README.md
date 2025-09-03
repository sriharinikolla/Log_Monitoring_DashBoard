# Log_Monitoring_DashBoard
# 🌀 Kafka Log Processing App

A containerized Python application for **producing, consuming, and simulating log data streams** using **Kafka**.  
This project demonstrates a simple **event-driven architecture** where logs are produced, sent to Kafka, and consumed in real time.

---


---

## 📑 Table of Contents
- [About](#-about)    
- [Installation](#-installation)  
- [Usage](#-usage)  
- [Configuration](#-configuration)   

---

## 📖 About
This project simulates a **real-time log processing pipeline** with **Kafka**.  
- **Producer** sends log events to Kafka  
- **Consumer** reads and processes events  
- **Simulated requests** generate fake workloads for testing  

It’s a great starter for learning **Kafka + Python + Docker** in distributed systems.

---

---

## ⚙️ Installation

### Prerequisites
- [Docker](https://docs.docker.com/get-docker/) & [Docker Compose](https://docs.docker.com/compose/)  
- Python 3.9+ (if running locally without Docker)

### Clone Repository
```bash
git clone https://github.com/yourusername/cc.git
cd cc

---

## 🚀 Usage

### Run with Docker Compose
```bash
docker-compose up --build
1.Starts Kafka + Zookeeper + App
2.Logs will stream in real-time

docker-compose exec app python simulate_requests.py
3.simulates log requests

docker-compose logs -f app
4.watch consumer output

---

##🔧 Configuration

Environment variables can be added (for example, Kafka broker settings).
Update docker-compose.yml or .env file (if you add one) to configure:

Kafka broker URL

Topic names

Consumer group ID

