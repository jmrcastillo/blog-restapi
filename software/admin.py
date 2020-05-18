from django.contrib import admin
from django.contrib.auth.models import Group, User

from .models import Blog


admin.site.register(Blog)
admin.site.unregister(Group)
admin.site.unregister(User)
