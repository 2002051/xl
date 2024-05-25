# """限流组件"""
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import exceptions
# from rest_framework import status
# from rest_framework.throttling import SimpleRateThrottle
# from django.core.cache import cache as default_cache
#
#
# class ThrottledException(exceptions.APIException):
#     """限流异常"""
#     status_code = status.HTTP_429_TOO_MANY_REQUESTS
#     default_code = 'throttled'
#
#
# class CommonThrottle(SimpleRateThrottle):
#     """普通限流逻辑， 用户初次使用接口，将会拥有默认100次访问"""
#     cache = default_cache  # 访问记录存放在django的缓存中（需设置缓存）
#     scope = "user"  # 构造缓存中的key
#     cache_format = 'throttle_%(scope)s_%(ident)s'
#     THROTTLE_RATES = {"user": "10/m"}
#     def get_cache_key(self, request, view):
#         self.ident = self.get_ident(request)
#         print("1",self.ident)
#
#         return True
#
#     def throttle_failure(self):
#         print(12313)
#         print("ident", self.ident)
#
#         detail = {
#             "code": 1005,
#             "data": "访问频率限制",
#             'detail': "需等待{}s才能访问"
#         }
#         raise ThrottledException(detail)