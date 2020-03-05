from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.

class test_view(APIView):
    """
    Test view.
    """

    def get(self, request):
        return Response({'error': None, 'data': 'Success GET!'})

    def post(self, request):
        return Response({'error': None, 'data': 'Success POST!'})
