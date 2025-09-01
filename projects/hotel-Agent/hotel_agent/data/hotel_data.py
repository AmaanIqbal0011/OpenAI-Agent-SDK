from agents import function_tool

@function_tool
def res_info():
  """Get Info about the Hotel based on a query """
  data = {
        "hotel_name": "The Grand Dine",
        "total_rooms": 200,
        "private_room": True,
        "number_of_private_rooms": 50,
        "numbers_of_room_available" : 150,
        "accounts":5,
        "tax":"Monthly paid 2500$"
    }
  return f'Our hotel {data['hotel_name']} has {data['total_rooms']} rooms, with {data['numbers_of_room_available']} available. and private rooms is {data["private_room"]} and number of private rooms is {data["number_of_private_rooms"]} and accounts is{data["accounts"]} and we pay tax{data["tax"]}'