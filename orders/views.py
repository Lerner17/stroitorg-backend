import html

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status

from .models import Order, OrderProduct


class OrderAPIView(APIView):

    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        data = {
            'first_name': html.escape(request.data.get('first_name')),
            'phone': html.escape(request.data.get('phone'))
        }
        cart = request.data.get('items')
        print(data, cart)

        if data and cart:
            order = Order.objects.create(**data)
            for item in cart:
                OrderProduct.objects.create(
                    order=order, product_id=item['id'], quantity=item['quantity'])

        return Response(status=status.HTTP_200_OK)
