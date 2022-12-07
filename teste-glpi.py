import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def tickets(self):
        self.client.get("/front/ticket.php")

    def on_start(self):
        self.client.post("/front/login.php", auth=("glpi", "glpi"))
