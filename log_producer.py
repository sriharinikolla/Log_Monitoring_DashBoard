from kafka import KafkaProducer
import json
import time
import random

print("⏳ Initializing Kafka Producer...")

try:
    producer = KafkaProducer(
        bootstrap_servers='localhost:9092',  # Use 'kafka:9092' if inside Docker
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    print("✅ Kafka Producer initialized.")
except Exception as e:
    print("❌ Failed to initialize Kafka Producer:", e)
    exit()

endpoints = ["/api/login", "/api/logout", "/api/products", "/api/orders", "/api/status"]

print("🚀 Starting to send logs...")

while True:
    try:
        log = {
            "endpoint": random.choice(endpoints),
            "status_code": random.choice([200, 400, 500]),
            "response_time": round(random.uniform(0.1, 1.5), 3),
            "timestamp": time.time()
        }

        print("📤 Sending log:", log)
        producer.send('logs-topic', log)
        producer.flush()
        print("✅ Log sent!")

    except Exception as e:
        print("❌ Error while sending log:", e)

    time.sleep(1)
