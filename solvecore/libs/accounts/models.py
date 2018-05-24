"""
Provide model user and user-account related models.
"""
from django.core import validators
from django.core.mail import send_mail
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, **kwargs):
        user = self.create_user(**kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    Store User account details.
    """
    # Use either of the username fields below:
    # username = models.CharField(
    #     _('username'),
    #     max_length=30,
    #     unique=True,
    #     help_text=_('Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.'),
    #     validators=[
    #         validators.RegexValidator(
    #             r'^[\w.@+-]+$',
    #             _('Enter a valid username. This value may contain only '
    #               'letters, numbers ' 'and @/./+/-/_ characters.')
    #         ),
    #     ],
    #     error_messages={
    #         'unique': _("A user with that username already exists."),
    #     },
    # )
    # username = models.CharField(_('username'), max_length=10, unique=True,
        # help_text=_('Required. 10 characters mobile number. digits only.'),
        # validators=[
            # validators.RegexValidator(r'^\d+$', _('Enter a valid username. '
                # 'This value may contain only numbers of your 10 digit mobile number.'), 'invalid'),
        # ],
        # error_messages={
            # 'unique': _("A user with that username already exists."),
        # })
    email = models.EmailField(_('email address'), max_length=255, unique=True,
                              db_index=True,)

    # Use Either first_name and last_name OR name field.
    # first_name = models.CharField(_('first name'), max_length=30, blank=True)
    # last_name = models.CharField(_('last name'), max_length=30, blank=True)
    name = models.CharField(_('name'), max_length=255)

    # profile_picture = models.ImageField(upload_to='profile_picture', null=True, blank=True)
    # Add your custom user model fields here.

    is_staff = models.BooleanField(_('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(_('active'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active.  Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    # Modify USERNAME_FIELD and REQUIRED_FIELDS as required.
    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['email']

    class Meta:
        swappable = 'AUTH_USER_MODEL'
        db_table = 'auth_user'
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ['name', 'email'] # Set it as required.
        permissions = (
            ("can_activate", "Can activate user"),
            ("can_deactivate", "Can deactivate user"),
            ("can_view", "Can view user")
        )

    # Use Either one of __str__ methods.
    def __str__(self):
        return '{name} <{email}>'.format(
            name=self.name,
            email=self.email,
        )
    # def __str__(self):
        # return '{first_name} {last_name} <{email}>'.format(
            # first_name=self.first_name,
            # last_name=self.last_name,
            # email=self.email,
        # )


    # Use either one of get_full_name methods and either one of get_short_name methods
    # def get_full_name(self):
        # """
        # Returns the first_name plus the last_name, with a space in between.
        # """
        # full_name = '%s %s' % (self.first_name, self.last_name)
        # return full_name.strip()

    # def get_short_name(self):
        # "Returns the short name for the user."
        # return self.first_name

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)
