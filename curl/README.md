# Curl

## Submit a Job:

```shell
curl -X POST "https://api.ionq.co/v0.3/jobs" \
  -H "Authorization: apiKey $IONQ_API_KEY" \
  -H "Content-Type: application/json" \
  -d @data.json
```

> {"id":"46ce01e7-689c-49c8-893d-64948d2a1381","status":"ready","request":1691434240}

## Query a Job:

```shell
curl "https://api.ionq.co/v0.3/jobs/46ce01e7-689c-49c8-893d-64948d2a1381" \
  -H "Authorization: apiKey $IONQ_API_KEY"
```

> {"noise":{"model":"ideal"},"status":"completed","children":[],"target":"simulator","predicted_execution_time":4,"execution_time":46,"id":"46ce01e7-689c-49c8-893d-64948d2a1381","qubits":2,"request":1691434240,"start":1691434242,"response":1691434242,"gate_counts":{"1q":1,"2q":1},"results_url":"/v0.3/jobs/46ce01e7-689c-49c8-893d-64948d2a1381/results"}

## Get Job Results:

```shell
curl "https://api.ionq.co/v0.3/jobs/46ce01e7-689c-49c8-893d-64948d2a1381/results" \
  -H "Authorization: apiKey $IONQ_API_KEY"
```

> {"0":0.500000000,"3":0.500000000}
