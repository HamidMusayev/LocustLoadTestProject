from locust import HttpUser, task, between

class AuthUser(HttpUser):
    wait_time = between(1, 2)  # simulate realistic delay between requests
    host = "https://localhost:7086"  # Set the host here

    def on_start(self):
        self.client.verify = False  # Disable SSL verification (for local dev)

    @task
    def login(self):
        payload = {
            "email": "test@gmail.com",
            "password": "N123456n!"
        }
        headers = {
            "accept": "text/plain",
            "Content-Type": "application/json"
        }

        with self.client.post(
            "/api/Auth/login",
            json=payload,
            headers=headers,
            catch_response=True
        ) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Unexpected status code: {response.status_code}")

    @task
    def get_form_instance_home(self):
        headers = {
            "accept": "*/*",
            "Authorization": "<YOUR-TOKEN>"
        }
        with self.client.get(
            "/api/FormInstance/home?sortType=NameIncrease",
            headers=headers,
            catch_response=True
        ) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Unexpected status code: {response.status_code}")

