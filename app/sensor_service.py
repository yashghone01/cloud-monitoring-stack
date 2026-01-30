import time
import random
from flask import Flask, jsonify
from prometheus_client import Counter, Gauge, Histogram, generate_latest

app = Flask(__name__)

# Reduced from 5MB to 50KB
data_blob = "X" * 50_000

REQUEST_COUNT = Counter("sensor_requests_total", "Total sensor requests")
CPU_SPIKE = Gauge("sensor_cpu_spike", "Simulated CPU spike state")
PROCESS_LATENCY = Histogram("sensor_processing_latency_seconds", "Processing time")

@app.route("/metrics")
def metrics():
    start = time.time()

    # Simulate latency without CPU burn
    time.sleep(0.01)

    PROCESS_LATENCY.observe(time.time() - start)
    CPU_SPIKE.set(random.randint(0, 1))
    REQUEST_COUNT.inc()

    return generate_latest()

@app.route("/sensor")
def sensor():
    if random.random() < 0.2:
        # Return metadata instead of huge blob
        return jsonify({"data_size": len(data_blob)})

    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
