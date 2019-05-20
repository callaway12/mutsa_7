from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('published')
    body = models.TextField()
    def summary (self):
        return self.body[:50]
    
    def __str__ (self):
        return self.title
        

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comment_text = models.TextField(max_length=255)
