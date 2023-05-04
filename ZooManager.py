from Zoo import Zoo
from ZooKeeper import ZooKeeper
from Elephant import Elephant
from Horse import Horse
from Lion import Lion
from Peacock import Peacock
from Tiger import Tiger


class ZooManager:
    feeding_list = []   # List to store the animals to feed
    healing_list = []   # List to store the animals to medicate

    tour = True     # Keeps the program running until it is told to end
    entrance_msg = "Welcome to the zoo.\nEnter the ZooKeeper's name: "
    name = input(entrance_msg).title()

    zoo = Zoo()
    zk = ZooKeeper(name)

    # String messages
    leave_msg = "\nThank you for touring the zoo.\nGoodbye."
    error_msg = "\nInstruction unclear.\nEnter 'help' for instructions"
    add_msg = "These animals can be added to the zoo:\nTiger, Lion, Horse, Elephant and Peacock."
    add_msg += "\nEnter the first letter in the animal's name to it to the zoo: "
    followup_msg = "\nPress 1 to View All Animals\nPress 2 To Feed Animals\nPress 3 to Give Animals Medicine"
    followup_msg += "\nOr you can add another animal by entering the first letter in their name: "
    feed_animal_msg = "\nWhich animal(s) do you want to feed?\nEnter the animal's name to feed or 'quit' to leave"
    heal_animal_msg = "\nWhich animal(s) do you want to medicate?"
    heal_animal_msg += "\nEnter the animal's name to medicate or 'quit' to leave"
    no_medicate = "No animals to medicate"
    no_feed = "No animals to feed"

    print("\nEnter 'help' for a repeat of the instructions")
    add_animal = input(add_msg).lower()

    # Beginning of the program
    while tour:
        try:
            # Creates tiger object and adds it to the zoo
            if add_animal == "t" or add_animal[0].lower() == "t":
                tiger = Tiger()
                tiger.set_name(input("\nEnter tiger name: "))
                zoo.add_animals(tiger)
                add_animal = input(followup_msg)

            # Creates elephant object and adds it to the zoo
            elif add_animal == "e":
                elephant = Elephant()
                elephant.set_name(input("\nEnter elephant name: "))
                zoo.add_animals(elephant)
                add_animal = input(followup_msg)

            # Creates horse object and adds it to the zoo
            elif add_animal == "h":
                horse = Horse()
                horse.set_name(input("\nEnter horse name: "))
                zoo.add_animals(horse)
                add_animal = input(followup_msg)

            # Creates lion object and adds it to the zoo
            elif add_animal == "l":
                lion = Lion()
                lion.set_name(input("\nEnter lion name: "))
                zoo.add_animals(lion)
                add_animal = input(followup_msg)

            # Creates peacock object and adds it to the zoo
            elif add_animal == "p":
                peacock = Peacock()
                peacock.set_name(input("\nEnter peacock name: "))
                zoo.add_animals(peacock)
                add_animal = input(followup_msg)

            # Displays beginning message
            elif add_animal == "help":
                add_animal = input(add_msg).lower()

            # Shows all the animals currently stored
            elif add_animal == "1":
                print("\nThese are all the animals currently in cages")
                zoo.show_animals()
                add_animal = input(followup_msg)

            # Allows for animals to be fed
            elif add_animal == "2":
                choice = int(input("\nEnter 1 to feed manually Or Enter 2 to feed all animals to full automatically: "))

                # Animals are manually fed with choice 1
                if choice == 1:
                    begin = True
                    feeding_list.clear()
                    zoo.show_animal_name()
                    print(feed_animal_msg)
                    if zoo.cages:
                        while begin:
                            feed = input(":").lower()
                            for animal in zoo.cages:
                                if animal.get_name() == feed:
                                    feeding_list.append(animal)  # Adds the animal I want to feed to a list
                                    print(f"{animal.get_name().title()} has been added to the feeding list")
                                elif feed == "quit":
                                    begin = False
                                elif feed == "help":
                                    print("Enter animal name")
                                    break

                    if feeding_list:
                        print(feeding_list)  # Prints out all objects in the list to feed
                        feed = int(input("Insert how much food to feed animal:  "))
                        if feed <= 0:
                            print("\nYou did not feed the animals")
                        else:
                            for feed_animal in feeding_list:  # Loops through animals in the feeding list and feeds them
                                zk.feed_animals(feed, feed_animal)
                    else:
                        print(f"\n{no_feed}")

                # Animals are automatically fed with choice 1
                elif choice == 2:
                    feeding_list.clear()
                    for animal in zoo.cages:
                        feeding_list.append(animal)

                    if feeding_list:
                        full = 5
                        for feed_animal in feeding_list:
                            feed = full - feed_animal.get_hunger_status()
                            if feed == 0:
                                print(f"\n{feed_animal.get_name().title()} is full")
                            else:
                                zk.feed_animals(feed, feed_animal)
                    else:
                        print(f"\n{no_feed}")
                else:
                    print("\nYou did not enter 1 or 2")

                add_animal = input(followup_msg)

            # Allows for animals to be medicated
            elif add_animal == "3":
                choice = int(input("\nEnter 1 to give medicate manually or Enter 2 to make all animals healthy: "))

                # Animals are manually medicated with choice 1
                if choice == 1:
                    begin = True
                    healing_list.clear()
                    zoo.show_animal_name()
                    print(heal_animal_msg)
                    if zoo.cages:
                        while begin:
                            heal = input(":").lower()
                            for animal in zoo.cages:
                                if animal.get_name() == heal:
                                    healing_list.append(animal)
                                    print(f"{animal.get_name().title()} has been added to the medicate list")
                                elif heal == "quit":
                                    begin = False
                                elif heal == "help":
                                    print("Enter animal name")
                                    break

                    if healing_list:
                        heal = int(input("\nInsert how much to medicate animal: "))
                        if heal <= 0:
                            print("\nYou did not medicate the animals")
                        else:
                            for heal_animal in healing_list:
                                zk.heal_animals(heal, heal_animal)
                    else:
                        print(f"\n{no_medicate}")

                # Animals are automatically medicated with choice 2
                elif choice == 2:
                    healing_list.clear()
                    for animal in zoo.cages:
                        healing_list.append(animal)

                    if healing_list:
                        full_health = 10
                        for heal_animal in healing_list:
                            heal = full_health - heal_animal.get_health_status()
                            if heal == 0:
                                print(f"\n{heal_animal.get_name().title()} is in perfect health")
                            else:
                                zk.heal_animals(heal, heal_animal)
                    else:
                        print(f"\n{no_medicate}")
                else:
                    print("\nYou did not enter 1 or 2")

                add_animal = input(followup_msg)

            elif add_animal == "quit":
                print(leave_msg)
                tour = False

            else:
                print(error_msg)
                add_animal = input(add_msg)

        except ValueError:
            print("\nInvalid Input")
