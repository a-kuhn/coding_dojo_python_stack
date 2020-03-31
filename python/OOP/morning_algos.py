def parenValid(str):
    switch = 0
    for i in str:
        if switch == -1:
            return False
        if i == "(":
            switch += 1
        elif i == ")":
            switch -= 1
    return switch == 0


# print(parenValid("Y(3(p)p(3)r)s"))
# print(parenValid("N(0(p)3"))
# print(parenValid("N(0)t ) 0(k"))
# print(parenValid("N(0)t ) 0(k"))
# print(parenValid("a(b))(c"))


def bracesValid(str):
    order = []
    for i in str:
        if i == "(" or i == "{" or i == "[":
            order += i
        if i == ")":
            if order[-1] != "(":
                return False
            order.pop()
        if i == "}":
            if order[-1] != "{":
                return False
            order.pop()
        if i == "]":
            if order[-1] != "[":
                return False
            order.pop()
    return order == []

print(bracesValid("W(a{t}s[o(n{ c}o)m]e )h[e{r}e]!"))
print(bracesValid("D(i{a}l[ t]o)n{e"))
print(bracesValid("A(1)s[O (n]0{t) 0}k"))