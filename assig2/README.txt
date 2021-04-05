

Kubernetes - Deploying the services on the local machine:
---------------------------------------------------------
The yml files for the Kubenetes deployments and services are in the 'services.yml' folder.
A Docker image for each application service has been created from the files in the 'source' folder and pushed to Docker Hub. 
These are pulled by the deployment files if not already present on the local machine.

Scripts to start/stop/view services are in 'scripts_LINUX' or 'scripts_WIN' folders, depending on OS:

 - The START script creates and deploys the architecture from the yml files.
 - The STOP script stops it, terminating the services & deployments and killing all the relevant pods.
 - The INFO script shows the state of deployments, services and pods running at any given time.

Once services are deployed, the localhost port for viewing the analytics / metrics web pages is 30000. 
Use the INFO script to make sure all services are up & running before trying to access the page.
This page also has a link to a dashboard for monitoring the Flask server.


Architecture:
-------------
Apart from monitoring services, no extra application services were added since assignment 1. The existing ones were just modified to 
cater for the additional dataset streaming and metrics calculations. In the grpc-server, an extra rpc function was implemented for the 
streaming of the 2nd dataset. The grpc-client service in turn uses threads to receive the two streams in parallel, concurrently computing 
the metrics for each, and passing them onto the flask server. The web-server was also modified to display an extra page to show the metrics 
for the additional stream.


Metrics / Analytics:
--------------------
From the point of view of metrics / analytics calulations, the two datasets have some equivalent columns, allowing for 
the same kind of analyics to be carried out on both. However, some pre-processing was required in the grpc-server code so that 
the equivalent columns relating to the analytics have the same column name and data format. Columns not relevant to the 
analytics are dropped before streaming.


Monitoring & Visualization Services (Prometheus & Grafana)
-----------------------------------------
Prometheus, a monitoring & time series database software was chosen for the purpose of monitoring the Flask server. This was chosen
because there is a convenient and straight forward library for Flask called 'prometheus_flask_exporter' which enables Prometheus to 'scrape' 
data from it via a '/metrics' endpoint. Furthermore, the data that is to be exposed to Prometheus is easily configured in the Flask code 
with the help of annotations. For deployment as a Kubernetes service, a docker image of this software was used. 

For the visualization of the monitored data, an application called Grafana was chosen. This web application enables the creation of a 
dashboard page showing charts of data, and it is easily configured to set up Prometheus as the data source. Again, a docker image 
was used for the creation of this service. 

The two services above are configured to monitor and display the following 3 statistics from the Flask server:

  1. Endpoint monitoring, i.e. request counts on each endpoint.
  2. CPU usage.
  3. Memory usage.

The services are started along with the other application services via the 'START' script.
A link for viewing the Grafana dasboard page is provided in the application's index page (localhost:30000).


Functional Testing of Flask Endpoints:
--------------------------------------
The testing aspect of the project again concentrates on the Flask server API. Postman was used to develop a collection of some 25 individual tests for 
the endpoints in which all possible GET and POST requests are tested. The tests were then exported to a JSON file (tests/postman/collection.json) which 
may be re-imported to any Postman workspace in order to run them. However, for this application, a CLI utility called Newman is used to execute them from 
the JSON file, so there is no need to have Postman installed. This utilty is run from a docker image in order to save from having to install it and 
its Node.js dependencies. When the services are up, running the included 'run_TESTS.sh' script will pull the Newman docker image, create the container 
and run all of the tests in the collection. Results are then displayed in the terminal. All of the API tests are functional in that their aim is to 
assert that the endpoints are producing valid, expected responses. 

Although the tests are not automated in that you must run the script manually after deployimg the services, they could easily enough be 
integrated into a CI/CD type devops environment such as Jenkins, where the script could be triggered after each build. However, setting up 
such an environment would be something of an overkill for this project. Another automation option would be to set up a monitor in the Postman 
application, enabling the test suite to be run periodically. However, Postman does not support monitoring of internal localhost services, 
meaning that they would need to be hosted externally on a publicly available server. 











