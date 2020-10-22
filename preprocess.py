import fileinput
import glob

for name in glob.glob('data/*.ann'):
    for line in fileinput.FileInput(name, inplace=1):
        print(line.replace("\t", " "))