from api.services.TicketService import TicketService
from api.connectors.BaseConnector import BaseConnector

# TODO: Redirect POST, PUT and DELETE requests
class OrdersConnector(BaseConnector, TicketService):
    def __init__(self):
        BaseConnector.__init__(self)
        TicketService.__init__(self)

    def connected_post_order_unregistered_user(self, api_key):
        return self.connect(api_key, self.http.request('POST', self.api_url() + 'orders'))

    def connected_post_order_registered_user(self, api_key, user_id, token):
        return self.connect(api_key, self.http.request('POST', self.api_url() + 'orders/' + user_id + '/' + token))

    def connected_get_orders_registered_user(self, api_key, user_id, token):
        return self.connect(api_key, self.http.request('GET', self.api_url() + 'orders/' + user_id + '/' + token))

    def connected_get_order_registered_user(self, api_key, user_id, token, order_id):
        return self.connect(api_key, self.http.request('GET', self.api_url() + 'orders/' + user_id + '/' + token + '/' + order_id))
