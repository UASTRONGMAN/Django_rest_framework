from rest_framework.views import APIView
from rest_framework.response import Response

class UsersApp(APIView):
    def get(self, *args, **kwargs):
        return Response('Hello, its get method')
    def post(self, *args, **kwargs):
        data = self.request.data
        return Response(data)


class UsersAppRetrive(APIView):
    def put(self, *args, **kwargs):
        pk = kwargs['pk']
        return Response('Hello, its put method')
    def patch(self, *args, **kwargs):
        return Response('Hello, its patch method')
    def delete(self, *args, **kwargs):
        return Response('Hello, its delete method')