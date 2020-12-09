from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Category(models.Model):
    category_name = models.CharField('Category', max_length=50)
    category_title = models.CharField('Category title', max_length=100, null=True)
    def __str__(self):
        return self.category_name



class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    CHOISES = (
        ("Must read" , "Must read"),
        ("Hot this week", 'Hot this week'),
        ("Trending", 'Trending')
    )
    importance = models.CharField(max_length=200, null=True, choices=CHOISES)


    subject = models.CharField('Titlte', max_length=200)
    item_name = models.CharField('Post item name(What kind of items will be appear in this post)', max_length=200,
                                 null=True)
    title_description = models.CharField('TittleDescription', max_length=400)
    picture_main = models.ImageField(upload_to="gallery")
    post_description = RichTextField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    slug = models.SlugField(null=True, unique=True)
    def __str__(self):
        return self.subject


class PostItem(models.Model):
    choises = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    )

    subject = models.ForeignKey(Post, on_delete=models.CASCADE)
    item_title = models.CharField('Item title', max_length=500)
    item_name = models.CharField('ItemName', max_length=50)
    item_description = models.CharField('ItemDescription', max_length=50)
    item_picture = models.ImageField(upload_to="gallery")
    item_link = models.CharField('Link', max_length=400)
    place_in_top = models.IntegerField(choices=choises, default='1')

    description = RichTextField()

    def __str__(self):
        return self.item_name


class Pros(models.Model):
    item_name = models.ForeignKey(PostItem, on_delete=models.CASCADE)
    pros_title = models.CharField('Pros', max_length=200)

    def __str__(self):
        return self.pros_title


class Cons(models.Model):
    item_name = models.ForeignKey(PostItem, on_delete=models.CASCADE)
    cons_title = models.CharField('Cons', max_length=200)

    def __str__(self):
        return self.cons_title


class Benefits(models.Model):
    item_name = models.ForeignKey(PostItem, on_delete=models.CASCADE)
    benefit_title = models.CharField('Benefit title', max_length=200)
    benefit_desc = models.CharField('Benefit description', max_length=200)

    def __str__(self):
        return self.benefit_title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_name = models.ForeignKey(User, editable=False, on_delete=models.CASCADE)
    comment_text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)


class TableRow(models.Model):
    post_name = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    table_row = models.CharField('Table row', max_length=200, null=True)


class TableValue(models.Model):
    post_item = models.ForeignKey(PostItem, on_delete=models.CASCADE, null=True)
    table_value = models.CharField('Table value', max_length=200, null=True)

    def __str__(self):
        return self.table_value


