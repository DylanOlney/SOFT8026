#! /bin/sh

kubectl delete deployment flask-server-dep
kubectl delete deployment grpc-server-dep
kubectl delete deployment grpc-client-dep

kubectl delete svc flask-server
kubectl delete svc grpc-server

./continue.o








