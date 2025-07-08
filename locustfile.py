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

'''
    @task
    def login_and_get_form_instance_home(self):
        # Step 1: Login and get token
        payload = {
            "email": self.email,
            "password": self.password
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
        ) as login_response:
            if login_response.status_code == 200:
                try:
                    token = login_response.json().get("token")
                except Exception as e:
                    login_response.failure(f"Failed to parse token: {e}")
                    return
                if not token:
                    login_response.failure("No token found in login response")
                    return
                login_response.success()
            else:
                login_response.failure(f"Unexpected status code: {login_response.status_code}")
                return

        # Step 2: Use token to call get_form_instance_home
        headers = {
            "accept": "*/*",
            "Authorization": f"Bearer {token}"
        }
        with self.client.get(
            "/api/FormInstance/home?sortType=NameIncrease",
            headers=headers,
            catch_response=True
        ) as response:
            if response.status_code == 200:
                response.success()
                response.success()
            else:
                response.failure(f"Unexpected status code: {response.status_code}")

'''
