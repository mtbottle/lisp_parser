from lisp_parser.lisp_to_ast import parse_lisp_helper
import pytest

def test_parse_example():
    lisp_code = "(first (list 1 (+ 2 3) 9))"
    ast, final_bracket = parse_lisp_helper(lisp_code, 0)
    assert final_bracket == len(lisp_code) - 1
    assert ["first", ["list", 1, ["+", 2, 3], 9]] == ast

def test_parse_one_layer():
    lisp_code = "(list 8 9 3)"
    ast, final_bracket = parse_lisp_helper(lisp_code, 0)
    assert final_bracket == len(lisp_code) - 1
    assert ["list", 8, 9, 3] == ast


def test_parse_bracket_after_end():
    lisp_code = "(list 1 (+ 2 5) 4 (- 5 8))"
    ast, final_bracket = parse_lisp_helper(lisp_code, 0)
    assert ["list", 1, ["+", 2, 5], 4, ["-", 5, 8]] == ast

