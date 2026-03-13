from django.core.exceptions import ValidationError


def validacao_cpf(value):
    # Implementar lógica de validação de CPF aqui
    # Por enquanto, apenas verifica se possui 11 dígitos numéricos
    if not value.isdigit() or len(value) != 11:
        raise ValidationError('CPF inválido. Deve conter 11 dígitos numéricos.')
