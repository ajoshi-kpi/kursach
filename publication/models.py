from django.db import models

# Create your models here.
class Publication(models.Model):
	class Meta():
		db_table = 'publication'
	publication_title = models.CharField(max_length = 200)
	publication_author = models.CharField(max_length = 200)
	publication_short = models.TextField()
	publication_text = models.TextField()
	publication_date = models.DateTimeField()	
	publication_cat = models.TextField(max_length = 30)

class Comments(models.Model):
	class Meta():
		db_table = 'comments'
	comments_text = models.TextField()
	comments_publication = models.ForeignKey(Publication)	 	