from django.core.management.base import BaseCommand , CommandParser
from django.contrib.auth import get_user_model

class Command(BaseCommand):
 def add_arguments(self, parser):
  parser.add_argument('user')
  parser.add_argument('email')
  parser.add_argument('pwd')
  # return super().add_arguments(parser)

 def handle(self, *args, **kwargs):
  User = get_user_model()
  username= kwargs['user']
  email = kwargs['email']
  password = kwargs['pwd']
  if not User.objects.filter(username=username).exists():
   User.objects.create_superuser(username=username,
                                 email=email,
                                 password=password)
   self.stdout.write(self.style.SUCCESS('SuperUSer Created'))
  else:
   self.stdout.write(self.style.WARNING('superUSer Already Exists'))