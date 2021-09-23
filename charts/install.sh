
# kubectl create namespace monitoring

# Metrics Server
kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml

# Prometheus
helm upgrade --install prometheus  \
  ./prometheus \
  --namespace monitoring \
  --values ./prometheus/values-boldx.yaml

# Grafana
helm upgrade --install grafana  \
  ./grafana \
  --namespace monitoring \
  --values ./grafana/values-boldx.yaml

# Elasticsearch
helm upgrade --install elasticsearch  \
  ./elasticsearch \
  --namespace monitoring

# Kibana
helm upgrade --install kibana  \
  ./kibana \
  --namespace monitoring \
  --values ./kibana/values-boldx.yaml

# Logstash
helm upgrade --install logstash  \
  ./logstash \
  --namespace monitoring \
  --values ./logstash/values-boldx.yaml

# Jaeger
helm upgrade --install jaeger-tracing  \
  ./jaeger \
  --namespace monitoring \
  --values ./jaeger/values-boldx.yaml