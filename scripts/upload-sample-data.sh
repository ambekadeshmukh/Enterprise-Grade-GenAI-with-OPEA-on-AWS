#!/bin/bash
set -e

GATEWAY_URL=$(kubectl get service gateway -n opea-chatqna -o jsonpath='{.status.loadBalancer.ingress[0].hostname}')
if [ -z "$GATEWAY_URL" ]; then
  GATEWAY_URL=$(kubectl get service gateway -n opea-chatqna -o jsonpath='{.spec.clusterIP}')
fi

echo "Uploading sample documents to the ChatQnA application..."

for file in sample-data/documents/*.md; do
  if [[ "$file" != *"metadata.json" ]]; then
    echo "Uploading $file..."
    CONTENT=$(cat "$file" | sed 's/"/\\"/g' | sed ':a;N;$!ba;s/\n/\\n/g')
    
    curl -X POST "http://$GATEWAY_URL:8888/v1/chatqna" \
      -H "Content-Type: application/json" \
      -d "{
        \"messages\": [],
        \"documents\": [
          {
            \"content\": \"$CONTENT\",
            \"metadata\": {
              \"source\": \"$file\"
            }
          }
        ]
      }"
    echo ""
  fi
done

echo "Sample documents uploaded successfully!"