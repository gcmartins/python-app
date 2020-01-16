from utils import dicionario


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

    return milhar_extenso(numero, sinal)


def milhar_extenso(numero, sinal):
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
