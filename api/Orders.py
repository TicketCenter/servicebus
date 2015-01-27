from django.http import HttpResponse

from api.connectors.OrdersConnector import OrdersConnector

# TODO: Redirect POST, PUT and DELETE requests
class Orders(OrdersConnector):
    def __init__(self):
        OrdersConnector.__init__(self)

    def post_order_unregistered_user(self, request):
        return HttpResponse(self.connected_post_order_unregistered_user(request.GET.get('api_key', '')),
                            content_type='application/json')

    def order_registered_user(self, request, user_id, token):
        if request.method == 'POST':
            return self.post_order_registered_user(request, user_id, token)
        elif request.method == 'GET':
            return self.get_orders_registered_user(request, user_id, token)

    def post_order_registered_user(self, request, user_id, token):
        return HttpResponse(self.connected_post_order_registered_user(request.GET.get('api_key', ''),
                                                         user_id,
                                                         token),
                            content_type='application/json')

    def get_orders_registered_user(self, request, user_id, token):
        return HttpResponse(self.connected_get_orders_registered_user(request.GET.get('api_key', ''),
                                                         user_id,
                                                         token),
                            content_type='application/json')

    def get_order_registered_user(self, request, user_id, token, order_id):
        return HttpResponse(self.connected_get_order_registered_user(request.GET.get('api_key', ''),
                                                         user_id,
                                                         token,
                                                         order_id),
                            content_type='application/json')
