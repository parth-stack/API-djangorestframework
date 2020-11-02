from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.serializers import UserSerializer
from django.contrib.auth.models import User

class UserRegister(APIView):
    """ 
    Creates the user. 
    """
    def get(self, request, format='json'):
        return Response('''Enter your query in json format Ex : {"username": "foobar","email": "foobarbaz@example.com","password": "foo"}''')        

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class UserLogin(APIView):
    """ 
    Logins the user. 
    """
    def get(self, request, format='json'):
        return Response('''Enter your query in json format Ex : {'username':'foobar','password':'foo'}''')

    def post(self, request, format='json'):
        serializer = UserSerializer()
        user = serializer.ask(data=request.data)
        print(user)
        if user:
            return Response('Logedin', status=status.HTTP_201_CREATED)
        else:
            return Response('Not Registered', status=status.HTTP_201_CREATED)