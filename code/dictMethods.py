marks = {
    "rakhi": 29,
    "seerat":15,
    "acbd":22,
    "xyz":[1,2,3,4],
    1:"rakhi"
}

print(marks.items())

print(marks.keys())

print(marks.values())

marks.update({"rakhi":30,"sam":25})
print(marks)

print(marks.get("rakhi2")) #prints none
print(marks["rakhi2"]) #give errors