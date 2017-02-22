from __future__ import unicode_literals
from django.db import models
import re
import bcrypt

# Create your models here.
EMAIL_REGEX = re.compile (r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def validate_user(self, post):
        isValid = True
        if not EMAIL_REGEX.match(post.get('email')):
            isValid = False
            print "1"
        if len(post.get("first_name"))==0:
            isValid = False
            print "2"
        if len(post.get("last_name"))==0:
            isValid = False
            print "3"
        if len(post.get('email'))==0:
            isValid = False
            print "4"
        if len(post.get("password"))==0:
            isValid = False
            print "5"
        if post.get('password') != post.get('confirm_password'):
            isValid = False
            print "6"
        return isValid

    def login_user(self,post):
        user = self.filter(email=post.get('email')).first()
        if user and bcrypt.hashpw(post.get('password').encode(), user.password.encode()) == user.password:
            return (True,user)
        return (False, 'notuser')

class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
