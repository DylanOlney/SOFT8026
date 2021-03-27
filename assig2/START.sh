#! /bin/sh

# create grpc-server
kubectl create -f ./services/grpc-server-dep.yml
kubectl create -f ./services/grpc-server-svc.yml

# create grpc-client
kubectl create -f ./services/grpc-client-dep.yml

# create flask-server
kubectl create -f ./services/flask-server-dep.yml
kubectl create -f ./services/flask-server-svc.yml


./continue.o






