#game_objects.py

couch = {"name": "couch", "type": "furniture", "image":"couch.png"}

queen_bed = {"name": "queen bed", "type": "furniture", "image": "queen_bed.png" }

double_bed = {"name": "double bed", "type": "furniture", "image": "double_bed.png" }

dresser = {"name": "dresser", "type": "furniture", "image": "dresser.png"}

dining_table = {"name": "dining table", "type": "furniture", "image":"dining_table.png"}

door_a = {"name": "door a", "type": "door", "image":"door.png"}

door_b = {"name": "door b", "type": "door", "image":"door.png"}

door_c = {"name": "door c", "type": "door", "image":"door.png"}

door_d = {"name": "door d","type": "door", "image":"door.png"}

coins = {"name": "some spare change", "type": "misc"}

key_a = {"name": "key for door a", "type": "key", "target": door_a}

key_b = {"name": "key for door b", "type": "key", "target": door_b}

key_c = {"name": "key for door c", "type": "key", "target": door_c}

key_d = {"name": "key for door d", "type": "key", "target": door_d}

piano = {"name": "piano", "type": "furniture", "image":"piano.png"}

bedroom_1 = {"name": "bedroom 1", "type": "room"}

bedroom_2 = {"name": "bedroom 2", "type": "room"}

living_room = {"name": "the living room", "type": "room"}

game_room = {"name": "the game room", "type": "room"}

outside = {"name": "outside", "type": "room"}

all_rooms = [game_room, outside, living_room, bedroom_1, bedroom_2]

all_doors = [door_a, door_b, door_c, door_d]

#Initial object relations
object_relations = {
    "the game room": [couch, piano, door_a],
    "bedroom 1": [queen_bed, door_a, door_b, door_c],
    "bedroom 2": [double_bed, dresser, door_b],
    "the living room": [dining_table, door_c, door_d],
    "couch": [coins],
    "piano": [key_a],
    "queen bed": [key_b],
    "double bed": [key_c],
    "dresser": [key_d],
    "outside": [door_d],
    "door a": [game_room, bedroom_1],
    "door b": [bedroom_1, bedroom_2],
    "door c": [bedroom_1, living_room],
    "door d": [outside, living_room]
}


# Starting game state
game_state = {
    "current_room": game_room,
    "keys_collected": [],
    "target_room": outside
}
