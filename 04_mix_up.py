"""
04. mix_up

Dadas as strings a e b, retorne uma string com a e b separados
por um espaço '<a> <b>', além disso, troque os 2 primeiros caracteres
das duas strings.

Exemplo:
    'mix', 'pod' -> 'pox mid'
    'dog, 'dinner' -> 'dig donner'

Assuma que a e b tem tamanho 2 ou maior.
"""

## a, b, as váriaveis da função recebem que o stop do 3 caracter de b recebe o 3 de a, ou seja de mix pod vira pox mid,
#  e o 3 caracter de a, vai receber o 3 de b, a ordem começando com b[:2], ao em vez de a[:2] no começo do comando, 
# faz com que inverta as palavras também ao em vez de ser mid pox fica pox mid, as duas chaves dentro da string, precedendo
# a função format são importantes, caso só tenha uma, vai puxar só a, ou só b

def mix_up(a, b):
    # +++ SUA SOLUÇÃO +++
    a, b = b[:2] + a[2:], a[:2] + b[2:]
    return '{} {}'.format(a, b)


# --- Daqui para baixo são apenas códigos auxiliáries de teste. ---

def test(f, in_, expected):
    """
    Executa a função f com o parâmetro in_ e compara o resultado com expected.
    :return: Exibe uma mensagem indicando se a função f está correta ou não.
    """
    out = f(*in_)

    if out == expected:
        sign = '✅'
        info = ''
    else:
        sign = '❌'
        info = f'e o correto é {expected!r}'

    print(f'{sign} {f.__name__}{in_!r} retornou {out!r} {info}')


if __name__ == '__main__':
    # Testes que verificam o resultado do seu código em alguns cenários.
    test(mix_up, ('mix', 'pod'), 'pox mid')
    test(mix_up, ('dog', 'dinner'), 'dig donner')
    test(mix_up, ('gnash', 'sport'), 'spash gnort')
    test(mix_up, ('pezzy', 'firm'), 'fizzy perm')
