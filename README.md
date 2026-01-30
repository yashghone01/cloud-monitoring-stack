# Origin DevOps Assignment — Sensor Monitoring Stack

This project deploys a simulated sensor service and a monitoring stack using Docker and VictoriaMetrics.

## Architecture
Sensor Service (Flask)
→ Exposes Prometheus-compatible metrics  
→ VictoriaMetrics scrapes them  
→ VMUI visualizes them in real time  

## Services

### Sensor Service
- Flask API exposing:
  - /sensor
  - /metrics
- Simulates:
  - CPU spikes
  - High memory payloads
  - Request latency
- Metrics:
  - sensor_requests_total
  - sensor_processing_latency_seconds
  - sensor_cpu_spike

### VictoriaMetrics
- Scrapes sensor metrics
- Stores time series
- Provides VMUI dashboard on port `8428`

---

## How to Run

```bash
docker-compose up

## Access:

Sensor API: http://localhost:8000/sensor

Metrics: http://localhost:8000/metrics

VMUI: http://localhost:8428/vmui

# Resource Limits
Docker Compose enforces memory limits:

Sensor: 80 MB

VictoriaMetrics: 120 MB

This simulates real edge-device constraints.

##Tech Stack
1. Python (Flask)
2. Prometheus client
3. Docker
4. Docker Compose
5. VictoriaMetrics

##Author
Yash Ghone
<img width="1366" height="768" alt="Project completion SS" src="https://github.com/user-attachments/assets/82a333b0-c9eb-4f49-aee2-bd5a9acb8032" />
