from django.contrib import admin

# Register your models here.

from django.utils.html import format_html
from culapp import models


# MasterPieces admin model
class MasterPiecesAdmin(admin.ModelAdmin):
    # 需要显示的字段信息
    list_display = ('id', 'pieces_name_ch', 'pieces_name_en')

    # 设置哪些字段可以点击进入编辑界面，默认是第一个字段
    list_display_links = ('id', 'pieces_name_ch', 'pieces_name_en')

    # 让ID显示为5位数
    def id(self, obj):
        return format_html(
            '<span>{}</span>',
            '%05d' % obj.pieces_id
        )
admin.site.register(models.MasterPieces, MasterPiecesAdmin)


# Craftsman admin model
class CraftsmanAdmin(admin.ModelAdmin):
    # 需要显示的字段信息
    list_display = ('id', 'craftsman_name_ch', 'item_pieces_name', 'craftsman_name_en')

    # 设置哪些字段可以点击进入编辑界面，默认是第一个字段
    list_display_links = ('id', 'craftsman_name_ch', 'item_pieces_name', 'craftsman_name_en')

    # 让ID显示为5位数
    def id(self, obj):
        return format_html(
            '<span>{}</span>',
            '%05d' % obj.craftsman_id
        )
    def item_pieces_name(self, obj):
        return format_html(
            '<span>{}</span>',
            obj.item.pieces_name_ch
        )

    item_pieces_name.short_description = '传承项目'
admin.site.register(models.Craftsman, CraftsmanAdmin)


# Events admin model
class EventsAdmin(admin.ModelAdmin):
    # 需要显示的字段信息
    list_display = ('id', 'theme')

    # 设置哪些字段可以点击进入编辑界面，默认是第一个字段
    list_display_links = ('id', 'theme')

    # 让ID显示为5位数
    def id(self, obj):
        return format_html(
            '<span>{}</span>',
            '%05d' % obj.events_id
        )
admin.site.register(models.Events, EventsAdmin)


# User admin model
class UserAdmin(admin.ModelAdmin):
    # 需要显示的字段信息
    list_display = ('id', 'username', 'password')

    # 设置哪些字段可以点击进入编辑界面，默认是第一个字段
    list_display_links = ('id', 'username', 'password')

    # 让ID显示为5位数
    def id(self, obj):
        return format_html(
            '<span>{}</span>',
            '%05d' % obj.user_id
        )
admin.site.register(models.User, UserAdmin)

