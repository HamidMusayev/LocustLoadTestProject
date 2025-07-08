# Locust Load Test Project

This project uses [Locust](https://locust.io/) to test the performance of the `/api/Auth/login` endpoint.

## Requirements

- Python 3.7 or higher
- Locust

Install Locust:

```bash
pip install locust
````

## How to Run

1. Open a terminal and run:

```bash
locust -f locustfile.py 
```
or just
```bash
locust
```

2. Open your browser and go to:

```
http://localhost:8089
```

3. Fill in:

* Number of users (e.g. 100)
* Spawn rate (e.g. 10)
* Click **Start swarming**

## Notes

* The tested endpoint is:

```
POST https://localhost:7086/api/Auth/login
```

* SSL verification is disabled (for localhost use).
