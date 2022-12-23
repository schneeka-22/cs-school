
import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

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

df = pd.read_csv('https://raw.githubusercontent.com/schneeka-22/cs-school/master/brainstoke.csv')

# Which age group is most likely to suffer from a stroke?
def view_age_ar():

    sns.kdeplot(x=df.loc[df['stroke'] == 1]['age'], color='#1a759f', label='Stroke',fill=True)  # age grp graph probability distribution for stroke
    sns.kdeplot(x=df.loc[df['stroke'] == 0]['age'], color='#52b69a', label='healthy', fill=True)
    plt.legend(loc='upper left')
    plt.show()

def age_hist():


    x = np.arange(len(df))
    ages = df['age']
    binz = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
    labels = ['Children and teens', 'adults', 'middle age', 'elderly']
    freq, bin, patches = plt.hist(ages, bins=binz, edgecolor="black")

    print(freq)
    print(bin)
    print(patches)

    for i in range(0, 2):
        patches[i].set_facecolor('#184e77')
    for i in range(2, 4):
        patches[i].set_facecolor('#1a759f')
    for i in range(4, 6):
        patches[i].set_facecolor('#52b69a')
    for i in range(6, 8):
        patches[i].set_facecolor('#99d98c')
    for i in range(8, 9):
        patches[i].set_facecolor('#d9ed92')

    colors = ['#184e77', '#1a759f', '#52b69a', '#99d98c', '#d9ed92']

    font1 = {'family': 'serif', 'color': 'crimson', 'size': 20}
    font2 = {'family': 'serif', 'color': 'darkgreen', 'size': 15}

    plt.title("Age distribution of people who suffered from a stroke", fontdict=font1, loc="center")
    plt.xlabel("age in years", fontdict=font2)
    plt.ylabel("Number of people", fontdict=font2)
    from matplotlib.patches import Rectangle
    handles = [Rectangle((0, 0), 1, 1, color=c, ec='k') for c in colors]
    plt.legend(handles, labels, loc='upper center', bbox_to_anchor=(0.5, -0.08), fancybox=True, shadow=True, ncol=5)
    plt.show()

# What is the effect of smoking on the chances of having a stroke?
def pie_smoke():
    status = ['Never smoked', 'Formally Smoked', 'Smokes', 'Unknown']

    sizes = [144.684, 98.172, 67.176, 49.968]
    font1 = {'family': 'serif', 'color': 'crimson', 'size': 20}
    plt.title('Smoking status distribution', fontdict=font1)
    colors = ['#184e77', '#1a759f', '#52b69a', '#99d98c', '#d9ed92']

    plt.pie(sizes, labels=status, colors=colors, startangle=90, shadow=True, explode=(0, 0, 0.1, 0), radius=1.2,
            autopct='%1.1f%%', textprops={'color': '#f35b04', 'font': 'serif', 'fontsize': 15})


    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.08), fancybox=True, shadow=True, ncol=5)

    plt.show()

# Does working conditions have any effect on the probability of getting a stroke
def wrkage_str():
    plt.title("Relation between of work type and stroke",loc="right")
    sns.kdeplot(x=df.loc[df['stroke'] == 1]['age'], color='#184e77', label='stroke', fill=True,)
    sns.kdeplot(x=df.loc[df['work_type'] =="Private"]['age'], color='#52b69a', label='Private', fill=True,)
    sns.kdeplot(x=df.loc[df['work_type'] =="Govt_job" ]['age'], color='#bfd200', label='Govt_job', fill=True,)
    sns.kdeplot(x=df.loc[df['work_type'] =="Self_employed" ]['age'], color='#34aoa4', label='Self_employed', fill=True,)
    plt.legend(loc='upper left')
    plt.show()

# What is the influence of BMI on the possibility of a person to get a stroke?
def bmi_str_scatter():
  z = df['bmi']
  y = df[df['stroke']==1]
  x = df['age']
  plt.title("Dependence of Stroke on BMI and Age",loc="right")
  plt.xlabel("Age")
  plt.ylabel("BMI")
  plt.scatter(x,z,marker="^", color='#52b69a')
  plt.show()

# what is the probability of  a female to suffer from stroke as compared to a male of respective ages?

def genage_str():
    plt.title("Relation between Stroke, Gender and Age",loc="right")
    sns.kdeplot(x=df.loc[df['gender'] == "Male"]['age'], color='#1a759f', label='Male',fill=True)
    sns.kdeplot(x=df.loc[df['gender'] == "Female"]['age'], color='#52b69a', label='Female', fill=True)
    sns.kdeplot(x=df.loc[df['stroke'] == 1]['age'], color='#184e77', label='Stroke', fill=True,)
    plt.legend(loc='upper left')
    plt.show()

# For which range of BMI the stroke probability is greatest, what should be an ideal BMI of a person to stay away from stroke?

def bmi_str_line():
    y = df['stroke']
    x = df['bmi']
    plt.title("Relation between stroke and BMI", loc="right")
    plt.xlabel('BMI', fontsize=18)
    plt.ylabel('stroke', fontsize=12)
    plt.bar(x, y, color='#52b69a')
    plt.show()


while(1):
    print("----------------------- MENU -----------------------")
    print("           1. DISPLAY THE DATASET")
    print("           2. APPEND IN THE DATASET")
    print("           3. DELETE FROM THE DATASET")
    print("           4. UPDATE THE DATASET")
    print("           5. DISPLAY STATS OF NUMERIC DATA")
    print("           6. DISPLAY KDE PLOT FOR AGE DISTRIBUTION")
    print("           7. DISPLAY HISTOGRAM FOR VARIOUS AGE GROUPS WHO SUFFERED FROM A STROKE")
    print("           8. DISPLAY SMOKING STATUS DISTRIBUTION FOR STROKE PATIENTS")
    print("           9. SHOW RELATION BETWEEN WORK TYPE,AGE AND STROKE")
    print("           10. SCATTER PLOT FOR DEPENDENCE OF STROKE ON BMI AND AGE")
    print("           11. RELATION BETWEEN STROKE AND BOTH GENDERS OF RESPECTIVE AGES ")
    print("           12. RELATION BETWEEN BMI AND STROKE")
    print("           13. EXIT")
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
        print('non null value counts')
        df.info()
        print('stats of numeric categories')
        print(df.describe(exclude='object'))
    elif (ch == 6):
        view_age_ar()
    elif (ch == 7):
        age_hist()
    elif (ch == 8):
        pie_smoke()
    elif (ch == 9):
        wrkage_str()

    elif (ch == 10):
        bmi_str_scatter()
    elif (ch == 11):
        genage_str()
    elif (ch == 12):
        bmi_str_line()
    elif (ch == 13):
        print ('thank you')
        break
    else:
        print("INCORRECT CHOICE")
