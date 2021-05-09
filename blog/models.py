from django.db import models

# Create your models here.
class Poll (models.Model):

  STATES =(
    (0, " Draft"),
    (1," published"),
  )


  title = models.CharField(max_length=100)
  question = models.CharField(max_length =100)
  active_until = models.DateTimeField(auto_now_add=True)
  status =models.IntegerField(choices=STATES)


class Option(models.Model):
    title = models.CharField(max_length=100)
    Has_by =models.ForeignKey(
     'Poll',
     on_delete=models.CASCADE,
    )


class Response(models.Model):
  name = models.CharField(max_length=50)
  response_time = models.DateTimeField(auto_now_add=True)
  Has_by =models.ForeignKey(
     'Option',
     on_delete=models.CASCADE,
    )


  

  

