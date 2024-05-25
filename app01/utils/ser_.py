"""序列化 器"""
from rest_framework import serializers
from app01 import models


class WallPaperSer(serializers.ModelSerializer):
    class Meta:
        model = models.WallPaper
        fields = "__all__"


