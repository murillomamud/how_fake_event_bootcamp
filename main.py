import boto3
import json
from fake_web_events import Simulation

client = boto3.client('firehose')

def put_record(event:dict):
    data = json.dumps(event) + "/n" 
    response = client.put_record(
        DeliveryStreamName='bootcamp-class2', #kinesis service name
        Record={"Data":data}
    )
    print(event)
    return response

simulation = Simulation(user_pool_size=100,sessions_per_day=1000000)    
events = simulation.run(duration_seconds=10)

for event in events:
    put_record(event)

  