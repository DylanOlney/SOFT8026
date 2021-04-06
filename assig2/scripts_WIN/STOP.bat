@echo off
echo Deleting all services, deployments and configmaps...
echo.
REM delete deployments
kubectl delete deployment flask-server-dep
kubectl delete deployment grpc-server-dep
kubectl delete deployment grpc-client-dep
kubectl delete deployment prometheus-dep
kubectl delete deployment grafana

REM delete services
kubectl delete svc flask-server
kubectl delete svc grpc-server
kubectl delete svc grafana
kubectl delete svc prometheus

REM delete configmaps
kubectl delete configmap prometheus-config
kubectl delete configmap grafana-dashboards
kubectl delete configmap grafana-dashcfg
kubectl delete configmap grafana-datasource
kubectl delete configmap grafana-ini
kubectl delete configmap flask-source
kubectl delete configmap flask-index

echo.
echo Services are stopping...
echo Run INFO.bat to check status.
echo.
pause








