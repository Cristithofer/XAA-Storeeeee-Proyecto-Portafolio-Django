from django import forms
from .models import Producto, Categoria

class ProductoForm(forms.ModelForm):
    class Meta:
        model  = Producto
        fields = ['nombre', 'categoria', 'descripcion', 'precio', 'stock', 'imagen', 'disponible']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: Teclado Gamer RGB'
            }),
            'categoria': forms.Select(attrs={
                'class': 'form-select'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Descripcion del producto...'
            }),
            'precio': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: 19990',
                'min': 1
            }),
            'stock': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ej: 10',
                'min': 0
            }),
            'imagen': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
            'disponible': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre', '').strip()
        if len(nombre) < 3:
            raise forms.ValidationError('El nombre debe tener al menos 3 caracteres.')
        return nombre

    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio is None or precio <= 0:
            raise forms.ValidationError('El precio debe ser mayor a 0.')
        return precio

    def clean_stock(self):
        stock = self.cleaned_data.get('stock')
        if stock is None or stock < 0:
            raise forms.ValidationError('El stock no puede ser negativo.')
        return stock
