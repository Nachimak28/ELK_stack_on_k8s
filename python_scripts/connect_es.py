from elasticsearch import Elasticsearch

def connect_to_es_cluster(es_host):
    _es_obj = Elasticsearch(hosts=es_host, timeout=10)
    if _es_obj.ping():
        print('Connected successfully')
    else:
        print('Could not connect!')


connect_to_es_cluster(es_host='10.43.57.223') # cluster ip of the elasticsearch cluster deployed inside k8s

