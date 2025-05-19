from django.contrib import admin

# Register your models here.

from .models import Vuz_1
from .models import Comments
from .models import Comments_2

admin.site.register(Vuz_1)

admin.site.register(Comments)
admin.site.register(Comments_2)