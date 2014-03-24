
def action(player):
    """This is our main game engine
    it should take all of the commands from the player
    and do the actions accordingly
    """
    
    list_of_commands =["move", "rest", "exit", "eat"]
    print list_of_commands
    action = raw_input("\nWhat will you do?")
    if action == "move":
        move(player)
    elif action == "eat":
        eat(player)
    elif action == "stats":
        status_update(player)
    elif action == "unequip":
        unequip_item(player)
    elif action == "equip":
        equip_item(player)
    elif action == "rest":
        rest(player)
    elif action == "exit":
        sys.exit(0)