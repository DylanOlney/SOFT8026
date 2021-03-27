
import time
import grpc
import json
import logging
import streamer_pb2 as pb2
import streamer_pb2_grpc as pb2_grpc
from benedict import benedict
import requests


TIMEOUT_SEC = 2
dataStore = benedict() # A benedict dictionary.
                      # This is a mergeable extension of a regular dict() 
                     # and it will be used as an in-memory store for incoming data.

metricStore = dict()


def run():
    
    with grpc.insecure_channel('grpc_server:50051') as channel:
        while grpc_server_on(channel) == False:
            print('Waiting for gRPC server...')
            pass
        print('Server online. Connection established!')
        stub = pb2_grpc.StreamerStub(channel)
        stream = stub.getPosts(pb2.ClientRequest(msg='ready!'))  # This is the remote call (the value of 'msg' is arbitrary).
        for resp in stream:
           print('Recieved post data from stream...')
           d = json.loads(resp.dataRow)
           dataStore.merge(d)
           updateMetrics()
           postMetrics()


def grpc_server_on(channel) -> bool:
    try:
        grpc.channel_ready_future(channel).result(timeout=TIMEOUT_SEC)
        return True
    except grpc.FutureTimeoutError:
        return False

# The metrics for posts to date are calculated here and are a follows:
# - the average no. of comments per post since streaming started.
# - the post with most comments so far, since streaming started.
# - the post with most comments in the last 3 minutes (will be the same as above for at least the 1st 3 min.).
# - the oldest post so far.
def updateMetrics():
    total_comments = 0
    max_comments = -999
    earliest_date = 9999999999
    key_most_comments = ''
    key_oldest = ''
    count = 0
    keys = []
    for i in dataStore:
        keys.append(i)
        num_comments = int(dataStore[i]['num_comments'])
        created_utc = int(dataStore[i]['created_utc'])
        total_comments += num_comments
        if num_comments > max_comments:
            max_comments = num_comments
            key_most_comments = i
        if created_utc < earliest_date:
            earliest_date = created_utc
            key_oldest = i
        count += 1
    av_num_comments =  float(total_comments) / count
     
    max_comments_3min = -999
    key_most_comments_3min = ''
    t = time.time()
    
    # Rolloing 3 min. window of highest commentsin last
    for i in reversed(list(dataStore.keys())):
        num_comments = int(dataStore[i]['num_comments'])
        if dataStore[i]['timeStamp'] < (t - 180):   # only process 
            break
       
        if num_comments > max_comments_3min:
             max_comments_3min = num_comments
             key_most_comments_3min = i
        
    metricStore['av_num_comments'] = av_num_comments
    metricStore['most_comments'] = {key_most_comments: dataStore[key_most_comments]}
    metricStore['most_comments_3min'] = {key_most_comments_3min: dataStore[key_most_comments_3min]}
    metricStore['oldest_post'] = {key_oldest: dataStore[key_oldest]}
    #print(json.dumps(metricStore,indent=2))




# This function POSTs the latest metrics data to the Flask web server.
def postMetrics():
    URL = 'http://flask_server:5000/metrics'
    try:
        requests.post(url = URL, data = json.dumps(metricStore)) 
    except:
        pass
    


if __name__ == '__main__':
    logging.basicConfig()
    run()
