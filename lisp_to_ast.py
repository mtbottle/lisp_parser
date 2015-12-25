def split(string, char):
    return [x for x in string.split(char) if x]

def parse_lisp_root(lisp_code):
    """ Method to parse lisp code and turn it into an abstract syntax tree. 
        TODO: write some more description about the abstract syntax tree.

        ** very inefficient code
    """
    result, last_bracket = parse_lisp_helper(lisp_code)
    return result

def parse_lisp_helper(lisp_code):
    """Helper method to parse the internals of the lisp code
    return ast, index offset of the next )
    """
    lisp_code = lisp_code.strip()
    opening_bracket = lisp_code.find("(", 1)

    if lisp_code.startswith("("):
        lisp_code = lisp_code[1:]
    print lisp_code

    # base case
    if opening_bracket < 0:
        closing_bracket = lisp_code.find(")")
        print closing_bracket
        item = split(lisp_code[:closing_bracket], " ")
        if len(item) == 0:
            return None, closing_bracket+1
        if len(item) == 1:
            return item[0], closing_bracket
        return item, closing_bracket+1

    # inductive case
    ast = split(lisp_code[:opening_bracket], " ")
    closing_bracket = lisp_code[:opening_bracket].find(")")
    lisp_code = lisp_code[opening_bracket:]
    while opening_bracket > 0 or lisp_code:
        sub_ast, closing_bracket = parse_lisp_helper(lisp_code)
        if sub_ast:
            ast.append(sub_ast)
        lisp_code = lisp_code[closing_bracket:]
        opening_bracket = lisp_code.find("(")

    return ast, closing_bracket


if __name__ == "__main__":
    print parse_lisp_helper("(first (list 1 (+ 2 3) 9))")
