from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50,
                            blank=False,
                            default="Unknown category")

    def __str__(self):
        return self.name


class Element(models.Model):
    name = models.CharField(max_length=50,
                            blank=False,
                            default="Unknown element",
                            unique=True)
    first_recipe_el = models.IntegerField()
    second_recipe_el = models.IntegerField()
    description = models.TextField()
    category = models.ForeignKey(Category)
    created_at = models.DateTimeField(auto_now=True)

    def is_essential_element(self):
        if(self.first_recipe_el == 0 and self.second_recipe_el == 0):
            return True
        else:
            return False

    def __str__(self):
        return self.name

    def check_on_delete(self):
        conflict_elements = Element.objects.filter(models.Q(first_recipe_el=self.id) | models.Q(second_recipe_el=self.id))
        if len(conflict_elements) == 0:
            return False
        else:
            return conflict_elements


class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True, related_name='profile')
    open_elements = models.ManyToManyField(Element)

    def __str__(self):
        return self.user.username+"'s profile"


@receiver(post_save, sender=User)
def user_post_save(sender, instance, **kwargs):
    (profile, new) = UserProfile.objects.get_or_create(user=instance)