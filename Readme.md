ScaleCart – Scalable E-Commerce Backend System

ScaleCart is a scalable e-commerce backend system designed using FastAPI, MongoDB, and Redis.  
The project focuses on backend architecture, performance optimization, and system design concepts commonly used in real-world e-commerce platforms.

Features
- Product management APIs
- Cart service with Redis caching
- Order placement APIs
- API rate limiting for checkout
- Modular backend architecture
- Designed for scalability and performance

Tech Stack
- Backend: FastAPI (Python)
- Database: MongoDB
- Caching: Redis
- API Style: REST
- Tools: Git, Postman

 
 Architecture Overview
 Products stored in MongoDB
- Cart data cached in Redis for fast access
- Checkout endpoint protected with rate limiting


 Setup Instructions

 Prerequisites
- Python 3.9+
- MongoDB (local or Atlas)
- Redis (local)

Install dependencies
```bash
pip install fastapi uvicorn pymongo redis
