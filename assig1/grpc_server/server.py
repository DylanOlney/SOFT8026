
import grpc
import time
import logging
import pandas as pd
from concurrent import futures
import streamer_pb2 as pb2
import streamer_pb2_grpc as pb2_grpc
import json


# Loading the dataset into memory (global dataframe).
df = pd.read_csv('r_dataisbeautiful_posts.csv', dtype=object)

class StreamerService(pb2_grpc.StreamerServicer):

    # This is the method by which clients remotely request the data stream.
    # A loop calls a function which converts the dataframe rows to 
    # JSON strings and yields them one-by-one to the response stream.

    def getPosts(self, request, context):
       
        for index, row in df.iterrows():
            d = jsonify(row)
            time.sleep(0.5)   # adding a 500ms delay.
            print('Adding post data to stream...')
            yield pb2.ServerResponse(dataRow=d)




# This helper function takes a single row of data (pd series) and converts it
# to a dictionary with one element whose key is the 'id' field. The value of this
# dictionary is a sub dictionary containing the other field names and their values. 
# A time stamp is added along with the fields to record when the post was streamed.
# This configuration is then dumped to a JSON string which is returned.

def jsonify(row):
    temp = row.to_dict()
    id = temp['id']
    del temp['id']
    temp['timeStamp'] = time.time() 
    rtn = {}
    rtn[id] = temp
    return json.dumps(rtn, indent=3)
            

    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_StreamerServicer_to_server(StreamerService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
