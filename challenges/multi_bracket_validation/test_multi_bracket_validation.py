from multi_bracket_validation import BracketValidation
from node_linked_list_stack import Stack

def test_class_exists():
    assert BracketValidation

def test_class_instantiation():
    assert BracketValidation()

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