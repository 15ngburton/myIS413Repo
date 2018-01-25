from django.db import models


class Question(models.Model):
    question_text = models.TextField(blank=True, null=True)
    pub_date = models.DateTimeField('date published')
    duration = models.IntegerField(null=True)
    address = models.TextField(blank=True, null=True)
    zip = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    citystatezip = models.TextField(blank=True, null=True)


#class Choice(models.Model):
#    question = models.ForeignKey(Question, on_delete=models.CASCADE)
#    choice_text = models.CharField(max_length=200)
#    votes = models.IntegerField(default=0)
