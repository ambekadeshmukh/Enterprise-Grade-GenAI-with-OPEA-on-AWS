#!/bin/bash
set -e

echo "Deploying OPEA ChatQnA with AWS Bedrock..."
kubectl apply -k kubernetes/overlays/bedrock/

echo "Waiting for components to be ready..."
kubectl wait --for=condition=available --timeout=300s deployment -n opea-chatqna --all

echo "AWS Bedrock integration successfully deployed!"