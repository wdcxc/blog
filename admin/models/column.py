from django.db import models

class ColumnModel(models.Model):
    """栏目模型类"""

    name = models.CharField(max_length=100) # 栏目名
    parent = models.ForeignKey('self',on_delete=models.CASCADE) # 栏目父节点
    order = models.IntegerField() # 栏目显示顺序（数字越大，显示越前） 
    show = models.BooleanField(default=True) # 栏目是否显示（默认显示）
    grade = models.IntegerField() # 栏目等级，子栏目等级=父栏目等级+1
    add_time = models.DateTimeField(auto_now_add=True) # 栏目添加时间

    class Meta:
        db_table="columns"


