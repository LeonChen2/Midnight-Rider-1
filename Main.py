# main.py
# Midnight Rider
# A text-based adventure game.
# Gamespot gives it 9 out of 10.
import random
import sys
import textwrap
import time
INTRODUCTION = """
WELCOME TO MIDNIGHT RIDER
WE'VE STOLEN A CAR. WE NEED TO GET IT HOME.
THE CAR IS SPECIAL.
THAT'S WHY THE GOVERNMENT WANTS IT.
WE CAN'T LET THEM HAVE IT.
ONE GOAL: SURVIVAL... and THE CAR
REACH THE END BEFORE THE MAN GON GETCHU.
------
"""

WIN = """
YOU PRESS THE BUTTON TO OPEN THE GATE.
THIS ISN'T THE FIRST TIME YOU'VE DONE THIS.
YOU CAN TIME IT PERFECTLY SO THAT YOU
SLIDE THE AR IN AS THE GATES CLOSE.

YOU KNOW YOU DID THE RIGHT THING.
THE GOVERNMENT WOULD HAVE TORN THE CAR APART.
ANALYSING IT, TESTING IT, THEN DESTROYING IT.

THEY DON'T KNOW IT'S SECRETS...
THAT IS GOLD THE KEY TO DIFFERENT WORLDS.

AS YOU STEP OUT OF THE VEHICLE, FIDO RUNS
UP TO YOU.
"THANK YOU FOR SAVING ME," HE SAYS.

AS YOU TAKE A COUPLE OF STEPS AWAY FROM THE CAR,
IT MAKES A STRANGE NOISE

BEFORE YOUR EYES, IT SHIFTS ITS SHAPE.
YOU'VE SEEN IT BEFORE, BUT ONLY ON TV.

"BUMBLEBEE?..."
"""

CHOICES = """
    ----
    A. Eat tofu
    S. Turn around and shoot at agents
    M. Drive at moderate speed.
    C. Speed ahead at full throttle
    D. Stop and Refuel (NO FOOD AVAILABLE)
    E. Status Check
    Q. QUIT 
    ----
"""

def type_text_output(string):
    for char in textwrap.dedent(INTRODUCTION):
        time.sleep(0.05)
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(1)

def main():
    # Display introduction
    type_text_output(INTRODUCTION)

    # CONSTANTS
    MAX_FUEL_LEVEL = 50
    MAX_DISTANCE_TRAVELED = 100
    MAX_TOFU = 3

    # Variables
    done = False

    kms_travelled = 99          # 100 km is the end
    agents_distance = -20       # 0 is the end
    turns = 0
    tofu = MAX_TOFU             # 3 is max
    fuel = MAX_FUEL_LEVEL       # max is 50L
    hunger = 0




    # MAIN LOOP
    while not done:
        # Random events
        # FIDO - refills your food (5%)
        if food < 3 and random.random() < 0.05:
            # Refill tofu
            tofu = MAX_TOFU
            # Player feedback
            print("******** You look at your tofu container")
            print("******** it is filled magically")
            print("******** \"You're welcome!'\", says a small voice")
            print("******** The dog used its magic tofu cooking skills")
        # Check if reached END GAME
        # WIN - Traveled the Distance Req'd
        if kms_travelled > MAX_DISTANCE_TRAVELED:
            time.sleep(2)
            type_text_output(WIN)
            # Print win scenario - STYLISTIC TYPING
            # Break
            break


        # Present the user their choices
        print(CHOICES)

        user_choice = input("What do you want to do? ").lower().strip("!,.?")

        if user_choice == "e":
            print(f"\t---Status Check---")
            print(f"\tkm travelled: {kms_travelled}")
            print(f"\tFuel remaining: {fuel}L")
            print(f"\tAgents are {abs(agents_distance)} kms behind")
            print(f"\tYou have {tofu} tofu left")
            print(f"\t--------\n")

        if user_choice == "a":
            if tofu > 0:
                tofu -= 1
                hunger = 0
                print()
                print("-------- Mmmm. Yummy tofu.")
                print("-------- Your hunger is sated.")
                print()
            else:
                print()
                print("-------- You have none left.")
                print()


        if user_choice == "s":

            random.randrange(1,5)



            players_distance_now = random.randrange(2, 6)
            agents_distance_now = random.randrange(1,5)

            fuel -= random.randrange(3, 9)
            kms_travelled += players_distance_now
            agents_distance -= players_distance_now - agents_distance_now

        if user_choice == "c":
            pass
            # Fast
            players_distance_now = random.randrange(10, 16)
            agents_distance_now = random.randrange(7, 15)

            # Burn fuel
            fuel -= random.randrange(5, 11)

            # Player distance traveled
            kms_travelled += players_distance_now

            # Agents distance traveled
            agents_distance -= players_distance_now - agents_distance_now

            # Feedback to player
            print()
            print("ZOOOOOOM")
            print(f"-------- You traveled {players_distance_now} kms.")
            print()

        if user_choice == "m":
            pass
            players_distance_now = random.randrange(5, 11)
            agents_distance_now = random.randrange(7, 15)
            fuel -= random.randrange(1, 7)
            kms_travelled += players_distance_now
            agents_distance -= players_distance_now - agents_distance_now
            print()
            print("You continue to travel at moderate speed")
            print(f"-------- You traveled {players_distance_now} kms.")
            print()



        if user_choice == "d":
            # Refueling
            # Fill up the fuel tank
            fuel = MAX_FUEL_LEVEL

            # Consider the agents coming closer
            agents_distance += random.randrange(7, 15)

            # Give player feedback
            print("-------- You filled the fuel tank.")
            print("-------- The agents got closer...")
            print("-------- ")
        elif user_choice == "q":
            done = True
            print("Thanks for playing. Play again soon!")

        time.sleep(1.5)

        # TODO: Change the environment based on
        #       user choice, and RNG
        # TODO: Random event generator


if __name__ == "__main__":
    main()