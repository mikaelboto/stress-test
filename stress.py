from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1,5)

    @task
    def page(self):
        self.client.get("/teste")
