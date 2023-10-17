from http.client import HTTPConnection, HTTPResponse
from json import loads

class ClientAPI:

    def __init__(
            self,
            type: str,
            value: str,
        ) -> int:

        self.host = "www.thecolorapi.com"
        self.url = '/id?{}={}'.format(type, value)
    
    def get(self):
        
        conn: HTTPConnection = HTTPConnection(self.host)
        conn.request("GET",self.url)
        response: HTTPResponse = conn.getresponse()
        
        return loads(response.read().decode())["hex"]["clean"]