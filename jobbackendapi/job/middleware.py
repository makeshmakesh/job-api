#pylint:disable=all


class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("Request", getattr(request, 'body', request))

        response = self.get_response(request)
        print("Response", getattr(response, 'data', response))

        return response