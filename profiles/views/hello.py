from django.http.request import HttpRequest
from django.http.response import JsonResponse


def hello_view(request: HttpRequest):
    print(f"request.body: {request.body}")

    response = {"message": "Hello World!"}
    return JsonResponse(response)
