from api.services.ArtistService import ArtistService
from api.connectors.BaseConnector import BaseConnector

class ConcertsConnector(BaseConnector):
    artistService = ArtistService()

    def __init__(self):
        BaseConnector.__init__(self)

    def get_concerts(self, api_key, location, artist, page_size, page_number):
        return self.connect(api_key, self.http.request('GET', self.artistService.api_url() + 'concerts' + '?api_key=' + self.artistService.api_key() + '&location=' + location + '&artist=' + artist + '&page_size=' + page_size + '&page_number=' + page_number).data)

    def get_concert(self, api_key, id):
        return self.connect(api_key, self.http.request('GET', self.artistService.api_url() + 'concerts/' + id + '?api_key=' + self.artistService.api_key().data))
