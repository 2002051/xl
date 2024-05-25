from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import ListModelMixin
from app01.utils.res_ import MyResponse
from app01.utils.ser_ import WallPaperSer
from app01 import models
from app01.utils.auth_ import IpAuth,YtwKeyAuth
# from app01.utils.thr_ import CommonThrottle

class WallPaperView(MyResponse, ListModelMixin, GenericViewSet):
    authentication_classes = [IpAuth,YtwKeyAuth]
    queryset = models.WallPaper.objects.all().order_by("-id")
    serializer_class = WallPaperSer
    # throttle_classes = [CommonThrottle]


