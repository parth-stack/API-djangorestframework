# from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view

from .models import Product
from .serializers import ProductSerializer



from django.db import connection
def count_stock():
        with connection.cursor() as cursor:
            cursor.execute("SELECT SUM(pd_count) FROM api_product")
            row = cursor.fetchone()
        return row



@api_view(['GET','POST'])
@csrf_exempt
def insert(request):
    """
    List all Products by GET , or create a new by POST JSON(application/json) {"pd_name": "cotton saree" , "pd_type": "sarree" , "pd_cost": "4000" , "pd_count": "0"}
    """
    if request.method == 'GET':
        p = Product.objects.all()
        serializer = ProductSerializer(p, many=True)
        return Response(serializer.data,status=200)

    elif request.method == 'POST':
        # data = JSONParser().parse(request.data)
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET'])
@csrf_exempt
def display(request,product):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        p = Product.objects.filter(pd_name=product)
    except Product.DoesNotExist:
        return Response(status=404)
    
    if request.method == 'GET':
        serializer = ProductSerializer(p, many=True)
        data = serializer.data
        data = [{'STOCK PILE':str(count_stock()[0])}] + data
        return Response(data,status=200)