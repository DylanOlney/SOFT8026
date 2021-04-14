
import time
import grpc
import json
import logging
import streamer_pb2 as pb2
import streamer_pb2_grpc as pb2_grpc
from benedict import benedict
import requests
from concurrent.futures import ThreadPoolExecutor

TIMEOUT_SEC = 2


def run():
    
    with grpc.insecure_channel('grpc-server:50051') as channel:
        
        while grpc_server_on(channel) == False:
            print('Waiting for gRPC server...')
            pass
        print('Server online. Connection established!')
        
        wait_for_serverless()

        stub = pb2_grpc.StreamerStub(channel)

        # These are the remote calls (the value of 'msg' is arbitrary).
        stream1 =  stub.getPosts(pb2.ClientRequest(msg='posts!'))  
        stream2 =  stub.getVids(pb2.ClientRequest(msg='vids!')) 

        postsStore = benedict() 
        vidsStore = benedict() 

        # Using two threads to read and process both streams concurrently. 
        with ThreadPoolExecutor(max_workers=2) as executor:
           executor.submit(processStream, stream1, postsStore, 'received blog post data from stream...', 'http://flask-server:5000/data_posts')
           executor.submit(processStream, stream2, vidsStore,  'received video data from stream...', 'http://flask-server:5000/data_vids')




def processStream(stream, store , msg, url):
    for resp in stream:
        print(msg)
        d = json.loads(resp.dataRow)
        store.merge(d)
        #data = updateMetrics(store)
        data = requests.post(url = 'http://metrics-func:8080', data = {'dataDict': store})
        postMetrics(url, json.dumps(data))


def grpc_server_on(channel) -> bool:
    try:
        grpc.channel_ready_future(channel).result(timeout=TIMEOUT_SEC)
        return True
    except grpc.FutureTimeoutError:
        return False

def wait_for_serverless():
     while True:
         resp = requests.post(url = 'http://metrics-func:8080', data = {'dataDict': 'test'}, timeout=2)
         if resp = 'ok':
            break;
         print("Waiting for serverless function to come online....")
     return


# The metrics for posts/videos to date are calculated here and are a follows:
# - the average no. of comments per post/video since streaming started.
# - the post/video with most comments so far, since streaming started.
# - the post/video with most comments in the last 3 minutes (will be the same as above for at least the 1st 3 min.).
# - the oldest post/video so far.


#def updateMetrics(dataDict):
#    total_comments = 0
#    max_comments = -999
#    earliest_date = 9999999999
#    key_most_comments = ''
#    key_oldest = ''
#    count = 0
#    for i in dataDict:
#        num_comments = int(dataDict[i]['num_comments'])
#        created_utc = int(dataDict[i]['created_utc'])
#        total_comments += num_comments
#        if num_comments > max_comments:
#            max_comments = num_comments
#            key_most_comments = i
#        if created_utc < earliest_date:
#            earliest_date = created_utc
#            key_oldest = i
#        count += 1
#    av_num_comments =  float(total_comments) / count
#     
#    max_comments_3min = -999
#    key_most_comments_3min = ''
#    t = int(time.time())
#    
#    # Rolling 3-min window of max comments...
#    for i in reversed(list(dataDict.keys())):
#        num_comments = int(dataDict[i]['num_comments'])
#        if int(dataDict[i]['streamed_time']) < (t - 180):
#            break
#       
#        if num_comments > max_comments_3min:
#             max_comments_3min = num_comments
#             key_most_comments_3min = i
#
#    metrics = {}  
#    metrics['av_num_comments'] = av_num_comments
#    metrics['most_comments'] = {key_most_comments: dataDict[key_most_comments]}
#    metrics['most_comments_3min'] = {key_most_comments_3min: dataDict[key_most_comments_3min]}
#    metrics['oldest_post'] = {key_oldest: dataDict[key_oldest]}
#    return json.dumps(metrics)




# This function POSTs the latest metrics data to the Flask web server.
def postMetrics(URL, jsonData):
    try:
        requests.post(url = URL, data = jsonData) 
    except:
        pass
    


if __name__ == '__main__':
    logging.basicConfig()
    run()
