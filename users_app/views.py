from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from users_app.models import UserModel
from django.forms import model_to_dict


class UsersApp(APIView):

    def get(self, *args, **kwargs):
        users = UserModel.objects.all()
        users = [model_to_dict(user) for user in users]
        return Response(users)

    def post(self, *args, **kwargs):
        data = self.request.data
        user = UserModel.objects.create(**data)
        return Response(model_to_dict(user))


class UsersAppRetrive(APIView):

    def get(self, *args, **kwargs):
        pk = kwargs['pk']
        try:
            user = UserModel.objects.get(pk=pk)
        except UserModel.DoesNotExist:
            return Response('not found', status=status.HTTP_404_NOT_FOUND)

        return Response(model_to_dict(user), status=status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        pk = kwargs['pk']
        data = self.request.data
        try:
            user = UserModel.objects.get(pk=pk)
        except UserModel.DoesNotExist:
            return Response('not found', status=status.HTTP_404_NOT_FOUND)
        user.name = data['name']
        user.age = data['age']
        user.gender = data['gender']
        user.save()
        return Response(model_to_dict(user), status=status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        return Response('Hello, its patch method')

    def delete(self, *args, **kwargs):
        pk = kwargs['pk']
        try:
            UserModel.objects.get(pk=pk).delete()
        except UserModel.DoesNotExist:
            return Response('not found', status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)