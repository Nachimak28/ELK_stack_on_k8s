# Deployment of ELK stack on K3s or in general - Kubernetes

WIP

## Prerequisites:
* A K8s/K3s cluster. 
* Helm


## Elastic Search

```bash
helm repo add elastic https://Helm.elastic.co
```

```bash
helm install elasticsearch elastic/elasticsearch -f k3s/elasticsearch_value_override.yaml
```


## Kibana

```bash
helm install kibana elastic/kibana -f k3s/kibana_value_override.yaml
```

## FluentD

```bash
helm repo add bitnami https://charts.bitnami.com/bitnami
```

```bash
helm install fluentd bitnami/fluentd
```

