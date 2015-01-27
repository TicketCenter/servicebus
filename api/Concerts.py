from django.http import HttpResponse

from api.connectors.ConcertsConnector import ConcertsConnector

"""
@class      Concerts
@author     Nils Berlijn
@version    1.0
@since      1.0
"""
class Concerts(ConcertsConnector):
    def __init__(self):
        ConcertsConnector.__init__(self)

    def get_concerts(self, request):
        return HttpResponse(self.connected_get_concerts(request.GET.get('api_key', ''),
                                                        request.GET.get('location', ''),
                                                        request.GET.get('artist', ''),
                                                        request.GET.get('page_size', ''),
                                                        request.GET.get('page_number', '')),
                            content_type='application/json')

    def get_concert(self, request, id):
        return HttpResponse(self.connected_get_concert(request.GET.get('api_key', ''),
                                                       id),
                            content_type='application/json')
