from django.contrib import admin
from top10.models import *


class TableInline(admin.StackedInline):
    model = TableRow
    extras = 3

class TableValue(admin.StackedInline):
    model = TableValue
    extras = 3


class ProsInline(admin.StackedInline):
    model = Pros
    extras = 3


class BenefitsInline(admin.StackedInline):
    model = Benefits
    extras = 3


class ConsInline(admin.StackedInline):
    model = Cons
    extras = 3


class PostAdmin(admin.ModelAdmin):
    inlines = [TableInline]
    prepopulated_fields = {'slug' : ('subject',)}


class PostsItemAdmin(admin.ModelAdmin):
    inlines = [TableValue, BenefitsInline, ProsInline, ConsInline]



admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(PostItem, PostsItemAdmin)
admin.site.register(Comment)
