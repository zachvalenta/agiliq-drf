from django.db import models
from django.contrib.auth.models import User


class Poll(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question


class Choice(models.Model):
    # data type = Poll primary key?
    # re: `related_name`, when using ORM API will be able to use `choices`
    # instead of `choice_set`
    poll_id = models.ForeignKey(Poll, related_name='choices', on_delete=models.CASCADE)
    text = models.CharField(max_length=100)

    def __str__(self):
        return self.choice_text


class Vote(models.Model):
    choice_id = models.ForeignKey(Choice, related_name='votes', on_delete=models.CASCADE)
    poll_id = models.ForeignKey(Poll, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        # meaning there can only be one record with this pairing of poll and user
        unique_together = ("poll_id", "user_id")
