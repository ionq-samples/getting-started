# API

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ionq-samples/getting-started/blob/main/api/main.ipynb)

---

Get your API key from <https://cloud.ionq.com/settings/keys>.

## Submit a Job:

```shell
curl -X POST "https://api.ionq.co/v0.3/jobs" \
  -H "Authorization: apiKey $IONQ_API_KEY" \
  -H "Content-Type: application/json" \
  -d @data.json
```

> {"id":"7cc8ce51-2e57-4140-96ce-cf8bada0bf91","status":"ready","request":1691469978}

Use `id` to query the job.

## Query a Job:

```shell
curl "https://api.ionq.co/v0.3/jobs/7cc8ce51-2e57-4140-96ce-cf8bada0bf91" \
  -H "Authorization: apiKey $IONQ_API_KEY"
```

> {"noise":{"model":"ideal"},"status":"submitted","children":[],"target":"simulator","id":"7cc8ce51-2e57-4140-96ce-cf8bada0bf91","request":1691469978}

> {"noise":{"model":"ideal"},"status":"completed","children":[],"target":"simulator","predicted_execution_time":4,"execution_time":26,"id":"7cc8ce51-2e57-4140-96ce-cf8bada0bf91","qubits":2,"request":1691469978,"start":1691469979,"response":1691469979,"gate_counts":{"1q":1,"2q":1},"results_url":"/v0.3/jobs/7cc8ce51-2e57-4140-96ce-cf8bada0bf91/results"}

When `status` becomes `completed`, get the job results.

## Get Job Results:

```shell
curl "https://api.ionq.co/v0.3/jobs/7cc8ce51-2e57-4140-96ce-cf8bada0bf91/results" \
  -H "Authorization: apiKey $IONQ_API_KEY"
```

> {"0":0.500000000,"3":0.500000000}
