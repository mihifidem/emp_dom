from django.db import models


class Domingo(models.Model):
	title = models.CharField(max_length=120)
	slug = models.SlugField(unique=True, max_length=80)
	liturgical_time = models.CharField(max_length=40)
	sunday_number = models.PositiveIntegerField()
	central_message = models.CharField(max_length=200)
	free_content = models.TextField()
	premium_content = models.TextField()
	admin_notes = models.TextField(blank=True, null=True)
	is_published = models.BooleanField(default=True)

	class Meta:
		verbose_name = 'Domingo'
		verbose_name_plural = 'Domingos'
		ordering = ['liturgical_time', 'sunday_number']

	def __str__(self):
		return f"{self.title} ({self.liturgical_time} #{self.sunday_number})"
