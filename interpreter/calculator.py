from interpreter.lexer import lex
from interpreter.parser import parse


def eval(input):
    tokens = lex(input)
    print(' '.join(map(str, tokens)))

    parsed = parse(tokens)
    print(f'{input} = {parsed.value}')


if __name__ == '__main__':
    eval('(13+4)-(12+1)')
    eval('1+(3-4)')

    # this won't work
    eval('1+2+(3-4)')
