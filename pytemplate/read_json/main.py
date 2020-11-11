"""
main
"""

import json


def is_satisfied(type_data, list_data):
    return type_data == "general" and "2" in list_data


if __name__ == "__main__":
    with open("jokes.json", mode="r", encoding="utf-8") as file:
        jokes = json.load(file)

    joke_list = sorted(
        [j["id"] for j in jokes if is_satisfied(j["type"], j["list"])]
    )
    print(repr(joke_list))
