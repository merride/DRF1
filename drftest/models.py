from django.db import models

# Create your models here.
class PersonInfo(models.Model):
    #pgenderchoices =  [('M', '男'), ('F', '女'),]
    pname = models.CharField(max_length=25, verbose_name='姓名')
    pbirthday = models.DateField(verbose_name='出生日期')
    #pgender = models.CharField(max_length=2, choices=pgenderchoices)
    #pprofilephoto = models.ImageField()
    pdesc = models.TextField()
    #UUIDField
