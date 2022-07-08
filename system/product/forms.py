from django import forms
from .models import BbCategoriesImport
from .models import BbDetailsImport
from .models import BbProductImages
from .models import BbProductImport
from .models import Databasechangelog
from .models import Databasechangeloglock

class ProductForm(forms.ModelForm):
    class Meta:
        model = BbCategoriesImport
        fields = '__all__'

