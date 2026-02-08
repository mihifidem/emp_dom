from django.contrib import admin


from .models import Domingo

@admin.register(Domingo)
class DomingoAdmin(admin.ModelAdmin):
	list_display = ("title", "liturgical_time", "is_published")
	search_fields = ("title", "slug")
	list_filter = ("liturgical_time",)
