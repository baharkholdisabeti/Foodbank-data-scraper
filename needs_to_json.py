import json

needs_arr = ["Cereal", "Oatmeal", "Pancake mix", "Fruits", "Vegetables", "Beef", "Poultry", "Meat", "Seafood", "Lunch Meat", "Beans", "Soup", "Peanut/Nut Butter", "Dried fruit", "Sauce", "Broth/Stock", "Bread"]
need_objects = []
count = 1
for need in needs_arr:
    need_object = {
        "pk": count,
        "model": "foodbank.need",
        "fields": {
            "need_str": needs_arr[count-1],
        },
    }
    need_objects.append(need_object)
    count += 1

with open('needs.json', 'w') as outfile:
    json.dump(need_objects, outfile)