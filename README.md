# Locust Custom User For Cloud Spanner

locust spanner user makes query benchmark testing easier.

# Setup

```
pip install git+https://github.com/tomoemon/locust_spanner.git
```

# Usage

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

```shell
locust --host projects/my-project/instances/my-instance/databases/my-database \
  -f sample.py \
  --users 1 \
  --spawn-rate 1 \
  --run-time 10s \
  --headless --print-stats
```
