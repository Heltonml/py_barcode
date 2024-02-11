from src.views.http_types.http_response import HttpReponse

def handle_errors(error: Exception) -> HttpReponse:
    return HttpReponse(
        status_code=500,
        body={
            "errors": [{
                "title": "Server Error!",
                "detail": str(error)
            }]
        }
    )
