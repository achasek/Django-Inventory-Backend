from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# TO SEED DATA
# python3 manage.py loaddata data

class Item(models.Model):
  name = models.CharField(max_length = 100)
  price = models.IntegerField(default = 0)
  description = models.TextField(max_length = 300)
  category = models.CharField(max_length = 100)
  image = models.TextField(max_length = 300)

  def __str__(self):
    return f'{self.name}'
  
class Profile(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    items = models.ManyToManyField(Item, related_name="cart", blank=True)

    # def __str__(self):
    #   return f'{self.username}'
    
    def __str__(self):
      return "%s (%s)" % (
        self.username,
        ", ".join(item.name for item in self.items.all())
    )

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
