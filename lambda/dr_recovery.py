import boto3
import time

drs = boto3.client('drs')
SOURCE_SERVER_ID = 's-xxxxxxxxxxxx'

def lambda_handler(event, context):
    print("DR triggered by CloudWatch Alarm")
    response = drs.describe_recovery_instances(
        filters={'sourceServerIDs': [SOURCE_SERVER_ID]}
    )
    for ri in response['items']:
        if ri['recoveryInstanceProperties']['state'] != 'LAUNCHED':
            # Thực hiện launch
            drs.start_recovery_instance_launch(
                recoveryInstanceID=ri['recoveryInstanceID']
            )
            print(f"Launching recovery instance {ri['recoveryInstanceID']}")
            time.sleep(30)
            return {"status": "Launch initiated", "recoveryInstanceID": ri['recoveryInstanceID']}
    return {"status": "No eligible recovery instance found"}
