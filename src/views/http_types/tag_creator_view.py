from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpReponse

class TagCreatorView:
    '''
        responsability for interaction with Http
    '''
    def validate_and_create(self, http_request: HttpRequest) -> HttpReponse:
        body = http_request.body
        product_code = body['product_code']
        print(product_code)
        # add user_case
        return HttpReponse(200, body={"result": "success!!!"})
