from api.resources.utils.Reader import Reader

class ArtistService(Reader):
    __API_URL = 'http://artistservice.ticketcenter.hanze.nberlijn.nl/api/'
    __API_KEY = 'pz76SUD2HE36689AMzF0A2m9pZrk2fUZ'

    def __init__(self):
        Reader.__init__(self)

    def get(self, verb, resource, parameters=None):
        return self.read(verb, self.__API_URL + resource + '?api_key=' + self.__API_KEY + parameters)
