from api.config.API import API

class BaseDAO():
    api = API()

    def __init__(self):
        pass

    def authenticate(self, api_key):
        if api_key == self.api.api_key():
            return True
        else:
            return False
