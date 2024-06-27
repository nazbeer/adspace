from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ['name','location','latitude','longitude','status','description','created_on','updated_on']
    list_filter = ('status',)
    search_fields = ('name', 'location')
    readonly_fields = ('created_on','updated_on')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','status','description','created_on','updated_on']
    list_filter = ('status',)
    search_fields = ('name',)
    readonly_fields = ('created_on','updated_on')


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name','category','status','description','created_on','updated_on']
    list_filter = ('status',)
    search_fields = ('name',)
    readonly_fields = ('created_on','updated_on')


@admin.register(ScreenType)
class ScreeenTypeAdmin(admin.ModelAdmin):
    list_display = ['name','status','description','created_on','updated_on']
    list_filter = ('status',)
    search_fields = ('name',)
    readonly_fields = ('created_on','updated_on')


@admin.register(TShirtSize)
class TShirtSizeAdmin(admin.ModelAdmin):
    list_display = ['name','status','description','created_on','updated_on']
    list_filter = ('status',)
    search_fields = ('name',)
    readonly_fields = ('created_on','updated_on')

@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ['category','subcategory','screen_type','description','area']
    list_filter = ('category',)
    search_fields = ('category','area','screen_type','location')


@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ['subject','message','received_date','closed','closed_date']
    list_filter = ('closed',)
    search_fields = ('vendor',)
