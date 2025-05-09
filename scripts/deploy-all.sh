#!/bin/bash
set -e

STACK_NAME="opea-chatqna-infra"
REGION="us-east-1"
CLUSTER_NAME="opea-chatqna"

# Install dependencies for sample data generation
pip install -r sample-data/requirements.txt

# Generate sample data
python sample-data/generate_samples.py

echo "Deploying infrastructure..."
./scripts/deploy-infrastructure.sh

echo "Waiting for cluster to be ready..."
sleep 60

echo "Deploying base OPEA ChatQnA application..."
kubectl apply -k kubernetes/base/

echo "Waiting for base components to be ready..."
kubectl wait --for=condition=available --timeout=300s deployment -n opea-chatqna --all

echo "Deploying monitoring tools..."
kubectl apply -k monitoring/

echo "All components deployed successfully!"

# Print access URLs
UI_URL=$(kubectl get service ui -n opea-chatqna -o jsonpath='{.status.loadBalancer.ingress[0].hostname}')
GRAFANA_URL=$(kubectl get service grafana -n opea-chatqna -o jsonpath='{.status.loadBalancer.ingress[0].hostname}')

echo "ChatQnA UI available at: http://$UI_URL"
echo "Grafana dashboard available at: http://$GRAFANA_URL (admin/admin)"