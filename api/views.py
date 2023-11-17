import json

from django.shortcuts import render
from django.http import JsonResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .classifier import prep_model, classify_image, base64_to_PILImage
from .models import Image

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from .serializers import ImageBase64Serilizer, ClassifiedImageSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def classify(request):
    if request.method == 'POST':
        data = request.data
        serializer = ImageBase64Serilizer(data=data)
        if serializer.is_valid():
            img = base64_to_PILImage(request.data.get('image'))
            # serializer.save()
            classified = classify_image(img)
            return Response(classified)
            # print(classified)
            # classified_serializer = ClassifiedImageSerializer(data=classified)
            # if classified_serializer.is_valid():
            #     return Response(classified_serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=400)
    