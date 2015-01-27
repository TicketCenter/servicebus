from django.http import HttpResponse

from api.connectors.ConcertsConnector import ConcertsConnector

class Concerts():
    concertsConnector = ConcertsConnector()

    def __init__(self):
        pass

    def get_concerts(self, request):
        return HttpResponse(self.concertsConnector.get_concerts(request.GET.get('api_key', ''),
                                              request.GET.get('location', ''),
                                              request.GET.get('artist', ''),
                                              request.GET.get('page_size', ''),
                                              request.GET.get('page_number', '')),
                            content_type='application/json')

    def get_concert(self, request, concert_id):
        return HttpResponse(self.concertsConnector.get_concert(request.GET.get('api_key', ''),
                                             concert_id),
                            content_type='application/json')
