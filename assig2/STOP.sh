#! /bin/sh

kubectl delete deployment flask-server-dep
kubectl delete deployment grpc-server-dep
kubectl delete deployment grpc-client-dep
kubectl delete deployment prometheus-dep
kubectl delete deployment grafana


kubectl delete svc flask-server
kubectl delete svc grpc-server
kubectl delete svc grafana
kubectl delete svc prometheus
kubectl delete configmap prometheus-config

./continue.o








