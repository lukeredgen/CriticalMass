from __future__ import unicode_literals

from django.db import models
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from django_enumfield import enum
from durationfield.db.models.fields.duration import DurationField
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

#Enums
class UserType(enum.Enum):
    ADMIN = 1
    CONTRIBUTOR = 2
    MODERATOR = 3
    USER = 4

    labels = {
        ADMIN: 'Admin',
        CONTRIBUTOR: 'Contributor',
        MODERATOR: 'Moderator',
        USER: 'User'
    }

class Network(enum.Enum):
    NBC = "NBC"
    ABC = "ABC"

class MyUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, first_name, last_name, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        if not first_name:
            raise ValueError('Please enter first name')

        if not last_name:
            raise ValueError('Please enter last name')

        if not date_of_birth:
            raise ValueError('Please select valid date of birth')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
            first_name=first_name,
            last_name=last_name
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_contributor(self, username, date_of_birth, first_name, last_name, password):
        u = self.create_user(username, password=password, date_of_birth=date_of_birth, first_name=first_name, last_name=last_name
                             )
        u.user_type = 2
        u.save(using=self._db)
        return u

    def create_moderator(self, username, date_of_birth, first_name, last_name, password):
        u = self.create_user(username, password=password, date_of_birth=date_of_birth, first_name=first_name, last_name=last_name
                             )
        u.user_type = 3
        u.save(using=self._db)
        return u

    def create_superuser(self, email, date_of_birth, first_name, last_name, password):
        u = self.create_user(email=email, password=password, date_of_birth=date_of_birth, first_name=first_name, last_name=last_name
                             )
        u.is_admin = True
        u.user_type = 1
        u.save(using=self._db)
        return u

class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='Email Address',
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField()
    first_name = models.CharField(
        verbose_name='First Name',
        max_length=255
    )
    last_name = models.CharField(
        verbose_name='Last Name',
        max_length=255
    )
    is_admin = models.BooleanField(default=False)
    user_type = enum.EnumField(UserType)
    is_active = models.BooleanField(default=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['date_of_birth', 'first_name', 'last_name']

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

class ReleaseCreator(models.Model):
    name = models.CharField(
        max_length=255,
        blank=False
    )

    def __str__(self):
        return self.name

class GroupCreator(models.Model):
    name = models.CharField(
        max_length=255,
        blank=False
    )

    def __str__(self):
        return self.name

# Create your models here.
class Release(models.Model):
    name = models.CharField(
        max_length=255,
        blank=False
    )
    release_date = models.DateField(
        auto_now=False
    )
    creator = models.ForeignKey(
        'ReleaseCreator',
        on_delete=models.PROTECT,
        blank=False
    )
    group_creator = models.ForeignKey(
        'GroupCreator',
        on_delete=models.PROTECT,
        blank=False
    )
    length = DurationField(
        blank=True
    )
    cover_url = models.CharField(
        max_length=500,
        blank=True
    )
    review = models.ForeignKey(
        'Review',
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class Album(Release):
    pass

class Track(Release):
    album = models.ForeignKey(
        'Album',
        on_delete=models.PROTECT,
        blank=True
    )

class Movie(Release):
    owner = models.ForeignKey('MyUser', related_name='movies')

class TVSeries(Release):
    pass

class TVSeason(Release):
    tv_series = models.ForeignKey(
        'TVSeries',
        on_delete=models.PROTECT,
        blank=True
    )
    network = enum.EnumField(Network)

class TVEpisode(Release):
    tv_season = models.ForeignKey(
        'TVSeason',
        on_delete=models.PROTECT,
        blank=True
    )

class Game(Release):
    pass

class Book(Release):
    pass

class Review(models.Model):
    body = models.CharField(
        max_length=100000,
        blank=True,
        null=True
    )
    GRADES = (
        ('A', 'A'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B', 'B'),
        ('B-', 'B-'),
        ('C+', 'C+'),
        ('C', 'C'),
        ('C-', 'C-'),
        ('D+', 'D+'),
        ('D', 'D'),
        ('D-', 'D-'),
        ('F', 'F'),
    )
    grade = models.CharField(max_length=2, choices=GRADES)

    def __str__(self):
        return self.grade