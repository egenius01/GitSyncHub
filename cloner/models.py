from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class LinkDump(models.Model):
    name = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='gituser')
    repo_link = models.URLField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class JsonDump(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='dumpuser')
    link = models.OneToOneField(LinkDump, on_delete=models.CASCADE, primary_key=True, related_name='Linkdump')
    name = models.CharField(max_length=20)
    dob = models.CharField(max_length=10)
    nationality = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.user} dumped {self.link}\'s Json Data'
