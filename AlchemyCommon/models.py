from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save, pre_delete
import os
# Create your models here.

from alchemysite import settings

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

    def dict(self):
        return {'id': self.id,
                'name': self.name,
                'first_recipe_el': self.first_recipe_el,
                'second_recipe_el': self.second_recipe_el,
                'description': self.description,
                'category': self.category.id,
                'created_at': str(self.created_at)}


class Report(models.Model):
    user = models.ForeignKey(User)
    accepted = models.NullBooleanField(null=True)
    text = models.TextField(max_length=500, blank=False)
    screenshot = models.ImageField(upload_to='report_screenshots/', blank=True)
    date = models.DateTimeField(auto_now=True)


    def delete_image(self):
        if self.screenshot:
            try:
                os.remove(settings.BASE_DIR + self.screenshot.url.replace('/', '\\'))
            except FileNotFoundError:
                pass
            self.screenshot = None
            self.save()


@receiver(pre_save, sender=Report)
def report_pre_save(sender, instance, **kwargs):
    if not instance.screenshot:
        return

    reports = Report.objects.all().order_by('-date')
    reports_with_scr_count = 0
    first_report_with_screen = None
    for report in reports:
        if report.screenshot:
            first_report_with_screen = report
            reports_with_scr_count += 1

    if first_report_with_screen and first_report_with_screen.id == instance.id:
        return

    if reports_with_scr_count >= settings.MAX_REPORT_SCREENS:
        first_report_with_screen.delete_image()


@receiver(pre_delete, sender=Report)
def report_pre_delete(sender, instance, **kwargs):
    instance.delete_image()


class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True, related_name='profile')
    open_elements = models.ManyToManyField(Element)
    activationToken = models.TextField()

    def __str__(self):
        return self.user.username+"'s profile"


@receiver(post_save, sender=User)
def user_post_save(sender, instance, **kwargs):
    (profile, new) = UserProfile.objects.get_or_create(user=instance)
