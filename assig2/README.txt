

Kubernetes - Deploying the services on the local machine:
---------------------------------------------------------
The .yml files for the Kubenetes deployments and services are in the 'services' folder.
A Docker image for each service has been created from the files in the 'source' folder and pushed to Docker Hub. 
These are pulled by the deployment files if not already present on the local machine.
The included START.sh script creates and deploys the architecture from the .yml files.
The included STOP.sh script stops it, terminating the services & deployments, killing all the relevant pods in the process.
Once deployed and up & running, the localhost port for viewing the analytics / metrics web pages is 30000.  


Architecture:
-------------
No new services were added since assignment 1. The existing ones were just modified to cater for the additional dataset 
streaming and metrics calculations. In the grpc-server, an extra rpc function was implemented for the streaming of the 2nd dataset. 
The grpc-client service in turn uses threads to receive the two streams in parallel, concurrently computing the metrics for each, 
and passing them onto the flask server. The web-server was also modified to display an extra page to show the metrics for the additional stream.


Metrics / Analytics:
--------------------
From the point of view of metrics calulations, the two datasets have some equivalent columns, allowing for the same 
type of analyics to be carried out on both. However, some pre-processing was required in the grpc-server code so that 
the equivalent columns relating to the analytics have the same column name and data format. Columns not relevant to the 
analytics are dropped before streaming.
