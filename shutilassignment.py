import glob
import shutil
import os

from datetime import datetime

def printDates(dates):
      for i in range(len(dates)):
            print(dates[i])

      if __name__ == "__main__":

#set where the sorce of the files are
            source = '/Users/Jerem/Desktop/FolderA/'
            files = glob.glob("*.txt")
            files.sort(key=os.path.getmtime)

from datetime import datetime

with open('.txt') as f:
    sorted_lines = sorted([l.strip() for l in f.readlines()][5:],
                          key=lambda line: datetime.strptime(line.split(",")[0], "%Y-%m-%d %H:%M:%S"))
    for line in sorted_lines:
        print(line)
            #dates.sort(key = lambda date: datetime.strptime(date, '%d'))

            #printDates(dates)

#set the destination path to folderB
#destination = '/Users/Jerem/Desktop/FolderB/'
#files = os.listdir(source)

#for i in files:
      #we are saying more the files represented by "i" to their new destination
      #shutil.move(source+i, destination)
