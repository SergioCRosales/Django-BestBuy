from django.contrib import admin
from .models import BbCategoriesImport
from .models import BbDetailsImport
from .models import BbProductImages
from .models import BbProductImport
from .models import Databasechangelog
from .models import Databasechangeloglock
# Register your models here.
admin.site.register(BbCategoriesImport)
admin.site.register(BbDetailsImport)
admin.site.register(BbProductImages)
admin.site.register(BbProductImport)
admin.site.register(Databasechangelog)
admin.site.register(Databasechangeloglock)