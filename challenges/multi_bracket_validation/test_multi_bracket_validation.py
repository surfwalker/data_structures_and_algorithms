from multi_bracket_validation import BracketValidation
from stack import Node, Stack
import pytest

def test_BracketValidation_class_exists():
    assert BracketValidation

def test_BracketValidation_class_instantiation():
    assert BracketValidation()

def test_Node_class_exists():
    assert Node

def test_Node_class_instantiation():
    assert Node('value')

def test_Stack_class_exists():
    assert Stack

def test_Stack_class_instantiation():
    assert Stack()

def test_consecutive_balanced_brackets():
    bracket_validation = BracketValidation()
    assert bracket_validation.multi_bracket_validation('(This)[will]{return True}') == True

def test_nested_balanced_brackets():
    bracket_validation = BracketValidation()
    assert bracket_validation.multi_bracket_validation('(This {will return} True)') == True

def test_nested_unbalanced_brackets():
    bracket_validation = BracketValidation()
    assert bracket_validation.multi_bracket_validation('[This will [return (False)') == False

def test_wrongly_matched_bracket():
    bracket_validation = BracketValidation()
    assert bracket_validation.multi_bracket_validation('{This[will} return False]') == False

def test_unbalanced_closing_bracket():
    bracket_validation = BracketValidation()
    assert bracket_validation.multi_bracket_validation('This will return False]') == False

def test_unbalanced_opening_bracket():
    bracket_validation = BracketValidation()
    assert bracket_validation.multi_bracket_validation('(This will return False') == False

def test_no_brackets():
    bracket_validation = BracketValidation()
    assert bracket_validation.multi_bracket_validation('This will return True') == True