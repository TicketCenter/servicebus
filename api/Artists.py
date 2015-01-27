from django.http import HttpResponse

from api.connectors.ArtistsConnector import ArtistsConnector

class Artists(ArtistsConnector):
    def __init__(self):
        ArtistsConnector.__init__(self)

    def get_artists(self, request):
        return HttpResponse(self.get_connected_artists(request.GET.get('api_key', ''),
                                              request.GET.get('characters', 'a'),
                                              request.GET.get('page_size', ''),
                                              request.GET.get('page_number', '')),
                            content_type='application/json')

    def get_artist(self, request, name):
        return HttpResponse(self.get_connected_artist(request.GET.get('api_key', ''),
                                             name),
                            content_type='application/json')