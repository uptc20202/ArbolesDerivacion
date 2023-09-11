class WordModel:
    def __init__(self, symbol):
        self.symbol = symbol

    def get_path_image(self):
        return "src/img/childNode.png"

    def get_symbol(self):
        return self.symbol

    def __str__(self):
        return self.symbol
