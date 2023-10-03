from django.db  import models


#author DataBase
class Author(models.Model):
    author_name=models.CharField(max_length=50)
    e_phn=models.CharField(max_length=20)
    author_question=models.CharField(max_length=500)
    pub_date=models.DateTimeField('date published')

    def __str__(self):
        return self.author_question


#voting or choose DataBase
class Choice(models.Model):
    question = models.ForeignKey(Author, on_delete=models.CASCADE)
    Choice_Answer= models.CharField(max_length=200)
    vote = models.IntegerField(default=0)

    def __str__(self):
        return self.Choice_Answer