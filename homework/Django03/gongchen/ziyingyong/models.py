from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

class BookInfo(models.Model):
    """
    id          主键
    name        书籍名字
    pub_date    书籍发布日期
    readcount   阅读量
    commentcount 评论量
    is_delete   是否删除
    """
    # id 主键 django自动为我们生成
    name = models.CharField(max_length=10, verbose_name='admin站点相关不是重点')
    pub_date = models.DateField(null=True)
    readcount = models.IntegerField(default=0)
    commentcount = models.IntegerField(default=0)
    is_delete = models.BooleanField(default=True)

    # 默认数据表的名字是: 子应用名小写_类名小写
    # 表名是可以修改的
    class Meta:
        db_table = 'bookinfo'  # 表名是可以修改的

    def __str__(self):
        return self.name


class PeopelInfo(models.Model):
    GENDER_CHOICE = (
        (0, 'boy'),
        (1, 'girl')
    )
    # (值,说明)


    name = models.CharField(max_length=10)
    # choices 选项 只能从 元组中选取一个
    # choices 的值 我们定义元组
    gender = models.SmallIntegerField(choices=GENDER_CHOICE, default=0)
    description = models.CharField(max_length=100, null=True)
    is_delete = models.BooleanField(default=False)

    # 外键
    # 属性 -- 字段 表的字段 会自动给我们的属性值添加一个_id
    # 类型 -- models.ForeignKey
    # 选项 -- 第一个参数:关联的类名
    #         第二个参数:on_delete

    #  黑帮老大 1个人
    #  小弟    n个人
    #  小弟不让老大死 劫狱
    #  老大死就死, 选个新的老大
    #  老大死 小弟跟着死

    # 书籍 1      -- 主表
    # 人物 n      -- 从表
    # on_delete  级联操作
    # 书籍表的数据 如果删除了, 人物表关联的数据该怎么做?
    # 1. 拒绝操作  2. 书籍数据删除了就删除了,人物信息还在  3. 书籍数据删除了就删除了,人物信息也删除
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)

    class Meta:
        db_table = 'peopleinfo'

    # 注意 表名必须是这个,因为后边 插入数据的SQL语句写死了

    def __str__(self):
        return self.name