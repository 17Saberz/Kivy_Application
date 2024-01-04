

card_width = 195
card_height = 303

images = {
    'D': [],   # list of image texture objects
    'C': [],
    'H': [],
    'S': [],
    'X': None  # card back texture object
}

class Card(Widget):
    suits = ['C', 'S', 'H', 'D']  # club, spade, heart, diamond
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
    index = {'A': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, 'T': 9, 'J': 10, 'Q': 11, 'K': 12}

    texture = ObjectProperty(None)

    def __init__(self, suit, rank, visible, **kwargs):
        super().__init__(**kwargs)

        if (suit in Card.suits) and (rank in Card.ranks):
            self.suit = suit
            self.rank = rank
        else:
            raise ValueError(f"Invalid card: {suit}{rank}")

        self.pos = (0, 0)
        self.size = (card_width, card_height)

        self.visible = visible
        self.set_visible(visible)

    def set_visible(self, visible=False):
        self.visible = visible
        if visible:
            self.texture = images[self.suit][Card.index[self.rank]]
        else:
            self.texture = images['X']  # card back