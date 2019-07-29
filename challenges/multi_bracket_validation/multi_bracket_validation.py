from node_linked_list_stack import Stack

class BracketValidation(object):

    def __init__(self):
        self.brackets = Stack()

    def multi_bracket_validation(self, string):
        for char in string:
            if char == '(' or char == '{' or char == '[':
                self.brackets.push(char)

            if char == ')':
                if self.brackets.peek() == '(':
                    self.brackets.pop()
                else:
                    return False

            if char == '}':
                if self.brackets.peek() == '{':
                    self.brackets.pop()
                else:
                    return False

            if char == ']':
                if self.brackets.peek() == '[':
                    self.brackets.pop()
                else:
                    return False

        if self.brackets.peek():
            return False
        else:
            return True
