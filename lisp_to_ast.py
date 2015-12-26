def split(string, char):
    return [x for x in string.split(char) if x]


def parse_lisp_root(lisp_code):
    """ Method to parse lisp code and turn it into an abstract syntax tree. 
        TODO: write some more description about the abstract syntax tree.

        ** very inefficient code
    """
    result, last_bracket = parse_lisp_helper(lisp_code)
    return result


def parse_lisp_helper(lisp_code, start_index):
    """ Helper method to parse the internals of the lisp code. 
        param lisp_code: The code we want to parse
        param start_index: The index of the opening bracket that we want to
                           parse.
        return ast: the abstract syntax tree
        return end_index: the index of the final parenthesis
    """
    assert lisp_code[start_index] == "("
    first_closing_paren = lisp_code.find(")", start_index)
    next_opening_paren = lisp_code.find("(", start_index+1)

    # base case, no more opening paren
    if next_opening_paren < 0 or next_opening_paren > first_closing_paren:
        return split(lisp_code[start_index+1:first_closing_paren], " "), \
                first_closing_paren

    # inductive case
    ast = split(lisp_code[start_index+1: next_opening_paren], " ")
    while next_opening_paren > 0 and lisp_code[first_closing_paren:]:
        sub_ast, first_closing_paren = parse_lisp_helper(lisp_code,
                                                         next_opening_paren)
        next_opening_paren = lisp_code.find("(", first_closing_paren+1)
        ast.append(sub_ast)

    # now finish parsing everything else after the last set of parens
    if first_closing_paren > -1:
        next_closing_paren = lisp_code.find(")", first_closing_paren+1)
        ast.extend(split(lisp_code[first_closing_paren+1:next_closing_paren], \
                         " "))
    else:
        next_closing_paren = len(lisp_code)

    return ast, next_closing_paren


if __name__ == "__main__":
    print parse_lisp_helper("(first (list 1 (+ 2 3) 9))", 0)
    print parse_lisp_helper("(first (list (+ 1 2) (- 4 1) 9 (+ 5 6)))", 0)
    print parse_lisp_helper("(list 8 9 3)", 0)
    print parse_lisp_helper("(cdr (list (car (list 1 (+ 2 5))) (- 2 4) 4 (- 5 8)))", 0)
