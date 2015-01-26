from django.http import HttpResponse

__author__ = 'Nils'

class Concerts():
    def __init__(self):
        pass

    @staticmethod
    def concerts(request):
        return HttpResponse('ALL CONCERTS ' +
                            request.GET.get('location', '') +
                            request.GET.get('page_size', '') +
                            request.GET.get('page_number', '')
        )

    # noinspection PyUnusedLocal
    @staticmethod
    def concert(request, concert_id):
        return HttpResponse('ONE CONCERT ' + concert_id)
