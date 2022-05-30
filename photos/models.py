from django.db import models

# Create your models here.


class Category(models.Model):
    '''categories module'''
    # CATEGORY=(
    #     'fashion':'fashion'
    # )
    name=models.CharField(max_length=40, blank=True)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()
        
    @classmethod
    def delete_category(cls, id):
        cls.objects.filter(id=id).delete()

    @classmethod
    def update_category(cls, id, cateUpdate):
        cls.objects.filter(id=id).update(category=cateUpdate)  


class Location(models.Model):
    '''locataion module'''
    name=models.CharField(max_length=40, blank=True)

    def __str__(self):
        return self.name



    def save_location(self):
        self.save()
        
    @classmethod
    def deleteLocation(cls, id):
        cls.objects.filter(id=id).delete()
        
    @classmethod
    def updateLocation(cls, id, locaUpdate):
        cls.objects.filter(id=id).update(location=locaUpdate)



class  Image(models.Model):
    '''image module'''
    name=models.CharField(max_length=40, blank=True)
    decription=models.TextField()
    image=models.ImageField(null=False, blank=True)
    category=models.ForeignKey(Category , on_delete=models.CASCADE)
    location=models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return self.name





    def save_image(self):
        self.save()
        
    @classmethod
    def update_image(cls, id, imagechange):
        cls.objects.filter(id = id).update(image1 = imagechange)
        
    @classmethod
    def delete_image(cls, id):
        cls.objects.filter(id=id).delete()

    @classmethod
    def update_image(cls, id, imagechange):
        cls.objects.filter(id = id).update(image = imagechange)

    @classmethod
    def get_images_by_id(cls, id):
        try:
            image = cls.objects.get(id=id)
            return image
         
            
        
        except Image.DoesNotExist:
            print('Image does not exist')

    @classmethod
    def search_image(cls, category):
        images = Image.objects.filter(category__category_name=category)
        return images

    @classmethod
    def filter_by_location(cls, location):
        images = Image.objects.filter(location__location=location)
        return images


    