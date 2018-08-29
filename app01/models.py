from django.db import models

# Create your models here.



#出版社表
class Publisher(models.Model):
    id = models.AutoField(primary_key=True)#创建一个自增的主键字段
    name = models.CharField(max_length=64,null=False,unique=True)  #unique  唯一
    addr = models.CharField(max_length=128,default="雁塔西路")

#书表
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64,null=False,unique=True)
    publisher = models.ForeignKey(to="Publisher")
    def __str__(self):
        return "<Book object:{}>".format(self.title)


#作者表

class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16,null=False,unique=True)
    book = models.ManyToManyField(to="Book")
    #告诉ORM,我这张表和book表是多对多的关系关联，ORM自动帮我生成了第三张表
    def __str__(self):
        return "<Author object:{}>".format(self.name)