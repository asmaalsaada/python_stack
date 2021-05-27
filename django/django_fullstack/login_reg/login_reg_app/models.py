from django.db import models
import re

# Create your models here.
class UsersManager(models.Manager):
    def reg_validator(self,postData):
        errors = {}
        FIRST_NAME_REGEX = re.compile(r"\b([A-ZÀ-ÿ][-,a-z. ']+[ ]*)+")
        if not FIRST_NAME_REGEX.match(postData['f_name']):
            errors['f_name'] = "Valid Charactors include (A-Z) (a-z) (' space -)"
        LAST_NAME_REGEX = re.compile(r"\b([A-ZÀ-ÿ][-,a-z. ']+[ ]*)+")
        if not LAST_NAME_REGEX.match(postData['l_name']):
            errors['l_name'] = "Last name has to be only letters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!"
        if len(postData['f_name']) < 2 : 
            errors['f_name'] = "The First Name should be at least 2 Characters long"
        if len(postData['l_name']) < 2 : 
            errors['l_name'] = "The Last Name should be at least 2 Characters long"
        if postData['c_pass'] !=  postData['passwd']: 
            errors['c_pass'] = "The passwords doesn't match!"   
        if len(postData['passwd']) < 8 : 
            errors['passwd'] = "The password should be at least 8 Characters long"
        return errors
    def login_validator(self,postData):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!"
        if len(postData['passwd']) < 8 : 
            errors['passwd'] = "The password should be at least 8 Characters long"
        return errors

class Users(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UsersManager()