#!/bin/bash
set -e

STACK_NAME="opea-chatqna-infra"
REGION="us-east-1"
CLUSTER_NAME="opea-chatqna"

echo "Starting cleanup process for OPEA ChatQnA resources..."

# Clean up Kubernetes resources
echo "Removing Kubernetes resources..."
kubectl delete namespace opea-chatqna --ignore-not-found=true

# Delete CloudFormation stack
echo "Deleting CloudFormation stack..."
aws cloudformation delete-stack --stack-name $STACK_NAME --region $REGION

echo "Waiting for stack deletion to complete..."
aws cloudformation wait stack-delete-complete --stack-name $STACK_NAME --region $REGION

echo "Cleanup completed successfully!"
echo "All OPEA ChatQnA resources have been removed from your AWS account."