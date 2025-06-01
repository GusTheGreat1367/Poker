import pydealer 
import pygame 
chips = pygame.image.load("Chips.png")
twoc = pygame.image.load("2_of_clubs.png")
twoh = pygame.image.load("2_of_hearts.png")
twod = pygame.image.load("2_of_diamonds.png")
twos = pygame.image.load("2_of_spades.png")
threec = pygame.image.load("3_of_clubs.png")
threeh = pygame.image.load("3_of_hearts.png")
threed = pygame.image.load("3_of_diamonds.png")
threes = pygame.image.load("3_of_spades.png")
fourc = pygame.image.load("4_of_clubs.png")
fourh = pygame.image.load("4_of_hearts.png")
fourd = pygame.image.load("4_of_diamonds.png")
fours = pygame.image.load("4_of_spades.png")
fivec = pygame.image.load("5_of_clubs.png")
fiveh = pygame.image.load("5_of_hearts.png")
fived = pygame.image.load("5_of_diamonds.png")
fives = pygame.image.load("5_of_spades.png")
sixc = pygame.image.load("6_of_clubs.png")
sixh = pygame.image.load("6_of_hearts.png")
sixd = pygame.image.load("6_of_diamonds.png")
sixes = pygame.image.load("6_of_spades.png")
seven_c = pygame.image.load("7_of_clubs.png")
seven_h = pygame.image.load("7_of_hearts.png")
seven_d = pygame.image.load("7_of_diamonds.png")
seven_s = pygame.image.load("7_of_spades.png")
eight_c = pygame.image.load("8_of_clubs.png")
eight_h = pygame.image.load("8_of_hearts.png")
eight_d = pygame.image.load("8_of_diamonds.png")
eight_s = pygame.image.load("8_of_spades.png")
nine_c = pygame.image.load("9_of_clubs.png")
nine_h = pygame.image.load("9_of_hearts.png")
nine_d = pygame.image.load("9_of_diamonds.png")
nine_s = pygame.image.load("9_of_spades.png")
ten_c = pygame.image.load("10_of_clubs.png")
ten_h = pygame.image.load("10_of_hearts.png")
ten_d = pygame.image.load("10_of_diamonds.png")
ten_s = pygame.image.load("10_of_spades.png")
jack_c = pygame.image.load("jack_of_clubs.png")
jack_h = pygame.image.load("jack_of_hearts.png")
jack_d = pygame.image.load("jack_of_diamonds.png")
jack_s = pygame.image.load("jack_of_spades.png")
queen_c = pygame.image.load("queen_of_clubs.png")
queen_h = pygame.image.load("queen_of_hearts.png")
queen_d = pygame.image.load("queen_of_diamonds.png")
queen_s = pygame.image.load("queen_of_spades.png")
king_c = pygame.image.load("king_of_clubs.png")
king_h = pygame.image.load("king_of_hearts.png")
king_d = pygame.image.load("king_of_diamonds.png")
king_s = pygame.image.load("king_of_spades.png")
ace_c = pygame.image.load("ace_of_clubs.png")
ace_h = pygame.image.load("ace_of_hearts.png")
ace_d = pygame.image.load("ace_of_diamonds.png")
ace_s = pygame.image.load("ace_of_spades.png")

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
    "king_of_clubs": king_c,
    "king_of_hearts": king_h,
    "king_of_diamonds": king_d,
    "king_of_spades": king_s,
    "ace_of_clubs": ace_c,
    "ace_of_hearts": ace_h,
    "ace_of_diamonds": ace_d,
    "ace_of_spades": ace_s
}
deck = pydealer.Deck()
deck.shuffle()

# Initialize pygame and create a window surface
pygame.init()
WIN = pygame.display.set_mode((800, 600))  # Set to your desired window size

def deal_cards(num_cards):
    hand = deck.deal(num_cards)
    return hand
BG = pygame.image.load("25200.jpg")  # Load your background image if needed
def display_hand(hand):
    x_position = 0
    y_position = 0
    for card in hand:
        card_name = f"{card.value.lower()}_of_{card.suit.lower()}"
        card_image = cards.get(card_name)
        if card_image:
            WIN.blit(card_image, (x_position, y_position))  # Replace with actual coordinates as needed
            x_position += 80  # Move x for next card
        print(f"Card: {card}, Image: {card_image}")  # Placeholder for actual rendering

def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        BG = pygame.image.load("25200.jpg")
        WIN.blit(BG, (0, 0))
        WIN.fill((0, 128, 0))  # Fill the window with a green background
        hand = deal_cards(5)  # Deal 5 cards
        display_hand(hand)  # Display the dealt hand
        pygame.display.flip()  # Update the display

    pygame.quit()                   
    
    hand = deal_cards(5)  # Deal 5 cards
    display_hand(hand)  # Display the dealt hand
    pygame.display.flip()  # Update the display

pygame.quit()
