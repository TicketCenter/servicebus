from django.http import HttpResponse

from api.connectors.UsersConnector import UsersConnector

"""
@class      Users
@author     Nils Berlijn
@version    1.0
@since      1.0
"""
# TODO: Redirect POST, PUT and DELETE requests
class Users(UsersConnector):
    def __init__(self):
        UsersConnector.__init__(self)

    def post_user(self, request):
        return HttpResponse(self.connected_post_user(request.GET.get('api_key', '')),
                            content_type='application/json')

    def post_user_login(self, request):
        return HttpResponse(self.connected_post_user_login(request.GET.get('api_key', '')),
                            content_type='application/json')

    def user_info(self, request, id, token):
        if request.method == 'GET':
            return self.get_user(request, id, token)
        elif request.method == 'PUT':
            return self.put_user(request, id, token)
        elif request.method == 'DELETE':
            return self.delete_user(request, id, token)

    def get_user(self, request, id, token):
        return HttpResponse(self.connected_get_user(request.GET.get('api_key', ''),
                                                    id,
                                                    token),
                            content_type='application/json')

    def put_user(self, request, id, token):
        return HttpResponse(self.connected_put_user(request.GET.get('api_key', ''),
                                                    id,
                                                    token),
                            content_type='application/json')

    def delete_user(self, request, id, token):
        return HttpResponse(self.connected_delete_user(request.GET.get('api_key', ''),
                                                       id,
                                                       token),
                            content_type='application/json')
