from django.db import models


# Create your models here.

class WallPaper(models.Model):
    """壁纸"""
    title = models.CharField(verbose_name="标题", max_length=128)
    url = models.ImageField(verbose_name="路径", upload_to='wallpaper/')
    author = models.CharField(verbose_name="作者", max_length=128, default="余天王")
    detail = models.TextField(verbose_name="详情", default="详情描述空空如也")


class IpList(models.Model):
    """ip名单"""
    ip = models.CharField(verbose_name="ip地址", max_length=64)
    times = models.IntegerField(verbose_name="剩余次数(默认一百次)", default=100)

class YtwKey(models.Model):
    """ytw_key 列表"""
    key = models.CharField(verbose_name="ytw_key",max_length=128)
    times = models.IntegerField(verbose_name="剩余次数",default=300)
