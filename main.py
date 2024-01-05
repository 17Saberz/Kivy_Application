import random
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from io import BytesIO
from PIL import Image as PilImage
from kivy.core.image import Image as CoreImage

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
            self.texture = images['X']

def extract_texture(image):
    """
    Load image into bytes buffer, convert to texture data
    """
    data = BytesIO()
    image.save(data, format='png')
    data.seek(0)
    return CoreImage(BytesIO(data.read()), ext='png').texture


def load_cards():
    global images
    card_back = extract_texture(PilImage.open('D:/Work AI/AI/Boat Sensei/qivy/kivy_application/asserts/card_back.png'))
    images['X'] = card_back

    full_deck = PilImage.open('D:/Work AI/AI/Boat Sensei/qivy/kivy_application/asserts/decklist.png')

    for row in range(4):
        textures = []
        suit = list(images.keys())[row]

        for col in range(13):
            spacing = (col * card_width, row * card_height, (col + 1) * card_width, (row + 1) * card_height)
            cropped = full_deck.crop(spacing) 
            texture = extract_texture(cropped)
            textures.append(texture)

        images[suit] = textures

class Hand:
    values = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 10, 'Q': 10, 'K': 10}

    def __init__(self):
        self.cards = []