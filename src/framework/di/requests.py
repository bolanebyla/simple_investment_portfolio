from dishka import Container
from rest_framework.request import Request


class DiRequest(Request):
    container: Container
