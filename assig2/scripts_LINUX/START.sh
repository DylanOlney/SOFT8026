#! /bin/sh

# create grpc-server
kubectl create -f ../services.yml/application/grpc-server-dep.yml
kubectl create -f ../services.yml/application/grpc-server-svc.yml

# create grpc-client
kubectl create -f ../services.yml/application/grpc-client-dep.yml

# create flask-server
kubectl create configmap flask-source --from-file ../source/flask-server/flaskServer.py
kubectl create configmap flask-index --from-file ../source/flask-server/templates/index.html
kubectl create -f ../services.yml/application/flask-server-dep.yml
kubectl create -f ../services.yml/application/flask-server-svc.yml


# create prometheus monitoring service
kubectl create configmap prometheus-config --from-file ../services.yml/monitoring/prometheus.yml
kubectl create -f ../services.yml/monitoring/prometheus-dep.yml
kubectl create -f ../services.yml/monitoring/prometheus-svc.yml


# create grafana dasboard service
kubectl create configmap grafana-dashboards --from-file ../services.yml/monitoring/dashboard
kubectl create configmap grafana-dashcfg --from-file ../services.yml/monitoring/dashboard.yml
kubectl create configmap grafana-datasource --from-file ../services.yml/monitoring/datasource.yml
kubectl create configmap grafana-ini --from-file ../services.yml/monitoring/grafana.ini
kubectl create -f ../services.yml/monitoring/grafana-dep.yml 
kubectl create -f ../services.yml/monitoring/grafana-svc.yml 


./helper/continue.o






