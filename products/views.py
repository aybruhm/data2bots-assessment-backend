# Rest Framework Imports
from rest_framework import status, views, permissions
from rest_framework.request import Request
from rest_framework.response import Response

# Payload Imports
from rest_api_payload import success_response

# Own Imports
from products.serializers import OrderSerializer
from products.models import Order


class UserOrdersAPIView(views.APIView):
    serializer_class = OrderSerializer
    permission_classes = (permissions.IsAuthenticated, )
    
    def get(self, request:Request) -> Response:
        """
        This function serializes the orders related to the logged-in user
        and returns a response object
        
        :param request: This is the request object that is sent to the view
        :type request: Request
        :return: A response object.
        """
        orders = Order.objects.prefetch_related("user").filter(user=request.user)
        serializer = self.serializer_class(orders, many=True)
        
        payload = success_response(
            status=True,
            message="User orders retrieved!",
            data=serializer.data
        )
        return Response(data=payload, status=status.HTTP_200_OK)