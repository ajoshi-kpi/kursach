from django.contrib import admin
from publication.models import Publication, Comments
# Register your models here.

class PublicationAdmin(admin.ModelAdmin):
	fields = ['publication_title', 'publication_author', 'publication_cat', 'publication_short' ,'publication_text', 'publication_link','publication_date']
	list_filter = ['publication_date']

admin.site.register(Publication,PublicationAdmin)	