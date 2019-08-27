from django.db import models
from django.contrib.auth import get_user_model

class Blog(models.Model):
    title = models.CharField(max_length = 50)
    date =  models.DateTimeField(auto_now_add = True)
    content = models.TextField(max_length = 5000)
    owner = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)

    def __str__(self):
        return self.title
