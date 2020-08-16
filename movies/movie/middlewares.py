from .models import Counter

class Requestcounter:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if(response.status_code == 200):
            Counter.objects.create(status = response.status_code)
        return response