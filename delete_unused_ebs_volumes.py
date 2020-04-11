# The script can be scheduled and will help remove unutilized resources and eventually save money
# If there is an important volume, you should create a backup with a snapshot. 
# You can also assign a special tag for the volume, such as “DND” (Do Not Delete).
# The script will filter out the volumes with the “DND” tag and delete the rest

# Link to the blog for this: https://medium.com/@keniya.bhavya/how-to-detect-and-delete-unused-aws-ebs-volumes-using-a-lambda-function-and-cloudwatch-6a5fdb08c730?source=friends_link&sk=e8bad0ef2fbffd899f988d039b374a05

#!/usr/bin/python
# -*- coding: utf-8 -*-
import boto3
ec2 = boto3.resource('ec2', region_name='ap-south-1')


def lambda_handler(event, context):
    for vol in ec2.volumes.all():
        if vol.state == 'available':
            if vol.tags is None:
                vid = vol.id
                v = ec2.Volume(vol.id)
                v.delete()
                print 'Deleted ' + vid
        continue
        for tag in vol.tags:
            if tag['Key'] == 'Name':
                value = tag['Value']
                if value != 'DND' and vol.state == 'available':
                    vid = vol.id
                    v = ec2.Volume(vol.id)
                    v.delete()
                    print 'Deleted ' + vid
