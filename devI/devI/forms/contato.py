from django import forms
from django.core.validators import MinLengthValidator


class ContatoForm(forms.Form):

    assunto = forms.CharField(
        max_length=200,
        label="Assunto",
        help_text="Assunto para o e-mail até 200 caracteres",
        validators=[
            MinLengthValidator(3)
        ],
    )

    remetente = forms.EmailField(
        label="E-mail",
        validators=[
            MinLengthValidator(5)
        ],
        help_text="E-mail do remetente para contato",
    )

    mensagem = forms.CharField(
        max_length=5000,
        label="Mensagem",
        help_text="Insira sua mensagem",
        validators=[
            MinLengthValidator(10)
        ],
        widget=forms.Textarea,
    )

    data = forms.DateField(label="Data de envio", widget=forms.DateInput)

    copia = forms.BooleanField(required=False, label="Desejo receber cópia")

    def __init__(self, *args, **kargs):

        super().__init__(*args, **kargs)
        for novo_campo in self.visible_fields():
            novo_campo.field.widget.attrs.update({"class": "form-control"})

            if len(novo_campo.errors) > 0:
                novo_campo.field.widget.attrs.update(
                    {"class": "form-control is-invalid"}
                )
        
        self.fields.get("copia").widget.attrs.pop("class", None)
