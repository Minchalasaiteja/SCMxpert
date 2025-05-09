from kafka import KafkaConsumer
from pymongo import MongoClient
import json

consumer = KafkaConsumer(
    'sensor_data',
    bootstrap_servers='kafka:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

MONGODB_URI = "mongodb+srv://saitejaminchala643:Prajwal1608@cluster1.2u2cmdn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1"

client = MongoClient(MONGODB_URI)
db = client.iot_data
collection = db.sensor_readings

print("Kafka consumer started. Waiting for messages...")

for message in consumer:
    data = message.value
    print(data)
    collection.insert_one(data)
    print(f"Inserted into MongoDB: {data}")
