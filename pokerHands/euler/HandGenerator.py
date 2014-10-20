class HandGenerator(object):
    def __init__(self, line_parser):
        self.__line_parser = line_parser

    def parse(self, lines):
        hands = []
        for line in lines:
            hands.append(self.__line_parser.parse(line))
        return hands