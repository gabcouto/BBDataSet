textfile = open("C:/Users/Gabriel Couto/Documents/repos/BBDataSet/BBDataSet/files/data/raw/csv/charts.csv")
lines = textfile.readlines()
for line in reversed(lines):
    print(line)
    print('-------------------------------------------')