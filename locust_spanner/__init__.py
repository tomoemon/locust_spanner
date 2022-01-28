import time

# patch for grpc request from here
# https://github.com/grpc/grpc/issues/4629#issuecomment-376962677
from gevent import monkey

monkey.patch_all()
import grpc.experimental.gevent as grpc_gevent

grpc_gevent.init_gevent()
# patch for grpc request to here
from google.cloud import spanner
import locust


class Client:
    """
    http://docs.locust.io/en/stable/testing-other-systems.html
    """

    def __init__(self, host, request_event):
        """
        :param host: projects/{PROJECT_ID}/instances/{INSTANCE_ID}/databases/{DATABASE}
        :param request_event:
        """
        _, project, _, instance_id, _, database = host.split("/")
        self.database = spanner.Client(project).instance(instance_id).database(database)
        self._request_event = request_event

    def execute(self, sql):
        result = []
        with self.database.snapshot() as snap:
            for row in snap.execute_sql(sql):
                result.append(row)
        return result

    def query(self, sql, *, name=""):
        request_meta = {
            "request_type": "sql",
            "name": name,
            "start_time": time.time(),
            "response_length": 0,
            "response": None,
            "context": {},
            "exception": None,
        }
        start_perf_counter = time.perf_counter()
        try:
            request_meta["response"] = self.execute(sql)
        except Exception as e:
            request_meta["exception"] = e
        request_meta["response_time"] = (
            time.perf_counter() - start_perf_counter
        ) * 1000
        self._request_event.fire(**request_meta)
        return request_meta["response"]


class User(locust.User):
    abstract = True

    def __init__(self, environment):
        super().__init__(environment)
        self.client = Client(self.host, environment.events.request)
