#!/bin/bash
set -e

echo "Deploying OPEA ChatQnA with OpenSearch..."
kubectl apply -k kubernetes/overlays/opensearch/

echo "Waiting for components to be ready..."
kubectl wait --for=condition=available --timeout=300s deployment -n opea-chatqna --all

echo "OpenSearch successfully deployed!"