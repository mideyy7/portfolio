#Token types
INTEGER,PLUS,EOF = 'INTEGER','PLUS','EOF'

class Token:
    def __init__(self,type,value):
        self.type = type
        self.value = value

    def __str__(self):
        return 'Token({type},{value})'.format(type = self.type,value = repr(self.value))

    def __repr__(self):
        return self.__str__()


class Interpreter:
    def __init__(self,text):
        self.text = text
        self.pos = 0
        self.currToken = None

    def error(self):
        raise Exception('Error parsing input')

    def getNextToken(self):
        text = self.text
        if self.pos > len(text) - 1:
            return Token(EOF,None)

        currChar = text[self.pos]
        if currChar.isdigit():
            token = Token(INTEGER,int(currChar))
            self.pos += 1
            return token
        if currChar == '+':
            token = Token(PLUS,currChar)
            self.pos += 1
            return token
        self.error()


    def eat(self,tokenType):
        if self.currToken.type == tokenType:
            self.currToken = self.getNextToken()
        else:
            self.error()

    def expr(self):
        self.currToken = self.getNextToken()
        left = self.currToken
        self.eat(INTEGER)
        operator = self.currToken
        self.eat(PLUS)
        right = self.currToken
        self.eat(INTEGER)
        result = left.value + right.value
        return result


def main():
    while True:
        try:
            text = input('calc> ')
        except EOFError:
            break
        if not text:
            continue
        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)

if __name__ == '__main__':
    main()




