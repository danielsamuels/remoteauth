from django.contrib import admin
from .models import Rank, DescriptionLine


class DescriptionLineAdmin(admin.TabularInline):
    model = DescriptionLine


class RankAdmin(admin.ModelAdmin):
    inlines = (DescriptionLineAdmin,)

admin.site.register(Rank, RankAdmin)
