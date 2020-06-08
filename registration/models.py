from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class MyUserManager(BaseUserManager):
    def create_user(self, email, name,gender, title,password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not name:
            raise ValueError('Users must have an name')
        if not title:
            raise ValueError('Users must have an title')
        if not password:
            raise ValueError('Users must have an password')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            title = title,
            gender = gender
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name,gender, title,password=None):
        user = self.create_user(
            email,
            password=password,
            name=name,
            gender=gender,
            title = title)
        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address',max_length=255,unique=True)
    name = models.CharField(verbose_name='name',max_length=60)
    title = models.CharField(verbose_name='title',max_length=30)
    gender=models.CharField(verbose_name='gender',max_length=1)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    score = models.IntegerField(default=0)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','title','gender']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        # Simplest possible answer: All admins are staff
        return self.is_admin
