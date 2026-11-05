from modeltranslation.translator import TranslationOptions, register

from blog.models import BannerModel
from products.models import CategoryModel, ProductModel, ColorModel


@register(CategoryModel)
class CategoryTranslationOptions(TranslationOptions):
    fields = 'name',


@register(ColorModel)
class ColorTranslationOptions(TranslationOptions):
    fields = 'color',


@register(ProductModel)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'short_description', 'long_description',)


@register(BannerModel)
class BannerTranslationOptions(TranslationOptions):
    fields = ('title', 'sub_title', 'text',)
