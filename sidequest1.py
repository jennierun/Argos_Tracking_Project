#Set a variable to the CSV filename
the_filename = 'data/raw/MoveBank/Satellite tracking of black-capped petrels 2019-argos.csv'

with open(the_filename, "r") as file:
    text = file.read()

print(text)