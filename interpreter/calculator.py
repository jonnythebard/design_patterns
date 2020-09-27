from interpreter.lexer import lex
from interpreter.parser import parse


def eval(input):
    tokens = lex(input)
    print(' '.join(map(str, tokens)))

    parsed = parse(tokens)
    print(f'{input} = {parsed.value}')


if __name__ == '__main__':
    eval('(13+4)-(12+1)')
    """
    1)
    Input string is given
    "(13+4)-(12+1)"
    
    2)
    Tokenize the string into mathematically meaningful way 
    ["(", "13", "+", ")", "-", "(", "12", "+", "1", ")"]
    
    Parser assumes the mathematical expression as a tree.
    Any subexpression should be wrapped by parenthesis.
                   "-"
          "+"                  "+"
    "13"       "4"       "12"       "1"
    
    3)
    Parser travels the tree in DFS fashion and reduces tree into one integer.
    First, parser recognizes 13 + 4 as subexpression and converts it to 17.
    
                    "-"
          "17"                 "+"
                         "12"       "1"
    
    4)
    Second, parser recognizes 12 + 1 as subexpression and converts it to 13.
    
                    "-"
          "17"                 "13"
          
    5)
    Third, parser recognizes 17 - 13 converts it to 4.
    
                    "4"
    
    """

    eval('1+(3-4)')
    # eval('(13+4)-(12+1)+(13+4)-(12+1)')

    # this won't work because parser cannot recognize subexpression
    eval('1+2+(3-4)')
