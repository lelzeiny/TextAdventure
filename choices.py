start = '''
You walking through the woods with your dog Spot. Suddenly he sees a squirrel.
The next thing you know you know, he is dragging you through a scary graveyard.
You are lost and lost Spot. You search your surroundings to find an ominous house.
Standing on the doorstep, you are unsure of what to do.

'''
incorrect = 0


print(start)


print("Type 'ring' to ring the doorbell or 'enter' to enter without asking")
user_input = input()
if user_input == "ring":
    print("You decide to ring the doorbell and a skeleton greets you."
    "'Welcome.' he whispers. 'Follow me.' You are scared out of your mind. What should you do?")
    print("Type'go' to follow him or 'run' to escape.")
    user_input = input()
    if user_input == "go":
        print("You decide to be a brave soul and follow him. After all, who doesn't like a slim friend?")
        print("As you walk, things become awkward. The silence is killing you. You NEED to start conversation.")
        print("Make conversation by typing a noun you like")
        user_input = input()
        print("...")
        print ("He is not going to talk")
        print ("Suddenly, he says, 'I like " + user_input + " '")
        print ("You decide you like thin friends too. You become very good friends. GOOD GAME")
    elif user_input == "run":
        print ("You decide to be a whimp and run for your life, but you are such a whimp that you trip on a gravestone.")
        print ("Good job.")
        print ("A mob of zombies are angry because you disturbed them. They eat your brain.")
        print ("YOU DIED.")
    else:
        incorrect = 1
elif user_input == "enter":
    print("You choose to enter impolitely. Gain some manners. As a result of your incompetence, you fall through a trap door.")
    print("At the bottom, there is a vast room, with one door. You can't see all of it, except for a locked door in front of you. ")
    print("Type 'pound' to yell through the door or 'explore' to see the rest of the room")
    user_input = input()
    if user_input == "pound":
        print("A skeleton comes and saves you.")
        print("He begins to escort you out, but you don't want to leave just quite yet. You pipe up and say something.")
        print("Type 'tour' to ask for a tour or 'joke' to say a joke.")
        user_input = input()
        if user_input == "tour":
            print("You get a tour, and the house is phenomenal.")
            print("INDIFFERENT GAME.")
        elif user_input == "joke":
            print("You can only think of one joke, but don't know if it is appropriate.")
            print("Continue anyway? yes or no")
            user_input = input()
            if user_input == "yes":
                print("You say:'How much does a skeleton weigh? A skeleTON!'")
                print("The skeleton glares at you. 'GET OUT.'")
                print("You are escorted to the door to leave, but feel a little empty inside.")
                print("EMPTY GAME")
            elif user_input == "no"
                print("In the moment of silence, you can think of another joke.")
                print("You say,'I bought some shoes from a drug dealer. I'm not sure what he laced them with, but I've been trippin' all day'")
                print("He cracks a smile. You gain a connection")
                print("GOOD GAME")
            else:
                incorrect = 1
    elif user_input == "explore":
        print("You explore the room because you are an adventurer. However, your memory isn't very good.")
        print("You wander and wander and become a wandering soul.")
        print("WANDERING GAME")
    else:
        incorrect = 1
else:
    incorrect = 1
if incorrect ==1:
    print ("Incorrect input! Please copy the choices exactly.")
