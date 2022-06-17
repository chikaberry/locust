from locust import HttpUser, between, task

class WebsiteUser(HttpUser):
    wait_time = between(5,15)

    def on_start(self):
        print("starting on login test....")

    @task
    def index(self):
        self.client.get("/")
