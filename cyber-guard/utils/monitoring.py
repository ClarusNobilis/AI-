from app import app
from prometheus_client import Counter, Histogram
from prometheus_flask_exporter import PrometheusMetrics

REQUEST_COUNT = Counter(
    'http_request_count', 'Total HTTP Requests',
    ['method', 'endpoint', 'status_code']
)

REQUEST_LATENCY = Histogram(
    'http_request_latency_seconds', 'HTTP Request Latency',
    ['method', 'endpoint']
)

metrics = PrometheusMetrics(app)
metrics.info('app_info', 'Application info', version='1.0.0')