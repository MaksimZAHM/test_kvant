from django.contrib import admin
from priorities.models import Creator, Priority


class PriorityAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'priority_value',
        'condition',
        'pub_date'
    )
    search_fields = ('priority_value', 'pub_date')
    list_filter = ('priority_value', 'pub_date', 'creators')

admin.site.register(Priority, PriorityAdmin)

class CreatorAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name'
    )
    search_fields = ('first_name', 'last_name')
    list_filter = ('last_name',)

admin.site.register(Creator, CreatorAdmin)
