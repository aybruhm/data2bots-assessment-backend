# Rest Framework Imports
from rest_framework import status, views, permissions
from rest_framework.request import Request
from rest_framework.response import Response

# YASG Imports
from drf_yasg.utils import swagger_auto_schema

# Payload Imports
from rest_api_payload import success_response, error_response

# Own Imports
from accounts.serializers import OrderSerializer
from accounts.models import Order


class UserOrdersAPIView(views.APIView):
    serializer_class = OrderSerializer
    permission_classes = (permissions.IsAuthenticated, )
    
    @swagger_auto_schema(request_body=serializer_class)
    def post(self, request:Request) -> Response:
        """
        This function serializes the logged-in user orders
        and returns a response object
        
        :param request: This is the request object that is sent to the view
        :type request: Request
        :return: A response object.
        """
        orders = Order.objects.prefetch_related("user").filter(user=request.user)
        serializer = self.serializer_class(orders, many=True)
        
        payload = success_response(
            status=True,
            messagge="User orders retrieved!",
            data=serializer.data
        )
        return Response(data=payload, status=status.HTTP_200_OK)