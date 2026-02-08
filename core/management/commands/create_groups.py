from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group

class Command(BaseCommand):
    help = 'Create user groups for role-based authentication.'

    def handle(self, *args, **options):
        roles = ['freeUser', 'premiumUser', 'admin']
        for role in roles:
            group, created = Group.objects.get_or_create(name=role)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Grupo creado: {role}'))
            else:
                self.stdout.write(f'Grupo ya existe: {role}')
