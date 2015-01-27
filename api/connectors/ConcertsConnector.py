from api.services.ArtistService import ArtistService
from api.connectors.BaseConnector import BaseConnector

"""
@class      ConcertsConnector
@author     Nils Berlijn
@version    1.0
@since      1.0
"""
class ConcertsConnector(BaseConnector, ArtistService):
    def __init__(self):
        BaseConnector.__init__(self)
        ArtistService.__init__(self)

    def connected_get_concerts(self, api_key, location, artist, page_size, page_number):
        return self.connect(api_key, self.http.request('GET',
                                                       self.api_url() + 'concerts' + '?api_key=' + self.api_key() + '&location=' + location + '&artist=' + artist + '&page_size=' + page_size + '&page_number=' + page_number).data)

    def connected_get_concert(self, api_key, id):
        return self.connect(api_key, self.http.request('GET',
                                                       self.api_url() + 'concerts/' + id + '?api_key=' + self.api_key()).data)
