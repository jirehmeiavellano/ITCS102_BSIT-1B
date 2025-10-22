# CREATING A LIST IN PYTHON

print("Welcome to Anime Title Lister Program!\n")

anime = []

while True:
    title = input("Enter the Title of an Anime (then just type 'exit' to stop): ").lower()
    print(f"'{title}' has been added to your list")
    if title == 'exit':
        print("You have exited the anime entry program ;)\n")
        break
    anime.append(title)

print("This are the list of the anime title you have entered:")
numbering = 0
for list in anime:
    numbering += 1
    print(f" {numbering}.) {list}")
    
  