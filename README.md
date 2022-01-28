# Locust Spanner: Locust Custom User For Cloud Spanner

Locust is an open source load testing tool.
https://locust.io/

Locust has a client for HTTP requests by default, which makes it easy to write load tests, but to send other requests, customization is required.

locust_spanner is a library that makes it easy to write requests to the Cloud Spanner database.

# Setup

```
pip install git+https://github.com/tomoemon/locust_spanner.git
```

# Usage

1. Write a locustfile using locust_spanner

```python
# sample.py
from locust import task
from locust_spanner import User


class QueryUser(User):
    @task
    def count(self):
        self.client.query("SELECT COUNT(*) FROM MyTable", name="count")

    @task
    def single(self):
        self.client.query('SELECT 1 FROM MyTable WHERE UserID="test"', name="single")
```

2. Run the script

```shell
locust --host projects/my-project/instances/my-instance/databases/my-database \
  -f sample.py \
  --users 1 \
  --spawn-rate 1 \
  --run-time 10s \
  --headless --print-stats
```
