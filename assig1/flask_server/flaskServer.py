from flask import Flask, request, render_template
import json

# This script runs a Flask server for rendering a single web page which displays the
# required metrics data. The data is posted regularly here by the gRPC client which computes it.
# Scripts in the web page can then GET this data at regular intervals, for display.


# A global dictionary for storing the metrics data.
global metricsData
metricsData = dict()


app = Flask(__name__)


# This is the route that renders the dashboard web page.
@app.route('/')
def index():
    return render_template("index.html");  



# This route allows the gRPC client to POST the metrics data.
# It also allows the web page to GET it on demand.
@app.route('/metrics', methods = ['POST', 'GET'])
def data():
    global metricsData
    if request.method == 'POST':
         metricsData = request.get_json(force = True)
         return ''
    elif request.method == 'GET':
         try:
             return metricsData
         except:
             return ''
    else:
        return ''


        
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

