 # SCMxpertLite - Supply Chain Management System

A modern web-based supply chain management system built with FastAPI, MongoDB, and Kafka for real-time device data monitoring.

## Features

- 🔐 User Authentication with reCAPTCHA
- 👥 Role-based Access Control (Admin/User)
- 📦 Shipment Management
- 📊 Real-time Device Data Monitoring
- 🔄 Kafka Integration for Data Streaming
- 🛠️ Docker Containerization

## Tech Stack

- **Backend**: FastAPI (Python)
- **Database**: MongoDB
- **Message Broker**: Apache Kafka
- **Frontend**: HTML, CSS, Jinja2 Templates
- **Authentication**: JWT, reCAPTCHA
- **Containerization**: Docker & Docker Compose

## Prerequisites

- Docker and Docker Compose
- Python 3.12+
- MongoDB Atlas Account
- Google reCAPTCHA API Keys

## Configuration

1. Create a `.env` file in the root directory with:

```env
MONGO_URI="your_mongodb_connection_string"
RECAPTCHA_SITE_KEY="your_recaptcha_site_key"
RECAPTCHA_SECRET_KEY="your_recaptcha_secret_key"
JWT_SECRET_KEY="your_jwt_secret_key"
JWT_ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=10
```

## Installation & Running

1. Build and start the containers:

```bash
docker-compose up --build
```

2. Access the application:
- Web Interface: http://localhost:8000
- API Documentation: http://localhost:8000/docs

## Project Structure

```
SCMxpert/
├── app.py              # Main FastAPI application
├── kafka/
│   ├── consumer.py     # Kafka consumer for device data
│   └── producer.py     # Kafka producer for device data
├── templates/          # HTML templates
├── static/            # Static files (CSS, images)
├── Dockerfile         # Main application Dockerfile
├── Dockerfile.consumer # Kafka consumer Dockerfile
├── Dockerfile.producer # Kafka producer Dockerfile
└── docker-compose.yml  # Docker compose configuration
```

## Features Breakdown

### User Management
- User registration and login
- Role-based access (Admin/User)
- reCAPTCHA integration for security
- Session management

### Shipment Management
- Create new shipments
- Track shipment status
- Edit shipment details (Admin)
- Delete shipments (Admin)

### Device Monitoring
- Real-time device data tracking
- Temperature monitoring
- Battery level tracking
- Route tracking

### Admin Features
- User management
- Shipment management
- Device data monitoring
- System administration

## Security Features

- Password hashing with bcrypt
- JWT-based authentication
- reCAPTCHA protection
- Role-based access control
- Session management

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
