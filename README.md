# Locust Custom User For Cloud Spanner

locust spanner user makes query benchmark testing easier.

# Setup

```
pip install git+https://github.com/tomoemon/locust_spanner.git
```

# Usage

```python
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
