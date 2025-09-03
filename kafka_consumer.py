from kafka import KafkaConsumer
import json
import psycopg2

# Kafka consumer setup
consumer = KafkaConsumer(
    'logs-topic',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='log-consumers'
)

# PostgreSQL connection setup
conn = psycopg2.connect(
    host="localhost",
    database="logdb",
    user="user",
    password="password"
)
cursor = conn.cursor()

print("✅ Kafka Consumer connected. Listening for logs...")

for message in consumer:
    log = message.value
    print("📥 Received log:", log)
    
    # Insert into PostgreSQL
    cursor.execute(
        "INSERT INTO logs (endpoint, status_code, response_time, timestamp) VALUES (%s, %s, %s, %s)",
        (log["endpoint"], log["status_code"], log["response_time"], log["timestamp"])
    )
    conn.commit()
