from django.db import models

# Create your models here.

class Quiz(models.Model):
    id = models.TextField(primary_key=True)
    name = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id

class Question(models.Model):
    question_id = models.TextField(primary_key=True)
    question_text = models.TextField(null=False)
    option_a = models.TextField(null=False)
    option_b = models.TextField(null=False)
    option_c = models.TextField(null=False)
    option_d = models.TextField(null=False)
    correct_answer = models.TextField(null=False)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self):
        return self.question_text

class Result(models.Model):
    result_id = models.TextField(primary_key=True)
    username = models.TextField(null=False)
    number_correct = models.IntegerField(null=False)
    total_questions = models.IntegerField(null=False)
    numeric_grade = models.FloatField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self):
        return self.result_id
