import logging
from prometheus_client import start_http_server, Summary, Gauge, Counter
import random
import time

# Metrics definitions
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
CPU_USAGE = Gauge('cpu_usage_percentage', 'CPU usage percentage')
MEMORY_USAGE = Gauge('memory_usage_percentage', 'Memory usage percentage')
DISK_USAGE = Gauge('disk_usage_percentage', 'Disk usage percentage')
NETWORK_USAGE = Gauge('network_usage_percentage', 'Network usage percentage')
REQUEST_COUNT = Counter('request_count', 'Total number of requests')

# Setup Prometheus monitoring server
def setup_prometheus_monitoring():
    start_http_server(8000)
    logging.info("Prometheus monitoring setup complete.")

# Monitor request processing time and increment request count
@REQUEST_TIME.time()
def monitor_request():
    time.sleep(random.random())  # Simulate request processing time
    REQUEST_COUNT.inc()  # Increment request count
    CPU_USAGE.set(random.uniform(0, 100))  # Simulate CPU usage
    MEMORY_USAGE.set(random.uniform(0, 100))  # Simulate memory usage
    DISK_USAGE.set(random.uniform(0, 100))  # Simulate disk usage
    NETWORK_USAGE.set(random.uniform(0, 100))  # Simulate network usage
    logging.info("Request monitored.")

# Monitor overall system metrics
def monitor_system_metrics():
    logging.info("Monitoring system metrics...")
    CPU_USAGE.set(random.uniform(0, 100))  # Simulate CPU usage
    MEMORY_USAGE.set(random.uniform(0, 100))  # Simulate memory usage
    DISK_USAGE.set(random.uniform(0, 100))  # Simulate disk usage
    NETWORK_USAGE.set(random.uniform(0, 100))  # Simulate network usage
    logging.info("System metrics monitored.")

# Monitor disk usage specifically
def monitor_disk_usage():
    logging.info("Monitoring disk usage...")
    DISK_USAGE.set(random.uniform(0, 100))  # Simulate disk usage
    logging.info("Disk usage monitored.")

# Monitor network usage specifically
def monitor_network_usage():
    logging.info("Monitoring network usage...")
    NETWORK_USAGE.set(random.uniform(0, 100))  # Simulate network usage
    logging.info("Network usage monitored.")

# Generate performance metrics over multiple iterations
def generate_performance_metrics():
    logging.info("Generating performance metrics...")
    for _ in range(10):
        monitor_request()  # Monitor individual request
        monitor_system_metrics()  # Monitor overall system
    logging.info("Performance metrics generated.")
