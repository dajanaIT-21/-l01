# Needed to create random numbers to simulate dice roll
import random

# Initialise player scores to 0
Mängia1_score = 0
pc_score = 0
pank = 1000

# Repeat everything in this block 10 times
for i in range(10):

    # Generate random numbers between 1 and 6 for each player.
    Mängia1_value = random.randint(1, 6)
    pc_value = random.randint(1, 6)

    # Display the values
    Mängia1_pakkumine = random.randint(1, 101)
    print("Mängia 1 viskas: ", Mängia1_value)
    
    print("Arvuti viskas: ", pc_value)
    
    def total_bank(pank):
        pank = 1000
    while pank > 0:
        print(f"Sul on ${pank} su panga kontol.")
        bet = int(input("Sisesta oma panus: "))

 
    # Selection: based on comparison of the values, take the appropriate path through the code.
    if Mängia1_value > pc_value:
        print("Mängia 1 võidab.")
        print("Mängia 1 võidab kogu laual oleva raha:)")
        Mängia1_score = Mängia1_score +1  # This is how we increment a variable
    elif pc_value > Mängia1_value:
        print("Arvuti võidab")
        print("Arvuti võidab kogu laual oleva raha:)")
        pc_score = pc_score +1
    
    else:
        print("Sen viik")

    input("Vajuta et jätkata.")  # Wait for user input to proceed.

print("### Mäng läbi ###")
print("Mängia 1 score:", Mängia1_score)
print("Arvuti:", pc_score)