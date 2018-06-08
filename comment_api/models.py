from django.db import models

class Comment(models.Model):
	name = models.CharField(max_length=50)
	comment_text = models.CharField(max_length=100)

	def __str__(self):
		return self.name