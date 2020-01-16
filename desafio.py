dicionario = {
    0: 'zero',
    1: 'um',
    2: 'dois',
    3: 'tres',
    4: 'quatro',
    5: 'cinco',
    6: 'seis',
    7: 'sete',
    8: 'oito',
    9: 'nove',
    10: 'dez',
    11: 'onze',
    12: 'doze',
    13: 'treze',
    14: 'quatorze',
    15: 'quinze',
    16: 'dezesseis',
    17: 'dezessete',
    18: 'dezoito',
    19: 'dezenove',
    20: 'vinte',
    30: 'trinta',
    40: 'quarenta',
    50: 'cinquenta',
    60: 'sessenta',
    70: 'setenta',
    80: 'oitenta',
    90: 'noventa',
    100: 'cento',
    200: 'duzentos',
    300: 'trezentos',
    400: 'quatrocentos',
    500: 'quinhentos',
    600: 'seissentos',
    700: 'setecentos',
    800: 'oitocentos',
    900: 'novecentos'
}



def extenso(numero):
    if (numero < -99999) | (numero > 99999):
        raise IOError

    sinal = ''
    if numero < 0:
        sinal = 'menos '
        numero = abs(numero)

    tamanho = len(str(numero))
    if tamanho <= 3:
        return sinal + centena_extenso(numero)

    milhar = int(numero / 1000)
    resto = numero % 1000
    if milhar == 1:
        if resto == 0:
            return sinal + 'mil'
        return sinal + 'mil e ' + centena_extenso(resto)
    if resto == 0:
        return sinal + centena_extenso(milhar) + ' mil'
    return sinal + centena_extenso(milhar) + ' mil e ' + centena_extenso(resto)


def centena_extenso(numero):
    tamanho = len(str(numero))
    if (tamanho <= 2) & (numero < 20):
        return dicionario[numero]

    expoente = tamanho - 1
    chave = int(numero / 10 ** expoente) * 10 ** expoente
    resto = numero % (10 ** expoente)
    if resto == 0:
        if chave == 100:
            return 'cem'
        return dicionario[chave]
    else:
        return dicionario[chave] + ' e ' + centena_extenso(resto)
