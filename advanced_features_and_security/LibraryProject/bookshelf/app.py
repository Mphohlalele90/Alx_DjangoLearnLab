from django.apps import AppConfig
from django.contrib.auth.models import Group, Permission

class BookshelfConfig(AppConfig):
    name = 'bookshelf'

    def ready(self):
        from django.contrib.contenttypes.models import ContentType
        Book = self.get_model('Book')
        content_type = ContentType.objects.get_for_model(Book)

        perms = {
            "can_view": Permission.objects.get(codename="can_view", content_type=content_type),
            "can_create": Permission.objects.get(codename="can_create", content_type=content_type),
            "can_edit": Permission.objects.get(codename="can_edit", content_type=content_type),
            "can_delete": Permission.objects.get(codename="can_delete", content_type=content_type),
        }

        group_permissions = {
            "Viewers": [perms['can_view']],
            "Editors": [perms['can_view'], perms['can_create'], perms['can_edit']],
            "Admins": [perms['can_view'], perms['can_create'], perms['can_edit'], perms['can_delete']],
        }

        for group_name, perm_list in group_permissions.items():
            group, created = Group.objects.get_or_create(name=group_name)
            group.permissions.set(perm_list)