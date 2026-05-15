from django.forms import ModelForm

# A classe ModelForm serve quando necessitamos de persistência de dados...

# A classe Form é utilizada para criar formulários, sem necessariamente ter a necessidade de persistir esses dados em um banco de dados.



class BaseForm(ModelForm):
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)

        for campo in self.visible_fields():
            campo.field.widget.attrs.update({"class": "form-control"})
            if len(campo.errors.data) > 0:
                campo.field.widget.attrs.update({"class": "form-control is-invalid"})
