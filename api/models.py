from django.db import models

# Create your models here.
from rest_framework_simplejwt.state import User


##########################################
#                                        #
# Make email in Django User unique field #
#                                        #
##########################################
User._meta.get_field('email')._unique = True