# Jen Nadeau

# instructions for the goal of the game and move commands
def show_instructions():
    # print a main menu and the commands
    print('CrossFit Text Adventure Game')
    print('Collect all 6 equipment items before seeing your Coach to win the game or owe your Coach 50 burpees!')
    print('Move commands: go South, go North, go East, go West')
    print("Add item to Inventory: get 'item name'")


def main():
    # player status
    def player_status():
        print('---------------------------')
        print('You are in the', current_room)
        print('Inventory:', inventory)
        if current_room != 'Lobby' and rooms[current_room]['item'] not in inventory:
            print('You see your', rooms[current_room]['item'] + '.')
        print('---------------------------')

    # A dictionary for the CrossFit text game
    # The dictionary linking a room to other rooms
    # and linking one item for each room except the Start room (Lobby)
    # and the room containing the villain (Workout Room).
    rooms = {
        'Lobby': {'South': 'Break Room', 'North': 'Cardio Room', 'East': 'Weight Room', 'West': 'Office'},
        'Break Room': {'North': 'Lobby', 'East': 'Bathroom', 'item': 'Sneakers'},
        'Bathroom': {'West': 'Break Room', 'item': 'Water bottle'},
        'Office': {'East': 'Lobby', 'item': 'Logbook'},
        'Cardio Room': {'South': 'Lobby', 'East': 'Equipment Room', 'item': 'Jump rope'},
        'Equipment Room': {'West': 'Cardio Room', 'item': 'Lifting belt'},
        'Weight Room': {'West': 'Lobby', 'North': 'Workout Room', 'item': 'Barbell'},
        'Workout Room': {'South': 'Weight Room', 'item': 'Coach'}  # villain
    }

    directions = ['North', 'South', 'East', 'West']
    items = ['Lifting belt', 'Jump rope', 'Logbook', 'Sneakers', 'Water bottle', 'Barbell']

    # define an inventory, which is initially empty
    inventory = []

    # start player in the Lobby
    current_room = 'Lobby'

    # show player game instructions
    show_instructions()

    # main game loop to move between rooms
    while True:
        player_status()
        move_command = input('Enter your move: ').split()
        if move_command[0] == 'go':
            if len(move_command) != 2:
                print('Invalid command!')
            elif move_command[1] in rooms[current_room]:
                current_room = rooms[current_room][move_command[1]]
                if current_room == 'Workout Room':
                    print("GAME OVER! You see your Coach before you picked up all of your equipment! 50 burpees!")
                    break
            elif move_command[1] not in directions:
                print('Invalid command!')
            elif move_command[1] not in rooms[current_room]:
                print("Can't go that way!")
            else:
                print('Invalid command!')
        elif move_command[0] == 'get':
            if len(move_command) == 1:
                print('Invalid command!')
            elif move_command[1] in rooms[current_room]['item'] and rooms[current_room]['item'] not in inventory:
                inventory.append(rooms[current_room]['item'])
                print(rooms[current_room]['item'], 'received!')
                if len(inventory) == 6:
                    print('You found all of your equipment! Enjoy your workout! Thanks for playing!')
                    break
            elif move_command[1] not in rooms[current_room]['item']:
                if move_command[1] in items:
                    print("Can't get", move_command[1] + '!')
                else:
                    print('Invalid command!')
            else:
                print('Invalid command!')
        else:
            print('Invalid command!')


main()
