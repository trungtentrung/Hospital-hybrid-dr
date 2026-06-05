#!/bin/bash
INSTANCE_ID="on-prem-vm"
aws cloudwatch put-metric-data \
  --namespace "HospitalDR" \
  --metric-name "Heartbeat" \
  --value 1 \
  --dimensions "InstanceId=$INSTANCE_ID" \
  --region ap-southeast-1
