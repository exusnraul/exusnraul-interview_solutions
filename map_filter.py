animals = ['dog','Mat','Hat', 'cat','     ','parrot', 'rabbit']
up_ann=list(filter(lambda animal:str.istitle(animal),animals)) #Returns only if the func returns True
# up_ann=list(filter(lambda animal:str.isspace(animal),animals)) #Returns only if the func returns True
print(up_ann)
uppered_animals = list(map(lambda animal: str.istitle(animal), animals))
print(uppered_animals)