from django.core.management import BaseCommand

from online_delivery.models import BaseUser


class Command(BaseCommand):

    def handle(self, *args, **options):
        if BaseUser.objects.count() == 0:
            username = "admin"
            password = "admin"
            print(f"Creating account for {username}")
            admin = BaseUser.objects.create_superuser(
                password=password, username=username
            )
            admin.is_active = True
            admin.is_admin = True
            admin.save()
        else:
            print("Admin accounts can only be initialized if no Accounts exist")
