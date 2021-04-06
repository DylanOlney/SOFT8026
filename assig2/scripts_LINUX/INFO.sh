#! /bin/sh

echo 'Deployments'
echo '--------------------------------------------------------------------------'
kubectl get deployment
echo '\nServices'
echo '--------------------------------------------------------------------------'
kubectl get svc
echo '\nPods'
echo '--------------------------------------------------------------------------'
kubectl get pod


echo "\nPress ENTER to continue..."
read input











