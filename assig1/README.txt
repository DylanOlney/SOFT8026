
N.B. The 'r_dataisbeautiful_posts.csv' dataset file is NOT included and needs to be placed in the 'grpc_server' folder 
before running 'docker-compose up' or 'docker-compose build', for the application to work.

There are three services in my assignment solution:

1. grpc_server      
2. grpc_client      
3. flask_server     

Each service has it's own build folder, Dockerfile and 'requirements.txt' file.
For the grpc client & server services, the required pb2 and pb2_grpc files were compiled from 
the 'streamer.proto' file in his directory using the following shell command:

python3 -m grpc_tools.protoc  -I./ --python_out=. --grpc_python_out=. streamer.proto

Copies of both of these files were then placed in both of the grpc service folders and deleted from this directory.
On running 'docker-compose up' from this directory, the metrics display webpage served by the Flask service can be viewed at:  

http://localhost:5000  

(Port 5000 of the flask_server container is mapped to port 5000 on the host machine - see 'docker-compose.yml' file). 
Note: It may take few seconds after the services start before results are available to the web page. If this
is the case, refresh the page and the results should start showing, updating automatically every 500ms thereafter.


Explanation of Operation
--------------------------
The grpc server firstly loads the dataset into memory and provides a remote procedure for clients to stream it, entry by entry.
As soon as the grpc client establishes that the server is up and ready, it calls this procedure and the streaming begins. 
Whenever the client recieves a new row of data from the stream, it firstly adds the record to an in-memory strore (see below).
It then computes/updates the metrics data before POST-ing the results (as JSON) to the Flask server.
The web page hosted by the Flask server dynamically reflects these results as they are generated, without the need to refresh 
it in the browser, as it contains a script which polls the Flask server with regular GET requests. 


In-memory data store
--------------------
There is no separate data storage service as the grpc_client service uses an in-memory data structure to store the streamed records.
This is implemented using a globally defined 'python-benedict' dictionary, which has the ability to merge with other dictionaries. 
In the resulting structure, each key is a unique post ID that maps to a sub-dictionary, which in turn maps the other field names 
of the post to their values. Also, because the metrics data is POST-ed directly to the web server, the need to store it somewhere
so that it can retrieve it, is eliminated.

