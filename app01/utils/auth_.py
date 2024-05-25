from rest_framework import status
from rest_framework.authentication import BaseAuthentication
from django.conf import settings
from app01 import models
from rest_framework.exceptions import AuthenticationFailed
from app01 import models
from rest_framework.exceptions import APIException


class MyExc(APIException):
    status_code = status.HTTP_200_OK


class IpAuth(BaseAuthentication):
    def authenticate(self, request):
        if request.method == "OPTIONS":
            return
        ytwkey = request.headers.get('ytwkey')

        # print("ytw_key", request.headers)
        # print("ytw_key", ytwkey)
        ip = request.META['REMOTE_ADDR']
        obj = models.IpList.objects.filter(ip=str(ip)).first()
        if not obj:
            obj = models.IpList.objects.create(ip=str(ip), times=100)
            print("queryset", obj)
            times = obj.times
        else:
            times = obj.times
        if times <= 0:

            exist = models.YtwKey.objects.filter(key=ytwkey).exists()
            if exist:
                return
            raise MyExc({"msg": "接口次数不足,请联系ytw,获取ytw_key"})
        print("obj", obj)
        obj.times = obj.times - 1
        obj.save()
        return


class YtwKeyAuth(BaseAuthentication):
    def authenticate(self, request):
        """需要再请求头中添加一个ytwkey"""
        ytwkey = request.headers.get("ytwkey")
        print(ytwkey)
        instance = models.YtwKey.objects.filter(key=ytwkey).first()
        print("instance.times",instance.times)

        if instance.times <= 0:
            raise MyExc({"msg", "此key的次数已经用完了，请联系ytw获取更多次数"})
        instance.times -= 1
        instance.save()
        return
