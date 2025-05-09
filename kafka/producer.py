from kafka import KafkaProducer
import json
import time
import random

def create_sensor_data():
    return {
        "Device_ID": random.randint(1000, 2000),
        "Battery_Level": round(random.uniform(3.0, 5.0), 2),
        "First_Sensor_temperature": round(random.uniform(-10, 40), 1),
        "Route_From": "Chennai, India",
        "Route_To": "London, UK"
    }

def main():
    print("Connecting to Kafka...")
    producer = KafkaProducer(
        bootstrap_servers=['kafka:9092'],
        value_serializer=lambda x: json.dumps(x).encode('utf-8'),
        acks='all',
        retries=3
    )
    
    print("Connected to Kafka, starting to send messages...")
    while True:
        try:
            data = create_sensor_data()
            producer.send('sensor_data', value=data)
            print(f"Sent data: {data}")
            producer.flush()
            time.sleep(5)  # Send a message every 5 seconds
        except Exception as e:
            print(f"Error sending message: {e}")
            time.sleep(1)

if __name__ == "__main__":
    main()
