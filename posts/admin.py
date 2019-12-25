
from django.contrib import admin

from .models import Post,Posted

admin.site.register(Posted)
admin.site.register(Post)