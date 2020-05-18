from django.contrib import admin  # type: ignore
from django.contrib.auth.models import Group, User  # type: ignore

from .models import Blog


admin.site.register(Blog)
admin.site.unregister(Group)
admin.site.unregister(User)
