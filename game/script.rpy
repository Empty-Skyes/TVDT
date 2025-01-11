# Define the characters with their respective colors
define alice = Character("Alice Liddell", color="#FF69B4")
define bob = Character("Bob Smith", color="#ADD8E6")

init python:
    # Import necessary classes
    from character import Character
    from combat import CombatManager
    from party import PartyManager
    from equipment import Equipment

    # Create characters manually with the Character class
    alice_char = Character("Alice Liddell", equipment=Equipment(weapon="Staff", armor="Robe"))
    bob_char = Character("Bob Smith", nickname="Enemy", equipment=Equipment(weapon="Axe", armor="Chainmail"))

    # Create the player character with combat equipment
    player_equipment = Equipment(weapon="Sword", armor="Leather Armor")
    pc_char = Character(fullname="Player", equipment=player_equipment)

    # Create PartyManager instance and add characters to their respective parties
    party_manager = PartyManager()
    party_manager.add_to_player_party(pc_char)
    party_manager.add_to_player_party(alice)
    party_manager.add_to_enemy_party(bob)

    # Create the CombatManager with the party manager instance
    combat_manager = CombatManager(party_manager)

label start:
    # Ask for the player's name
    window hide
    $ pc_name = renpy.input("What is your name?", default="Hero")
    window show

    "Nice to meet you, [pc_name]!"

    # Introduction scene with Alice watching
    scene bg room with fade
    show alice normal at center

    "You find yourself in a quiet room with a mysterious figure standing before you."

    alice "Hello, Hero! It's been a while, hasn't it? Or... should I call you [pc_name]?"

    # Show PC's equipment
    "I’m armed with [pc_char.equipment.weapon] and equipped with [pc_char.equipment.armor]!"

    "Alice smiles at you, but Bob is standing off to the side, ready for a fight."

    show bob normal at left

    bob "Don't forget about me! I'm still stronger than anyone, no matter what they say."
    bob "After all, I've got this [bob_char.equipment.weapon]. It's not just for show, you know!"

    "The battle is about to begin!"

    # Start combat loop
    jump combat_loop  # Jump into the combat loop

label combat_loop:
    # A simple start for the combat loop.
    $ results = combat_manager.start_combat()

    # Display the results of the combat round
    python:
        for result in results:
            renpy.pause(0.5)
            renpy.say("Result: %s" % result)

    # Once combat ends, show a message
    if "The enemy party has been defeated!" in results:
        "You won the battle!"

    elif "The player party has been defeated!" in results:
        "You lost the battle!"

    return
