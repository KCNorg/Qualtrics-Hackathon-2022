# params = {'review': ['Food', 'Boarding'],
#           'info': [
#               {
#                   "name": "Travel Type",
#                   "values": ["Personal Travel"]
#               },
#               {
#                   "name": "Travel Class",
#                   "values": ["Eco", "Eco Plus"]
#               },
#               {
#                   "name": "Travel Distance",
#                   "values": ["Middle", "Long"]
#               },
#               {
#                   "name": "Gender",
#                   "values": ["Female", "Male"]
#               },
#               {
#                   "name": "Passenger Type",
#                   "values": ["Loyal customer", "Disloyal Customer"]
#               },
#               {
#                   "name": "Age",
#                   "values": ["Child", "Young Adult", "Mid Adult", "Elder"]
#               }
#           ]
#           }

names_into_indexes = {
    "Personal Travel": 0,
    "Business Travel": 1,
    "Business": 2,
    "Eco": 3,
    "Eco Plus": 4,
    "Short": 5,
    "Middle": 6,
    "Long": 7,
    "Female": 8,
    "Male": 9,
    "Loyal customer": 10,
    "Disloyal Customer": 11,
    "Child": 12,
    "Young Adult": 13,
    "Mid Adult": 14,
    "Elder": 15
}

indexes_into_names = {
    0: "Personal Travel",
    1: "Business Travel",
    2: "Business",
    3: "Eco",
    4: "Eco Plus",
    5: "Short",
    6: "Middle",
    7: "Long",
    8: "Female",
    9: "Male",
    10: "Loyal customer",
    11: "Disloyal Customer",
    12: "Child",
    13: "Young Adult",
    14: "Mid Adult",
    15: "Elder"
}


def parser_into_binary(params):
    res = [0 for _ in range(16)]

    for i in params:
        for j in i["values"]:
            res[names_into_indexes[j]] = 1
    return res


def parser_from_binary(binary):
    return [indexes_into_names[i] for i in range(16) if binary[i] == 1]


# print(parser_into_binary(params["info"]))
# print(parser_from_binary(parser_into_binary(params["info"])))
