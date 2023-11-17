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
        # req_body = json.loads(request.body.decode('utf-8'))
        data = request.data
        # req_body = json.loads(request.body.decode('utf-8'))
        # print(request.data.get('image'))
        serializer = ImageBase64Serilizer(data=data)
        if serializer.is_valid():
            img = base64_to_PILImage(request.data.get('image'))

            # serializer.save()
            # last = Image.objects.last()
            # inference_model = prep_model()
            # print(req_body)
            classified = classify_image(img)
            return Response(classified)
            print(classified)
            classified_serializer = ClassifiedImageSerializer(data=classified)
            # response = JsonResponse(classified_serializer.data, status=200)
            # return Response(request.data.get('image'), status=status.HTTP_200_OK)
            # response_data = serializer()
            # return Response(serializer.data, status=status.HTTP_200_OK)
            if classified_serializer.is_valid():
                return Response(classified_serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=400)
    

# @api_view(["POST"])
# def base64_image_upload_api_view(request):
#     if request.method == "POST":
#         data = request.data
#         serializer = ArticleBase64Serilizer(data=data)
#         if serializer.is_valid():
#             article = serializer.save()
#             data = serializer.data
#             return Response(data=data)
#         return Response(serializer.errors, status=400)