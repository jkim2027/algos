# The items were to be displayed in category groups.
# Given an array of objects that contain a category key,
# return a dict to group the objects by their category.
# Make the grouping case-insensitive.
# Bonus: allow the key that is grouped by to be provided.

objects = [
    {
        "name": "Baby Yoda",
        "category": "cute",
    },
    {
        "name": "Cricket Protein",
        "category": "food",
    },
    {
        "name": "Shibe",
        "category": "Cute",
    },
    {
        "name": "Ancient India",
        "category": "Cradle of Civilization",
    },
    {
        "name": "Wasp Crackers",
        "category": "Food",
    },
    {
        "name": "The Fertile Crescent",
        "category": "Cradle of Civilization",
    },
]

def categorize(items):
    result_dict = {}
    for item in items:
        lower_category = item['category'].lower()
        if lower_category not in result_dict:
            result_dict[lower_category] = []

        result_dict[lower_category].append(item)

    return result_dict

# expected = {
#     "cute": [
#         {
#             "name": "Baby Yoda",
#             "category": "cute",
#         },
#         {
#             "name": "Shibe",
#             "category": "Cute",
#         },
#     ],
#     "food": [
#         {
#             "name": "Cricket Protein",
#             "category": "food",
#         },
#         {
#             "name": "Wasp Crackers",
#             "category": "Food",
#         },
#     ],
#     "cradle of civilization": [
#         {
#             "name": "Ancient India",
#             "category": "Cradle of Civilization",
#         },
#         {
#             "name": "The Fertile Crescent",
#             "category": "Cradle of Civilization",
#         },
#     ],
# }