from django.contrib import admin

from .models import Option, Collect

from .models import Message

from .models import Mark

admin.site.register(Collect)
admin.site.register(Option)

admin.site.register(Message)

admin.site.register(Mark)


