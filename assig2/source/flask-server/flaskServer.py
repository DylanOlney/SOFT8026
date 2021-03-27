from flask import Flask, request, render_template
import json

# This script runs a Flask server for rendering a single web page which displays the
# required metrics data. The data is posted regularly here by the gRPC client which computes it.
# Scripts in the web page can then GET this data at regular intervals, for display.


# A global dictionaries for storing the metrics data.
global postMetrics
global vidMetrics
postMetrics = dict()
vidMetrics = dict()

app = Flask(__name__)



# The index page with links to the others....

@app.route('/')
def index():
    return render_template("index.html");  


# These 2 routes render the webpages, one for posts and one for vids.

@app.route('/posts')
def posts():
    return render_template("posts.html");  


@app.route('/vids')
def vids():
    return render_template("vids.html");  



# This 2 routes allows the gRPC client to POST metrics data.
# also allowing the web pages to GET it on demand.

@app.route('/data_posts', methods = ['POST', 'GET'])
def data_posts():
    global postMetrics
    if request.method == 'POST':
         postMetrics = request.get_json(force = True)
         return ''
    elif request.method == 'GET':
         try:
             return postMetrics
         except:
             return ''
    else:
        return ''


@app.route('/data_vids', methods = ['POST', 'GET'])
def data_vids():
    global vidMetrics
    if request.method == 'POST':
         vidMetrics = request.get_json(force = True)
         return ''
    elif request.method == 'GET':
         try:
             return vidMetrics
         except:
             return ''
    else:
        return ''
       
 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

