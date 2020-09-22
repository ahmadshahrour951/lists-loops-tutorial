# Q1
songs = ["ROCKSTAR", "Do It", "For The Night"]

# Q2
print(songs[0])
print(songs[-1])
print(songs[1:])

# Q3
songs[-1] = "Billie Jean"

# Q4
songs.extend(["Handle With Care", "Shine On You Crazy Diamond",
              "My Beautiful Dark Twisted Fantasy"])
del songs[4]

# Q6
animals = ["Cat", "Dog", "Bird"]
animals.append("Rat")
print(animals[2])
del animals[0]
for animal in animals:
    print(animal)
