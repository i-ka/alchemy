from django.db import models

# Create your models here.

class Element(models.Model):
    name = models.CharField(max_length=50,blank=False,default="Unknown element")
    first_recipe_el = models.IntegerField()
    second_recipe_el = models.IntegerField()
    discription = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def is_essential_element(self):
        if(self.first_recipe_el==0 and self.second_recipe_el==0):return True
        else:return False

    def __str__(self):
        return self.name
