# Sensor Observability Stack (DevOps Project)

A production-style observability system built using Docker, Python and VictoriaMetrics to monitor a simulated sensor API in real time.

## 🚀 What this project demonstrates
- Dockerized microservices
- Prometheus-style metrics exposure
- Time-series scraping & storage using VictoriaMetrics
- Live visualization using VMUI
- Memory-limited containers to simulate real infrastructure
- Cloud deployment on AWS EC2

## 🧩 Architecture
Client → Sensor API → /metrics → VictoriaMetrics → VMUI Dashboard

## 📦 Components

### 1. Sensor Service (Flask)
A Python service that simulates IoT sensor traffic and exposes:
- Request count
- CPU spike state
- Request latency

Metrics are exported in Prometheus format at:

### 2. VictoriaMetrics
Scrapes the sensor metrics every 5 seconds and stores time-series data.

Exposes:
- Query API
- VMUI dashboard

## 🐳 How to Run

```bash
docker-compose up -d

Sensor API:
http://localhost:8000/sensor

Metrics:
http://localhost:8000/metrics

Dashboard:
http://localhost:8428/vmui

Example Query:
sensor_requests_total
Shows number of sensor requests processed.

☁️ Cloud Deployment

This stack is deployed on AWS EC2 using Docker.

Public VMUI:
http://<ec2-ip>:8428/vmui
