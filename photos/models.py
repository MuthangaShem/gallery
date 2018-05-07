from django.db import models
# Create your models here.


class Location(models.Model):
    location_name = models.CharField(max_length=30)

    def __str__(self):
        return self.location_name

    # save method
    def location_save(self):
        self.save()
    # delete method

    def location_delete(self):
        self.delete()

    @classmethod
    def update_image(cls, id, value):
        cls.objects.filter(id=id).update(location_name=value)
