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


class Category(models.Model):
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return self.category_name

     # save method
    def category_save(self):
        self.save()
    # delete method

    def category_delete(self):
        self.delete()

    @classmethod
    def update_image(cls, id, value):
        cls.objects.filter(id=id).update(category_name=value)


class Image(models.Model):
    image_name = models.CharField(max_length=20)
    image_description = models.TextField(max_length=200)
    image_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    image_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('published at', auto_now_add=True)
    image_url = models.ImageField(upload_to='images/%Y-%m-%d', null=True)

    def __str__(self):
        return self.image_name

    # save method
    def image_save(self):
        self.save()
    # delete method

    def image_delete(self):
        self.delete()
