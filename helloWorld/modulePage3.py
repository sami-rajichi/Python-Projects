person = {
    "name" : "Sami RAJICHI",
    "age" : 19,
    "country" : "Tuisia"
}

class language:
    def __init__(e, name, creator, year):
        e.name = name
        e.creator = creator
        e.year = year
    def infos(e):
        print(e.name, e.creator, e.year)