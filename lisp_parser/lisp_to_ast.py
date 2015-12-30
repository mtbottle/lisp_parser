def split(string, char):
    return [x for x in string.split(char) if x]


def split_and_cast(string, split_char):
    split_string = split(string, split_char)
    return [float(x) if x.isnumeric() else x for x in split_string]


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
        return split_and_cast(lisp_code[start_index+1:first_closing_paren], " "), \
                first_closing_paren

    # inductive case
    ast = split_and_cast(lisp_code[start_index+1: next_opening_paren], " ")
    while next_opening_paren > 0 and lisp_code[first_closing_paren:]: 
        sub_ast, first_closing_paren = parse_lisp_helper(lisp_code,
                                                         next_opening_paren)
        ast.append(sub_ast)
        next_opening_paren = lisp_code.find("(", first_closing_paren+1)

        # add all the scalar values between the closing bracket, and next
        # opening bracket
        if next_opening_paren > 0 and next_opening_paren > first_closing_paren:
            values = split_and_cast(lisp_code[first_closing_paren+1:next_opening_paren], " ")
            ast.extend(values)


    # now finish parsing everything else after the last set of parens
    if first_closing_paren > -1:
        next_closing_paren = lisp_code.find(")", first_closing_paren+1)
        ast.extend(split_and_cast(lisp_code[first_closing_paren+1:next_closing_paren], \
                         " "))
    else:
        next_closing_paren = len(lisp_code)

    return ast, next_closing_paren


