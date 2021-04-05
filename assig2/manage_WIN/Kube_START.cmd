@echo off

REM create grpc-server
kubectl create -f ../services/application/grpc-server-dep.yml
kubectl create -f ../services/application/grpc-server-svc.yml

REM create grpc-client
kubectl create -f ../services/application/grpc-client-dep.yml

REM create flask-server
kubectl create configmap flask-source --from-file ../source/flask-server/flaskServer.py
kubectl create configmap flask-index --from-file ../source/flask-server/templates/index.html
kubectl create -f ../services/application/flask-server-dep.yml
kubectl create -f ../services/application/flask-server-svc.yml


REM create prometheus monitoring service
kubectl create configmap prometheus-config --from-file ../services/monitoring/prometheus.yml
kubectl create -f ../services/monitoring/prometheus-dep.yml
kubectl create -f ../services/monitoring/prometheus-svc.yml


REM create grafana dasboard service
kubectl create configmap grafana-dashboards --from-file ../services/monitoring/dashboard
kubectl create configmap grafana-dashcfg --from-file ../services/monitoring/dashboard.yml
kubectl create configmap grafana-datasource --from-file ../services/monitoring/datasource.yml
kubectl create configmap grafana-ini --from-file ../services/monitoring/grafana.ini
kubectl create -f ../services/monitoring/grafana-dep.yml 
kubectl create -f ../services/monitoring/grafana-svc.yml 

echo.
pause






