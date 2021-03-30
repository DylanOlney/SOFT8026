#! /bin/sh

# create grpc-server
kubectl create -f services/application/grpc-server-dep.yml
kubectl create -f services/application/grpc-server-svc.yml

# create grpc-client
kubectl create -f services/application/grpc-client-dep.yml

# create flask-server
kubectl create -f services/application/flask-server-dep.yml
kubectl create -f services/application/flask-server-svc.yml


# create prometheus monitoring service
kubectl create configmap prometheus-config --from-file monitoring/prometheus.yml
kubectl create -f services/monitoring/prometheus-dep.yml
kubectl create -f services/monitoring/prometheus-svc.yml


# create grafana metrics visualising service
kubectl create -f services/monitoring/grafana-dep.yml 
kubectl create -f services/monitoring/grafana-vol.yml  
kubectl create -f services/monitoring/grafana-svc.yml 


./continue.o






