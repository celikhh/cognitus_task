import requests
from rest_framework import serializers, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Data


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ['label', 'text']


class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer


@api_view(["POST"])
def trigger_train(request):
    response = requests.post("http://algorithm:5000/train")
    return Response(response.json())


@api_view(["POST"])
def trigger_predict(request, user_text):
    response = requests.post("http://algorithm:5000/predict/%s" % user_text)
    return Response(response.json())
