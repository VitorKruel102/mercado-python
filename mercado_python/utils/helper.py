def formata_float_str_moeda(valor: float) -> str:
    valor = '{:.2f}'.format(valor)
    return f'R$ {valor}'