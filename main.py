
import csv
import matplotlib.pyplot as plt
import numpy

# ------------------------  function to read a csv file ----------------------------------
def readcsv():
    fields = []
    rows = []

    # reading csv file
    with open(r"C:\Users\admin\Downloads\brainstoke.csv", 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # extracting field names through first row
        fields = next(csvreader)

        # extracting each data row one by one
        for row in csvreader:
            rows.append(row)

        # get total number of rows
        print("Total no. of rows: %d" % (csvreader.line_num))

    # printing the field names
    print('Field names are:' + ', '.join(field for field in fields))

    # printing first 5 rows
    print('\nFirst 5 rows are:\n')
    for row in rows[:5]:
        # parsing each column of a row
        for col in row:
            print("%10s" % col, end=" "),
        print('\n')
    return fields
# ------------------------  function to append a csv file ----------------------------------

def addarec(fields):
    rows=[[5112,"female",76,1,0,'yes','Self-employed','Urban',98.6,24,'never smoked',0]]

    # writing to csv file
    with open(r"C:\Users\admin\Downloads\brainstoke.csv", 'a') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        # writing the data rows
        csvwriter.writerows(rows)
        print('data added')

def updaterec():
    lines=[]
    id = input("Please enter an id to be updated.")
    ind = int(input('enter index :'))
    new = input('enter new value to be updated:')
    flag = 0
    with open(r"G:\Test projects\brainstoke.csv", 'r') as readfile:

        reader = csv.reader(readfile)

        for row in reader:

            lines.append(row)

            for field in row:

                if field == id:
                    flag = 1
                    row[ind] = new
                    print('succ')
        if flag == 0:
            print('record not found')

    with open(r"G:\Test projects\brainstoke.csv", 'w') as writefile:

        writer = csv.writer(writefile)

        writer.writerows(lines)
        print('updated')

def delete():
    lines = list()

    id = input("Please enter an id to be deleted.")

    with open(r"G:\Test projects\brainstoke.csv", 'r') as readFile:

        reader = csv.reader(readFile)

        for row in reader:

            lines.append(row)

            for field in row:

                if field == id:
                    lines.remove(row)

    with open(r"G:\Test projects\brainstoke.csv", 'w') as writeFile:

        writer = csv.writer(writeFile)

        writer.writerows(lines)
        print('deleted')




while(1):
    print("----------------------- MENU -----------------------")
    print("           1. DISPLAY THE DATASET")
    print("           2. APPEND IN THE DATASET")
    print("           3. DELETE FROM THE DATASET")
    print("           4. UPDATE THE DATASET")
    print("           5. FUNCTION 1")
    print("           6. FUNCTION 2")
    print("           7. FUNCTION 3")
    print("           8. EXIT")
    ch=int(input("ENTER YOUR CHOICE : "))
    if(ch==1):
        fields = readcsv()
    elif (ch==2):
        addarec(fields)
    elif(ch==3):
        delete()
    elif (ch == 4):
        updaterec()
    elif (ch == 5):
        pass
    elif (ch == 6):
        pass
    elif (ch == 7):
        pass
    elif (ch == 8):
        break
    else:
        print("INCORRECT CHOICE")
