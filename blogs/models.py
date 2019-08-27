from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length = 50)
    date =  models.DateTimeField(auto_now_add = True)
    content = models.TextField(max_length = 5000)

    def __str__(self):
        return self.title
