from django.contrib import admin

from .models import User, Publication, Client

admin.site.register(User)
admin.site.register(Publication)
admin.site.register(Client)
