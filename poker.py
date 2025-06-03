import pydealer 
import pygame 

CARD_WIDTH, CARD_HEIGHT = 60, 90  # Set desired card size

pygame.init()
WIN = pygame.display.set_mode((800, 600))

def load_and_scale(filename):
    img = pygame.image.load(filename)
    return pygame.transform.scale(img, (CARD_WIDTH, CARD_HEIGHT))

chips = load_and_scale("Chips.png")
twoc = load_and_scale("2_of_clubs.png")
twoh = load_and_scale("2_of_hearts.png")
twod = load_and_scale("2_of_diamonds.png")
twos = load_and_scale("2_of_spades.png")
threec = load_and_scale("3_of_clubs.png")
threeh = load_and_scale("3_of_hearts.png")
threed = load_and_scale("3_of_diamonds.png")
threes = load_and_scale("3_of_spades.png")
fourc = load_and_scale("4_of_clubs.png")
fourh = load_and_scale("4_of_hearts.png")
fourd = load_and_scale("4_of_diamonds.png")
fours = load_and_scale("4_of_spades.png")
fivec = load_and_scale("5_of_clubs.png")
fiveh = load_and_scale("5_of_hearts.png")
fived = load_and_scale("5_of_diamonds.png")
fives = load_and_scale("5_of_spades.png")
sixc = load_and_scale("6_of_clubs.png")
sixh = load_and_scale("6_of_hearts.png")
sixd = load_and_scale("6_of_diamonds.png")
sixes = load_and_scale("6_of_spades.png")
seven_c = load_and_scale("7_of_clubs.png")
seven_h = load_and_scale("7_of_hearts.png")
seven_d = load_and_scale("7_of_diamonds.png")
seven_s = load_and_scale("7_of_spades.png")
eight_c = load_and_scale("8_of_clubs.png")
eight_h = load_and_scale("8_of_hearts.png")
eight_d = load_and_scale("8_of_diamonds.png")
eight_s = load_and_scale("8_of_spades.png")
nine_c = load_and_scale("9_of_clubs.png")
nine_h = load_and_scale("9_of_hearts.png")
nine_d = load_and_scale("9_of_diamonds.png")
nine_s = load_and_scale("9_of_spades.png")
ten_c = load_and_scale("10_of_clubs.png")
ten_h = load_and_scale("10_of_hearts.png")
ten_d = load_and_scale("10_of_diamonds.png")
ten_s = load_and_scale("10_of_spades.png")
jack_c = load_and_scale("jack_of_clubs.png")
jack_h = load_and_scale("jack_of_hearts.png")
jack_d = load_and_scale("jack_of_diamonds.png")
jack_s = load_and_scale("jack_of_spades.png")
queen_c = load_and_scale("queen_of_clubs.png")
queen_h = load_and_scale("queen_of_hearts.png")
queen_d = load_and_scale("queen_of_diamonds.png")
queen_s = load_and_scale("queen_of_spades.png")
king_c = load_and_scale("king_of_clubs.png")
king_h = load_and_scale("king_of_hearts.png")
king_d = load_and_scale("king_of_diamonds.png")
king_s = load_and_scale("king_of_spades.png")
ace_c = load_and_scale("ace_of_clubs.png")
ace_h = load_and_scale("ace_of_hearts.png")
ace_d = load_and_scale("ace_of_diamonds.png")
ace_s = load_and_scale("ace_of_spades.png")

cards = {
    "2_of_clubs": twoc,
    "2_of_hearts": twoh,
    "2_of_diamonds": twod,
    "2_of_spades": twos,
    "3_of_clubs": threec,
    "3_of_hearts": threeh,
    "3_of_diamonds": threed,
    "3_of_spades": threes,
    "4_of_clubs": fourc,
    "4_of_hearts": fourh,
    "4_of_diamonds": fourd,
    "4_of_spades": fours,
    "5_of_clubs": fivec,
    "5_of_hearts": fiveh,
    "5_of_diamonds": fived,
    "5_of_spades": fives,
    "6_of_clubs": sixc,
    "6_of_hearts": sixh,
    "6_of_diamonds": sixd,
    "6_of_spades": sixes,
    "7_of_clubs": seven_c,
    "7_of_hearts": seven_h,
    "7_of_diamonds": seven_d,
    "7_of_spades": seven_s,
    "8_of_clubs": eight_c,
    "8_of_hearts": eight_h,
    "8_of_diamonds": eight_d,
    "8_of_spades": eight_s,
    "9_of_clubs": nine_c,
    "9_of_hearts": nine_h,
    "9_of_diamonds": nine_d,
    "9_of_spades": nine_s,
    "10_of_clubs": ten_c,
    "10_of_hearts": ten_h,
    "10_of_diamonds": ten_d,
    "10_of_spades": ten_s,
    "jack_of_clubs": jack_c,
    "jack_of_hearts": jack_h,
    "jack_of_diamonds": jack_d,
    "jack_of_spades": jack_s,
    "queen_of_clubs": queen_c,
    "queen_of_hearts": queen_h,
    "queen_of_diamonds": queen_d,
    "queen_of_spades": queen_s,
    "king_of_clubs": king_c,
    "king_of_hearts": king_h,
    "king_of_diamonds": king_d,
    "king_of_spades": king_s,
    "ace_of_clubs": ace_c,
    "ace_of_hearts": ace_h,
    "ace_of_diamonds": ace_d,
    "ace_of_spades": ace_s
}

BG = pygame.image.load("25200.jpg")
BG = pygame.transform.scale(BG, (800, 600))

BG = pygame.image.load("25200.jpg")
BG = pygame.transform.scale(BG, (800, 600))

deck = pydealer.Deck()
deck.shuffle()

def deal_cards(num_cards):
    global deck
    if len(deck) < num_cards:
        deck = pydealer.Deck()
        deck.shuffle()
    deck.shuffle()  # Shuffle before each deal for more randomness
    hand = deck.deal(num_cards)
    return hand

def display_hand(hand):
    x_position = 20
    y_position = 400
    for card in hand:
        card_name = f"{card.value.lower()}_of_{card.suit.lower()}"
        card_image = cards.get(card_name)
        if card_image:
            WIN.blit(card_image, (x_position, y_position))
            x_position += CARD_WIDTH + 10  # Space between cards

def main():
    running = True
    hand = deal_cards(2)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                hand = deal_cards(5)  # Press SPACE to deal a new hand

        WIN.blit(BG, (0, 0))
        display_hand(hand)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
