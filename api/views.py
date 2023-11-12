from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .classifier import prep_model, classify

@api_view(['GET'])
def classify(request, imgstring):
    if request.method == 'GET':
        inference_model = prep_model()
        classified = classify(imgstring, inference_model)

        return Response(classified, status=status.HTTP_200_OK)