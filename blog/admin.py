from blog.models import BannerModel, PostModel, CommentModel, CommentLikeModel

from django.contrib import admin

from products.admin import MyTranslationAdmin


@admin.register(BannerModel)
class BannerModelAdmin(MyTranslationAdmin):
    list_display = ['title', 'sub_title', 'text']
    search_fields = ['title', 'sub_title', 'text']
    list_filter = ['title', 'sub_title', 'text']



admin.site.register(PostModel)
admin.site.register(CommentModel)
admin.site.register(CommentLikeModel)
