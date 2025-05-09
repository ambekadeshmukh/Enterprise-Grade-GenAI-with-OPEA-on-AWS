#!/bin/bash
set -e

echo "Deploying complete OPEA ChatQnA implementation with all customizations..."
kubectl apply -k kubernetes/overlays/prod/

echo "Waiting for components to be ready..."
kubectl wait --for=condition=available --timeout=300s deployment -n opea-chatqna --all

echo "Complete implementation successfully deployed!"

# Print access URLs
UI_URL=$(kubectl get service ui -n opea-chatqna -o jsonpath='{.status.loadBalancer.ingress[0].hostname}')
GRAFANA_URL=$(kubectl get service grafana -n opea-chatqna -o jsonpath='{.status.loadBalancer.ingress[0].hostname}')

echo "ChatQnA UI available at: http://$UI_URL"
echo "Grafana dashboard available at: http://$GRAFANA_URL (admin/admin)"