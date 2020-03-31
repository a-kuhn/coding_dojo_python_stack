from django.db import models
from datetime import datetime

# Create your models here.
class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        #add keys and values to error dictionary for each invalid field
        print("postData: ", postData)
        if len(postData["network"])<3:
            errors["network"] = "network input too short"
        if len(postData["title"])<2:
                errors["title"] = "title too short"
        if postData["title"] in [show['title'] for show in Show.objects.all().values()]:
            errors["title_dupe"] = "this title already exists"
        if len(postData["desc"]) > 0:
            if len(postData["desc"])<10:
                errors["desc"] = "description too short"
        if postData["release_date"] > datetime.now().strftime("%Y-%m-%d"):
            errors["release_date"] = "invalid release date"
        print("errors:  ",errors)
        return errors


class Show(models.Model):
    title = models.CharField(max_length = 255)
    network = models.CharField(max_length = 255)
    release_date = models.DateTimeField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = ShowManager()

    def releasedate(self):
        return self.release_date.strftime('%B %d'+','+' %Y')

    def edit_date(self):
        return self.release_date.strftime("%Y-%m-%d")