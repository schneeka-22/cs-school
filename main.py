
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
    with open(r"G:\Test projects\brainstoke.csv", 'r') as csvfile:
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
    a = input("Enter id:")
    b = input("Enter gender:")
    c = input("Enter age:")
    d = input("Enter hypertension (0/1):")
    e = input("Enter 1 if heart disease and 0 if not any heart disease:")
    f = input("Enter marital status:")
    g = input("Enter residence(urban or rural:): ")
    v = input("Enter work type:")
    h = input("Enter avg_glucose_level :")
    i = input("Enter bmi: ")
    j = input("Enter smoking_status: ")
    l = input("Enter stroke: ")
    row = [[a, b, c, d, e, f, v, g, h, i, j, l]]
    # writing to csv file
    with open(r"G:\Test projects\brainstoke.csv", 'a') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        # writing the data rows
        csvwriter.writerows(row)
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
                    print('success')
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
font1 = {'family': 'serif', 'color': 'crimson', 'size': 20}
font2 = {'family': 'serif', 'color': 'darkgreen', 'size': 15}
# Which age group is most likely to suffer from a stroke?
def view_age_ar():

    sns.kdeplot(x=df.loc[df['stroke'] == 1]['age'], color='#1a759f', label='Stroke',fill=True)  # age grp graph probability distribution for stroke
    sns.kdeplot(x=df.loc[df['stroke'] == 0]['age'], color='#52b69a', label='healthy', fill=True)
    plt.legend(loc='upper left')
    plt.title('Age Distribution', fontdict=font1)
    plt.text(-3.48,0.035,'Age has a significant impact on strokes, and it can clearly be seen that strokes are \nhighest for elderly and middle aged adults, '
                      '\nwhere as negligible for younger people.',
             {'font':'Serif', 'size':'16','color': '#184e77'}, bbox=dict(facecolor='#52b69a', alpha=0.1))
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
    plt.text(-4.03, 818,
             'From the graph it is clear that the risk of stroke increases as one gets older',
             {'font': 'Serif', 'size': '14', 'color': '#184e77'}, bbox=dict(facecolor='#52b69a', alpha=0.1))
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

    plt.text(1.02,-0.95,
             'It can be inferred that smoking status \n doesnt have a big role when it comes to strokes'
             ' \n and that data can be deceiving sometimes',
             {'font': 'Serif', 'size': '14', 'color': '#184e77'}, bbox=dict(facecolor='#52b69a', alpha=0.1))
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.08), fancybox=True, shadow=True, ncol=5)

    plt.show()

# Does working conditions have any effect on the probability of getting a stroke
def wrkage_hyp():
    sns.kdeplot(x=df.loc[df['stroke'] == 1]['age'], color='#184e77', label='stroke', fill=True, )
    sns.kdeplot(x=df.loc[df['work_type'] == "Private"]['age'], color='#52b69a', label='Private', fill=True, )
    sns.kdeplot(x=df.loc[df['work_type'] == "Govt_job"]['age'], color='#bfd200', label='Govt_job', fill=True, )
    sns.kdeplot(x=df.loc[df['work_type'] == "Self-employed"]['age'], color='#52b69a', label='Self_employed',
                fill=True, )
    plt.legend(loc='upper left')
    props = dict(boxstyle='round,pad=0.1', facecolor='lightgrey', alpha=0.4)
    plt.text(-2.15,0.032, '  ANALYSIS:-\n From the graph we can infer that almost 70% of people who '
                          '\n are employed in different types of work have suffered through'
                          '\n  stroke and the stroke is more evident in the people of age 45-80 years.\n'
                          '\nDeeper insights:-'
                          '\n1.The highest  no. of people who suffered from stroke on the basis of their \nwork types are the employees engaged in the private sector.'
                          '\n2. The self employed people are the lowest among the sufferers of the \nstroke',
             bbox=props)
    plt.show()


# What is the influence of BMI on the possibility of a person to get a stroke?
def bmi_str_scatter():
    z = df['bmi']
    x = df['age']

    plt.title("Dependence of Stroke on BMI and Age", loc="right")
    plt.xlabel("Age")
    plt.ylabel("BMI")
    plt.scatter(x, z, marker="^", color='#52b69a')
    props = dict(boxstyle='round,pad=0.1', facecolor='lightgrey', alpha=0.4)
    plt.text(55,91, '  ANALYSIS:-\n  From the illustration we can infer that the people having high'
                      '\n  BMI and who are older are more likely to suffer a stroke, along with'
                      '\n  reference to the observation done previously, in the above graphs.', bbox=props)

    plt.show()


# what is the probability of  a female to suffer from stroke as compared to a male of respective ages?

def genage_str():
    plt.title("Relation between Stroke, Gender and Age", loc="right")
    sns.kdeplot(x=df.loc[df['gender'] == "Male"]['age'], color='#1a759f', label='Male', fill=True)
    sns.kdeplot(x=df.loc[df['gender'] == "Female"]['age'], color='#52b69a', label='Female', fill=True)
    sns.kdeplot(x=df.loc[df['stroke'] == 1]['age'], color='#184e77', label='Stroke', fill=True, )
    plt.legend(loc='upper left')
    props = dict(boxstyle='round,pad=0.1', facecolor='lightgrey', alpha=0.4)
    plt.text(-2.15,0.036, '  ANALYSIS:-\n From the data we can say that the males and females have'
                          '\n almost the same no. of people suffering from stroke, hence gender doesn’t'
                          '\n have any noticeable impact on the process of getting a stroke.', bbox=props)
    plt.show()


# For which range of BMI the stroke probability is greatest, what should be an ideal BMI of a person to stay away from stroke?

def bmi_str_line():
    y = df['stroke']
    x = df['bmi']
    plt.title('Relation between stroke and BMI', fontweight='heavy', fontstyle='italic'
              , loc='center')
    plt.xlabel('BMI', fontsize=18)
    plt.ylabel('stroke', fontsize=18)
    plt.bar(x, y, color='#52b69a')
    props = dict(boxstyle='round,pad=0.1', facecolor='lightgrey', alpha=0.1)
    plt.text(69,0.925, '  ANALYSIS:-\nBMI doesn’t exhibit any influential aspect alone on the chances'
                      '\n of getting a stroke, there is ambiguity, hence it alone can not be taken'
                      '\n alone as a deciding factor for the analysis.', bbox=props)
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
        wrkage_hyp()

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
