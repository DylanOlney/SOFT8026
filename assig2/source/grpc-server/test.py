import time
import pandas as pd
from datetime import datetime
import json 
  
string = "2017-11-10T07:38:29.000Z"
  
  
element = datetime.strptime(string,"%Y-%m-%dT%H:%M:%S.%fZ")
  
timestamp = datetime.timestamp(element)
print(timestamp)

def getTimestamp(value):
  dateString  = datetime.strptime(value,"%Y-%m-%dT%H:%M:%S.%fZ")
  return str(int(datetime.timestamp(dateString)))


def jsonify(row):
    temp = row.to_dict()
    id = temp['id']
    del temp['id']
    temp['timeStamp'] = time.time() 
    rtn = {}
    rtn[id] = temp
    return json.dumps(rtn,indent=3)

df_posts = pd.read_csv('r_dataisbeautiful_posts.csv', dtype=object)
df_vids  = pd.read_csv('GBvideos.csv', dtype=object)
df_vids.rename({'video_id':'id', 'comment_count':'num_comments'}, axis=1, inplace=True)
df_vids['created_utc'] = df_vids.apply(lambda row: getTimestamp(row.publish_time), axis = 1)
df_vids.drop(['tags', 'description', 'publish_time'], axis=1, inplace=True)
print(df_vids.head())

for index, row in df_vids.iterrows():
    d = jsonify(row)
    print(d)
    time.sleep(0.5)
