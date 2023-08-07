from django.db import models


class FAQ(models.Model):
    question = models.CharField(max_length=300)
    question.short_description = 'FAQ Question'
    answer = models.TextField()
    answer.short_description = 'FAQ Answer'
    
    def __str__(self):
        return self.question
