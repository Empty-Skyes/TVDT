define pc = Character("[pc]")
define alice = Character("Alice")
define bob = Character("Bob")

init:
    $ gc_pc = GameCharacter("Mileena", archetype=archer)
    $ gc_alice = GameCharacter("Alice Liddell")
    $ gc_bob = GameCharacter("Bob Smith")
    $ relationship_manager = RelationshipManager()

    $ relationship_manager.set_relationship(gc_pc, gc_alice, "allies")
    $ relationship_manager.set_relationship(gc_pc, gc_bob, "enemies")

label start:
    window hide
    $ pc_name = renpy.input("What is your name?", default="Mileena").strip()
    window show

    "Welcome, [pc_name]! The game is now ready to begin."

    menu:
        "Test":
            jump test
        "Exit":
            return
