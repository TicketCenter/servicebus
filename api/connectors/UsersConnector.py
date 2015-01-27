from api.services.TicketService import TicketService
from api.connectors.BaseConnector import BaseConnector

"""
@class      UsersConnector
@author     Nils Berlijn
@version    1.0
@since      1.0
"""
# TODO: Redirect POST, PUT and DELETE requests
class UsersConnector(BaseConnector, TicketService):
    def __init__(self):
        BaseConnector.__init__(self)
        TicketService.__init__(self)

    def connected_post_user(self, api_key):
        return self.connect(api_key, self.http.request('POST',
                                                       self.api_url() + 'users'))

    def connected_post_user_login(self, api_key):
        return self.connect(api_key, self.http.request('POST',
                                                       self.api_url() + 'users/login'))

    def connected_get_user(self, api_key, id, token):
        return self.connect(api_key, self.http.request('POST',
                                                       self.api_url() + 'users/' + id + '/' + token))

    def connected_put_user(self, api_key, id, token):
        return self.connect(api_key, self.http.request('PUT',
                                                       self.api_url() + 'users/' + id + '/' + token))

    def connected_delete_user(self, api_key, id, token):
        return self.connect(api_key, self.http.request('DELETE',
                                                       self.api_url() + 'users/' + id + '/' + token))
