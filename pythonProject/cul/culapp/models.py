from django.db import models

# Create your models here.

# 超级用户
# username:001
# email:2451094971@qq.com
# password:001

# 非遗名录 master pieces
class MasterPieces(models.Model):
    pieces_id = models.IntegerField(null=False, primary_key=True, verbose_name='pieces_id')
    pieces_name_ch = models.CharField(max_length=64, null=False, verbose_name='项目名称')
    pieces_name_en = models.CharField(max_length=64, null=False, verbose_name='英文名')

    def __unicode__(self):  # __str__ on Python 3
        return self.MasterPieces

# 传承人名录 craftsman
class Craftsman(models.Model):
    craftsman_id = models.IntegerField(null=False, primary_key=True, verbose_name='craftsman_id')
    craftsman_name_ch = models.CharField(max_length=64, null=False, verbose_name='姓名')
    craftsman_name_en = models.CharField(max_length=64, null=False, verbose_name='英文名')
    item = models.ForeignKey(MasterPieces, on_delete=models.DO_NOTHING, verbose_name='传承项目')

# 活动events
class Events(models.Model):
    events_id = models.IntegerField(null=False, primary_key=True, verbose_name='events_id')
    theme = models.CharField(max_length=64, null=False, verbose_name='主题')

# 系统管理者 user
class User(models.Model):
    user_id = models.IntegerField(null=False, primary_key=True, verbose_name='工号')
    username = models.CharField(max_length=64, null=False, verbose_name='用户名')
    password = models.CharField(max_length=64, null=False, verbose_name='密码')
