#!/bin/bash
set -e

STACK_NAME="opea-chatqna-infra"
REGION="us-east-1"
CLUSTER_NAME="opea-chatqna"

echo "Deploying CloudFormation stack: $STACK_NAME"
aws cloudformation create-stack \
  --stack-name $STACK_NAME \
  --template-body file://infrastructure/cloudformation/eks-cluster.yaml \
  --capabilities CAPABILITY_IAM \
  --region $REGION

echo "Waiting for stack creation to complete..."
aws cloudformation wait stack-create-complete \
  --stack-name $STACK_NAME \
  --region $REGION

echo "Getting cluster info..."
aws eks update-kubeconfig --name $CLUSTER_NAME --region $REGION

echo "Verifying connection to cluster..."
kubectl get nodes

echo "Infrastructure deployment completed successfully!"