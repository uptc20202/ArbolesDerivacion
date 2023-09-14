class Node:
    def __init__(self, symbol):
        self.symbol = symbol
        self.left = None
        self.right = None

    def get_symbol(self):
        return self.symbol

    def set_symbol(self, symbol):
        self.symbol = symbol

    def get_left(self):
        return self.left

    def set_left(self, left):
        self.left = left

    def get_right(self):
        return self.right

    def set_right(self, right):
        self.right = right

    def add_to_bottom(self, node):
        actual = self
        while actual.right is not None:
            actual = actual.right
        actual.right = node
