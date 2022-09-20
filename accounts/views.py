# Rest Framework Imports
from rest_framework import status, views, permissions
from rest_framework.request import Request
from rest_framework.response import Response

# YASG Imports
from drf_yasg.utils import swagger_auto_schema

# Payload Imports
from rest_api_payload import success_response, error_response

# Own Imports
from accounts.serializers import (
    RegisterUserSerializer,
    UserSerializer
)
from accounts.models import User



class RegisterUserAPIView(views.APIView):
    serializer_class = RegisterUserSerializer
    permission_classes = (permissions.AllowAny, )
    
    @swagger_auto_schema(request_body=serializer_class)
    def post(self, request:Request) -> Response:
        """
        This function takes in a request object, 
        validates the data in the request object, saves the
        data if it's valid, and returns a response object
        
        :param request: This is the request object that is sent to the view
        :type request: Request
        :return: A response object.
        """
        
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            payload = success_response(
                status=True, message="User created successfully.",
                data=serializer.data
            )
            return Response(data=payload, status=status.HTTP_201_CREATED)
        
        else:
            payload = error_response(
                status=False,
                message=serializer.errors
            )
            return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)
        

class UpdateUserInformationAPIView(views.APIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, )
    
    def get_user(self, request:Request) -> User:
        """
        It returns a user object if the user exists, 
        otherwise it raises an exception
        
        :param email: The email of the user you want to get
        :type email: str
        :return: The user object is being returned.
        """
        try:
            user = User.objects.filter(email=request.user.email).first()
            return user
        except (User.DoesNotExist):
            raise Exception("User does not exist!")
            
    
    def get(self, request:Request) -> Response:
        """
        This function gets a user and 
        returns a serialized version of the user
        
        :param request: The request object
        :type request: Request
        :return: A Response object with the payload and status code.
        """
        user = self.get_user(request=request)
        serializer = self.serializer_class(user)
        
        payload = success_response(
            status=True,
            message="User retrieved successfully.",
            data=serializer.data
        )
        return Response(data=payload, status=status.HTTP_200_OK)
    
    def put(self, request:Request) -> Response:
        """
        It updates the user's information.
        
        :param request: The request object
        :type request: Request
        :return: A response object.
        """
        user = self.get_user(request=request)
        serializer = self.serializer_class(instance=user, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            
            payload = success_response(
                status=True,
                message="User update successfully.",
                data=serializer.data
            )
            return Response(data=payload, status=status.HTTP_202_ACCEPTED)
        
        else:
            payload = error_response(
                status=False,
                message=serializer.errors
            )
            return Response(data=payload, status=status.HTTP_400_BAD_REQUEST)