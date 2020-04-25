from locust import HttpLocust, TaskSet, task, between
import os
from os.path import join, dirname
from dotenv import load_dotenv

def load_environment_variables():
    dotenv_path = join(dirname(__file__), '.load_env')
    load_dotenv(dotenv_path)

def read_environment_variables(self):
    self.api_key = os.environ.get("API_KEY")
    self.authorization = os.environ.get("API_AUTHORIZATION")
    self.api_domain =os.environ.get('API_DOMAIN')

def api(self):
    headers = {
        "apikey": self.api_key,
        "Authorization": self.authorization
    }
    self.client.get("/api/users", headers = headers)

def get_another_apis(self):
    self.client.get("/another_api")

def get_another_api(self):
    self.client.get("/another_api/1")

def stop(l):
    print('Load testing done!')


class UserBehavior(TaskSet):

    def on_start(self):
        read_environment_variables(self)

#   Task’s execution ratio between api_tasks to another_api_tasks is set to 8:1
    @task(8)
    def api_tasks(self):
        api(self)

    @task(1)
    def another_api_tasks(self):
        get_another_apis(self)
        get_another_api(self)
    
    def on_stop(self):
        stop(self)

class APIUser(HttpLocust):
    
    load_environment_variables()
    host = os.environ.get('API_DOMAIN')
    task_set = UserBehavior
#   Stimulated api users wait a random time between a min and max value(in seconds) after each task execution. 
    wait_time = between(5.0, 9.0)
