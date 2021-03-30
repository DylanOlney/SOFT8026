#! /bin/sh

echo 'Deployments:'
kubectl get deployment
echo '\nServices:'
kubectl get svc
echo '\nPods:'
kubectl get pod

./continue.o








