#!/bin/bash
set -e

echo "Deploying OPEA ChatQnA with Guardrails..."
kubectl apply -k kubernetes/overlays/guardrails/

echo "Waiting for components to be ready..."
kubectl wait --for=condition=available --timeout=300s deployment -n opea-chatqna --all

echo "Guardrails successfully deployed!"