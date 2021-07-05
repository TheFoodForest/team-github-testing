from little_lib import little_package

names = ["little name", "middle name", "big\nname"]

for n in names:
    a = little_package.little_class(name=n)
    a.identify()

print("mess you up")
