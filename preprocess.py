import fileinput
import glob

for name in glob.glob('test/*.ann'):
    for line in fileinput.FileInput(name, inplace=1):
        print(line.replace("\t", " "))