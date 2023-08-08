# cURL

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ionq-samples/getting-started/blob/main/curl/main.ipynb)

---

## Submit a Job:

```shell
# Get your API key from https://cloud.ionq.com/settings/keys
curl -X POST "https://api.ionq.co/v0.3/jobs" \
  -A "curl/$(curl --version | awk 'NR==1 {print $2}')" \
  -H "Authorization: apiKey $IONQ_API_KEY" \
  -H "Content-Type: application/json" \
  -d @data.json
```

> {"id":"646b1651-6b64-4f76-a91c-8f2a173fe860","status":"ready","request":1691435811}

## Query a Job:

```shell
curl "https://api.ionq.co/v0.3/jobs/646b1651-6b64-4f76-a91c-8f2a173fe860" \
  -H "Authorization: apiKey $IONQ_API_KEY"
```

> {"noise":{"model":"ideal"},"status":"completed","children":[],"target":"simulator","predicted_execution_time":4,"execution_time":28,"id":"646b1651-6b64-4f76-a91c-8f2a173fe860","qubits":2,"request":1691435811,"start":1691435812,"response":1691435812,"gate_counts":{"1q":1,"2q":1},"results_url":"/v0.3/jobs/646b1651-6b64-4f76-a91c-8f2a173fe860/results"}

## Get Job Results:

```shell
curl "https://api.ionq.co/v0.3/jobs/646b1651-6b64-4f76-a91c-8f2a173fe860/results" \
  -H "Authorization: apiKey $IONQ_API_KEY"
```

> {"0":0.500000000,"3":0.500000000}
