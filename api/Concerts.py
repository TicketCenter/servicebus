from django.http import HttpResponse

from api.dao.ConcertsDAO import ConcertsDAO

class Concerts():
    dao = ConcertsDAO()

    def __init__(self):
        pass

    def concerts(self, request):
        return HttpResponse(self.dao.concerts(request.GET.get('api_key', ''),
                                              request.GET.get('location', ''),
                                              request.GET.get('page_size', ''),
                                              request.GET.get('page_number', '')),
                            content_type='application/json')

    def concert(self, request, concert_id):
        return HttpResponse(self.dao.concert(request.GET.get('api_key', ''),
                                             concert_id),
                            content_type='application/json')
