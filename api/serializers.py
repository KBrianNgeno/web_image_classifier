from rest_framework import serializers
from .models import Image, ClassifiedImage
from drf_extra_fields.fields import Base64ImageField

class ImageBase64Serilizer(serializers.ModelSerializer):
    image = Base64ImageField(required=False)
    class Meta:
        model = Image
        fields = ["id","image"]
        # fields = ["title", "content", "image"]

class ClassifiedImageSerializer(serializers.ModelSerializer):
    # image = Base64ImageField(required=False)
    # score = serializers.DecimalField(required=False)
    class Meta:
        model = ClassifiedImage
        fields = ["id", "category", "score"]