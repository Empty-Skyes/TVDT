# Define the player character's name (you can ask the player for this if you want)
default pc_name = "Player"  # You can change this default name or prompt the player for input later

# Define the characters with their respective colors
define allen = Character("Allen", color="#ACE1FF")
define alice = Character("Alice Liddell", color="#FF69B4")
define bob = Character("Bob Smith", color="#ADD8E6")

init python:
    # Import the necessary classes
    from character import Character, CombatManager, PartyManager

    # Create the player character (pc_char) and other characters
    pc_char = Character("Player", "Hero", nickname="Hero")
    alice_char = Character("Alice Liddell", "Hero")
    bob_char = Character("Bob Smith", "Enemy")

    # Create PartyManager instance
    party_manager = PartyManager()

    # Add characters to their respective parties
    party_manager.add_to_player_party(pc_char)  # Add player character to player party
    party_manager.add_to_player_party(alice_char)  # Add Alice to player party
    party_manager.add_to_enemy_party(bob_char)  # Add Bob to enemy party

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
    "I’m armed with [pc_char.combat_equipment.weapon] and equipped with [pc_char.combat_equipment.armor]!"

    "Alice smiles at you, but Bob is standing off to the side, ready for a fight."

    show bob normal at left

    bob "Don't forget about me! I'm still stronger than anyone, no matter what they say."
    bob "After all, I've got this [bob_char.combat_equipment.weapon]. It's not just for show, you know!"

    "The battle is about to begin!"

    # Start combat loop
    jump combat_loop  # Jump into the combat loop

label combat_loop:

    # Show current HP of both the player and Bob
    $ player_hp = pc_char.stats.current_hp
    $ enemy_hp = bob_char.stats.current_hp

    "Your current HP: [player_hp]"
    "Bob's current HP: [enemy_hp]"

    # Alice provides encouragement or comments on the battle
    alice "Come on, [pc_name]! You can do this!"
    alice "Just keep your guard up, and you'll beat him!"

    # Loop through the player's party and let each character take their turn
    $ player_characters = party_manager.player_party
    $ index = 0  # Start with the first character in the party

    while index < len(player_characters):
        $ character = player_characters[index]

        # Player's turn: Choose Attack, Arte, or Defend
        menu:
            "Attack":
                $ result = combat_manager.player_turn("attack", character)
                "You attack with [character.names]! [result]"

            "Arte":
                $ result = combat_manager.player_turn("arte", character)
                "You use Arte with [character.names]! [result]"

            "Defend":
                $ result = combat_manager.player_turn("defend", character)
                "You defend with [character.names]! [result]"

        # Check if combat is over after player's turn
        $ combat_status = combat_manager.is_combat_over()
        if combat_status:
            "The battle is over! [combat_status]"
            jump combat_end  # Jump to the end of the combat when it's over
        else:
            "The battle continues..."

        # Move to the next character in the party
        $ index += 1

    # After all characters in the player party have taken their turns, it's the enemy's turn
    $ result = combat_manager.enemy_turn()
    "Bob attacks! [result]"

    # Alice comments on the outcome of the enemy's attack
    alice "Watch out, [pc_name]! That was a close one!"

    # Check if combat is over after enemy's turn
    $ combat_status = combat_manager.is_combat_over()
    if combat_status:
        "The battle is over! [combat_status]"
        jump combat_end  # Jump to the end of the combat when it's over
    else:
        "The battle continues..."

    # Return to the start of the combat loop
    jump combat_loop

label combat_end:
    # Ending the scene after the combat ends
    "With Bob defeated, Alice nods approvingly at your victory."
    "You’ve survived the battle. What’s next on your adventure?"

    return
