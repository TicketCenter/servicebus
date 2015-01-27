"""
@class      ArtistService
@author     Nils Berlijn
@version    1.0
@since      1.0
"""
class ArtistService():
    __API_URL = 'http://artistservice.ticketcenter.hanze.nberlijn.nl/api/'
    __API_KEY = 'pz76SUD2HE36689AMzF0A2m9pZrk2fUZ'

    def __init__(self):
        pass

    def api_url(self):
        return self.__API_URL

    def api_key(self):
        return self.__API_KEY
