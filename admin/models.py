from django.db import models

class TagModel(models.Model):
    """文章标签模型类"""

    name = models.CharField(max_length=100) # 标签名字
    add_time = models.DateTimeField(auto_now_add=True) # 标签第一次添加时间
    show = models.BooleanField(default=True) # 是否显示
    grade = models.IntegerField(default=1) # 显示等级(等级越大，显示越前)

    class Meta:
        db_table = "tags"

class CategoryModel(models.Model):
    """文章类别模型类""" 

    name = models.CharField(max_length=100) # 类别名称  
    add_time = models.DateTimeField(auto_now_add=True) # 类别第一次添加时间
    show = models.BooleanField(default=True) # 是否显示
    grade = models.IntegerField(default=1) # 显示等级(等级越大，显示越前)
    show_in_header = models.BooleanField(default=False) # 是否在首页头部展示

    class Meta:
        db_table = "categories"

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

class DateArchiveModel(models.Model):
    """文章日期归档模型类"""

    DATE_GRADE_YEAR = 'Y'
    DATE_GRADE_MONTH = 'M'
    DATE_GRADE_DAY = 'D'
    DATE_GRADE = (('Y','year'),('M','m'),('D','day'))
    grade = models.CharField(max_length=1,choices=DATE_GRADE,default='Y') # 文章日期归档级别,共有三级：年，月，日
    pre_grade = models.ForeignKey('self',on_delete=models.CASCADE,related_name="next_grades",related_query_name="next_grade",null=True,default=None) # 该归档的父级
    date = models.CharField(max_length=2) # 日期中该所属归档级别的部分

    class Meta:
        db_table="date_archive"

class  CommentModel(models.Model):
    """文章评论模型类"""

    content = models.TextField() # 评论内容
    add_time = models.DateTimeField(auto_now_add=True) # 评论时间
    reply_comments = models.ManyToManyField('self',related_name="replied_comments",related_query_name="replied_comment",symmetrical=False) # 回复评论
    article = models.ForeignKey('ArticleModel',on_delete=models.CASCADE,related_name="comments",related_query_name="comment",null=True,blank=True) # 评论所属文章
    visitor = models.ForeignKey('VisitorModel',on_delete=models.CASCADE,related_name="comments",related_query_name="comment") # 评论者
    grade = models.IntegerField(default=0) # 评论等级，直接回复文章等级为0，等级越大代表回复嵌套层次越深

    class Meta:
        db_table = "comments"

class ArticleModel(models.Model):
    """文章模型类"""

    meta = models.TextField(null=True) # 文章头部 meta
    content = models.TextField() # 文章正文内容
    title = models.CharField(max_length=100,default="") # 文章标题
    author = models.CharField(max_length=50) # 文章作者
    add_time = models.DateTimeField(auto_now_add=True) # 文章添加时间
    open_to_public = models.BooleanField(default=False) # 是否公开
    description = models.CharField(max_length=300,default="暂无简介") # 文章简介
    tags = models.ManyToManyField(TagModel,related_name="articles",related_query_name="article") # 文章标签
    categories = models.ManyToManyField(CategoryModel,related_name="articles",related_query_name="article") # 文章类别
    read_num = models.IntegerField(default=0) # 文章阅读次数
    date_archives = models.ManyToManyField(DateArchiveModel,related_name="articles",related_query_name="article") # 文章日期归档
    allow_comment = models.BooleanField(default=False) # 是否允许评论

    class Meta:
        db_table = "articles"

class VisitorModel(models.Model):
    """ 访客模型 """

    name = models.CharField(max_length=50,default="anony") # 访客名字
    IP = models.GenericIPAddressField() # 访客 IP 地址
    add_time = models.DateTimeField(auto_now_add=True) # 访客第一次访问时间
    forbidden_visit = models.BooleanField(default=False) # 是否禁止访问
    avatar_url = models.URLField(default="https://ss1.bdstatic.com/70cFvXSh_Q1YnxGkpoWK1HF6hhy/it/u=1667998903,1616440854&fm=27&gp=0.jpg") # 头像链接地址

    class meta:
        db_table="visitors"

class VisitedRecordModel(models.Model):
    """ 访客访问记录模型 """
    
    visitor = models.ForeignKey(VisitorModel,on_delete=models.CASCADE) # 访客
    article = models.ForeignKey(ArticleModel,on_delete=models.CASCADE) # 访问文章
    visited_time = models.DateTimeField(auto_now_add=True) # 访问时间

    class meta:
        db_table = "visited_records"
