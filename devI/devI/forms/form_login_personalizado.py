

class FormLoginPersonalizado():

    def __init__(self, *args, **kargs):

        super().__init__(*args, **kargs)
        for novo_campo in self.visible_fields():
            novo_campo.field.widget.attrs.update({"class": "form-control"})

            if len(novo_campo.errors) > 0:
                novo_campo.field.widget.attrs.update(
                    {"class": "form-control is-invalid"}
                )