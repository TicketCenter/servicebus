import urllib3

__author__ = 'Nils'

class Reader():
    def __init__(self):
        pass

    @staticmethod
    def read(verb, url):
        http = urllib3.PoolManager()

        return http.request(verb, url).data

    # TODO: buildUrlParameters
