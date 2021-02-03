from prometheus_client import start_http_server, Gauge
import random
import time
import requests

# Create a metric to track time spent and requests made.
IP = Gauge('ip_as_a_number', 'IP address as a number')

def process_request():
    try:
        ip = requests.get('https://ifconfig.co/ip')
    except Exception as e:
        print(e)
        return(0)
    parts = ip.text[:-1].split('.')
    full = int(parts[0])*(10**9) + int(parts[1])*(10**6) + int(parts[2])*(10**3) + int(parts[3])
    IP.set(full)

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Generate some requests.
    while True:
        process_request()
        time.sleep(60)
