from framework.di import DiRequest, container


class ProvideDiContainerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: DiRequest):
        with container() as request_container:
            request.container = request_container
            response = self.get_response(request)
        return response
