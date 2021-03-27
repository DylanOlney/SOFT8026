
import grpc
import time
import logging
import pandas as pd
from concurrent import futures
import streamer_pb2 as pb2
import streamer_pb2_grpc as pb2_grpc
import json
from datetime import datetime


# Loading & pre-processing datasets ====================================================================================

# The two datasets have some equivalent columns of interest: id, no. of comments and publishing time.
# However, they are named differently and may have different formats, e.g. publishing time.
# The pre-processing done here, homogenizes the columns of interest so that they have the same name and format in both sets.
# This will enable the the analytics client to easily compute the same metrics on both of them.


df_posts = pd.read_csv('r_dataisbeautiful_posts.csv', dtype=object)
df_vids  = pd.read_csv('GBvideos.csv', dtype=object)

# Filling NaN values with a 'null' string.
df_posts.fillna('null', inplace=True)
df_vids.fillna('null', inplace=True)


# Pre-processing 'df_vids' so that the relevant, equivalent column names match that of 'df_posts'
df_vids.rename({'video_id':'id', 'comment_count':'num_comments'}, axis=1, inplace=True)


# Converting publish_time column values to timestamp format and putting results in new column, 'created_utc'.

def convertDate(value):
  dateString  = datetime.strptime(value,"%Y-%m-%dT%H:%M:%S.%fZ")
  return str(int(datetime.timestamp(dateString)))

df_vids['created_utc'] = df_vids.apply(lambda row: convertDate(row.publish_time), axis = 1)

#df_vids.drop(['tags', 'description', 'publish_time'], axis=1, inplace=True)

# keeping only columns of interest for the metrics being computed.
df_vids  =  df_vids[["id", "title", "num_comments" ,"created_utc"]]
df_posts = df_posts[["id", "title", "num_comments" ,"created_utc"]]


# =================================================================================================================



class StreamerService(pb2_grpc.StreamerServicer):

    # This is the method by which clients remotely request the data streams.
    # A loop calls a function which converts the dataframe rows to 
    # JSON strings and yields them one-by-one to the response stream.


    def getPosts(self, request, context):
        for index, row in df_posts.iterrows():
            d = jsonify(row)
            time.sleep(0.5)   # adding a 500ms delay.
            print('Adding post data to stream...')
            yield pb2.ServerResponse(dataRow=d)

    def getVids(self, request, context):
        for index, row in df_vids.iterrows():
            d = jsonify(row)
            time.sleep(0.5)   # adding a 500ms delay.
            print('Adding video data to stream...')
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
    temp['streamed_time'] = str(int(time.time())) 
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
