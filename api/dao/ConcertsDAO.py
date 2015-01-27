from api.resources.ArtistService import ArtistService
from api.dao.BaseDAO import BaseDAO
__author__ = 'Nils'

class ConcertsDAO(BaseDAO):
    artistService = ArtistService()

    def __init__(self):
        BaseDAO.__init__(self)

    def concerts(self, api_key, location, page_size, page_number):
        if self.authenticate(api_key):
            return self.artistService.get('GET', 'concerts', '&location=' + location + '&page_size=' + page_size + '&page_number=' + page_number)

    def concert(self, api_key, id):
        if self.authenticate(api_key):
            return self.artistService.get('GET', 'concerts/' + id)
