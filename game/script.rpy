# Define the player character's name (you can ask the player for this if you want)
default pc_name = "Player"  # You can change this default name or prompt the player for input later

# Define Alice and Bob as Ren'Py characters with colors
define allen = Character("Allen", color="#ACE1FF")
define alice = Character("Alice Liddell", color="#FF69B4")
define bob = Character("Bob Smith", color="#ADD8E6")

init python:
    # Import the char Character class from the external Python file
    from character_classes import Character

    # Create instances of your char Character class for char attributes
    alice_char = Character("Alice Liddell", "Hero", nickname="Ally")
    bob_char = Character("Bob Smith", "Hero")

    # Set Alice's combat equipment
    alice_char.combat_equipment.weapon = "Sword"
    alice_char.combat_equipment.armor = "Steel Armor"
    bob_char.combat_equipment.weapon = "Axe"
    bob_char.combat_equipment.armor = "Iron Armor"

    # Set relationship between Alice and Bob
    alice_char.relationship_manager.set_relationship("allies", "Bob")
    bob_char.relationship_manager.set_relationship("allies", "Alice")

    # Adjust Alice's LP
    alice_char.relationship_manager.adjust_lp(10)

    # Capitalize Alice's nickname if it exists
    if alice_char.names.nickname:
        alice_char.names.nickname = alice_char.names.nickname.capitalize()

label start:

    # Ask for player name
    window hide
    $ pc_name = renpy.input("What is your name?", default="Mileena")
    window show

    "Nice to meet you, [pc_name]!"

     # Introduction scene
    scene bg room with fade
    show alice normal at center

    "You find yourself in a quiet room with a mysterious figure standing before you."

    alice "Hello, Hero! It's been a while, hasn't it? Or... should I call you [pc_name]?"

    # Display Alice's combat equipment (via char logic)
    "I’m armed with [alice_char.combat_equipment.weapon] and equipped with [alice_char.combat_equipment.armor]!"

    "Alice smiles proudly, radiating confidence. You nod approvingly."

    show bob normal at left

    bob "Don't forget about me! I'm still stronger than Alice, no matter what she says."
    bob "After all, I've got this [bob_char.combat_equipment.weapon]. It's not just for show, you know!"

    # Ending the scene
    "With tensions eased, Alice and Bob continue their friendly banter as you prepare for your next adventure."

    return
