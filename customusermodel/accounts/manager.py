from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, phone_number, password=None, **kwargs):
        if not phone_number:
            raise ValueError('Phone number is required')
        
        kwargs['email'] = self.normalize_email(kwargs['email'])

        user = self.model(phone_number=phone_number, **kwargs)
        user.set_password(password)
        user.save(using=self.db)

        return user
    
    def create_superuser(self, phone_number, password=None, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)

        return self.create_user(phone_number, password, **kwargs)