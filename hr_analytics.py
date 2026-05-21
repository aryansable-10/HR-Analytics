"""HR analytics.ipynb

**Problem Statement**

1. Acomapany is facing the issue of employee attrition which is affection their business, deadlines are being delayed, projects stay imcomplete due to lack of expertise and experience.

2. So they have asked an analyst to find out what are the different reasons due to which the employees are resigning.

3. So the HR has surveyed the different employees from various departments and has provided a set of data.

-- **We as the analyst have to use this data to find out the various possible reasons due to which the employees are resigning and provide the inference to the HR**
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

df = pd.read_csv('/content/employe.csv')

df.head()

df.info()

"""# print 10 random rows from the data

"""

df.sample(10)

"""1. satisfactoryLevel - how much the employees are satisfied in the company
                    - ratings are on a scale of 0-1
possibility - if the satisfactory level is low the attrition chances would be high


2. lastEvaluation - last performance score , range 0-1
possibility - people with less evaluation will leave or even if people r having high evaluation but no salary hike

3. numberOfProjects - how many number of projects the person is working upon
possibility -


4. avgMonthlyHours - how much time on an average they are working
possibility - more working hrs = more work load
if the work hours are less they might not be interested in the work or maybe overstressed so they might also leave

5. timeSpent.company -- tenure, from how many years the employee is in the company
possibility -- more years with the company with no promotion and increment will leave,
if they have spent way too many years in the company they start to get comfortable and do not leave
if the people are freshers they might also think of staying in the company to gain some experience
if the people have been there in the company for an average years they might think of leaving for better oppurtunities

6. workAccident - any accident that would have occured during the work hours
only two values - 0 and 1

0 - false - no
1 - true - yes

if the value is 0 there's a high chance the employee will leave the company


if the value is 1 there's a high chance the employee will leave the company


8.promotionInLast5years -- if they have got any promotion in the previous 5 year


 if there is no promotion of employees they will see no growth and eventually they will leave and if they have been promoted they will stay


 9. dept -- various departments from where the data is completion_is_selected

10. salary -- the different salary levels the employees are getting is mentioned.

possibility - people who are getting low or high salary might have a tendency to leave.
"""

df.columns

# The different values inside the number of project col

df['numberOfProjects'].unique()

df['numberOfProjects'].value_counts() # along with the unique values we
# we also get the count that how many people are working on how many projects

df['workAccident'].unique()

df['promotionInLast5years'].unique()

df['dept'].value_counts()

df['salary'].value_counts()

"""Target column

"""

df['left'].unique()

"""1 - true --> the employee has left the company

 0 - false --> the employee is staying in the company

#Clean the dataset
"""

df.isnull().sum()

#duplicate is (3008)
df.duplicated().sum()

df.drop_duplicates(inplace=True)

#Remove duplicate
df.duplicated().sum()

df.shape

"""#Analysis with Visualisation"""

# Create a chart to show the distribution of employee turnover

sns.countplot(x='left', data=df)
plt.title("Employee Turnover Distribution")
plt.show()

"""# histogram and countplot -- both are frequency charts
# histogram is used when we have numerical data
# countplot is used when we have categorical data
1. trend analysis -- analysis over a period of time -- lineplot
2. compare categorical and numerical things -- bar chart
3. compare the proportions -- pie chart
4. compare two or more numerical variables -- scatter plot
5. compare all the numerical cols in dataset with each other -- pairwise comparison -- sns.pairplot
6. correlation between different cols -- heatmap
7. histogram and kde plots -- distribution of the data
8. outliers -- boxplot
"""

# affect of number of projects on employee attrition

x1 = sns.countplot(x='numberOfProjects', data = df, hue = 'left')
x1.bar_label(x1.containers[0])
x1.bar_label(x1.containers[1])
plt.show()

"""2 projects Employees may feel underutilized or bored. This can increase attrition.

3–5 projects Employees are properly engaged. Usually the lowest attrition rate occurs here.

6–7+ projects Employees may experience work overload or stress. This can increase attrition again

Find out the relationship between promotion and employee turnover.
"""

sns.countplot(x='promotionInLast5years', hue='left', data=df)

plt.xlabel("Promotion in Last 5 Years")
plt.ylabel("NO of Employees")
plt.title("Promotion vs Employee Turnover")

plt.legend(title="Left ", labels=["Stayed", "Left"])
plt.show()

"""Find out the relationship of the tenure and employee turnover"""

x1 = sns.countplot(x="timeSpent.company", hue="left", data=df)
x1.bar_label(x1.containers[0])
x1.bar_label(x1.containers[1])

plt.title("Employee Tenure vs Turnover")
plt.xlabel("Years Spent in Company")
plt.ylabel("Number of Employees")

plt.legend(title="Left", labels=["Stayed", "Left"])

plt.show()

"""filter the employees who got promotion but left"""

df1 = df[(df['promotionInLast5years']==1)&(df['left']==1)]

df1

"""# Create a scatter plot which shows the satisfactory level, no of projects, avgMonthlyHours"""

plt.figure(figsize=(4,4))
sns.scatterplot(x='avgMonthlyHours',y='numberOfProjects',data=df1,hue='satisfactoryLevel')
plt.show()

sns.scatterplot(x='avgMonthlyHours', y='satisfactoryLevel', hue='numberOfProjects',data=df1, palette='viridis')
plt.title('Satisfactory Level vs. Average Monthly Hours by Number of Projects')
plt.xlabel('Avg Monthly Hours')
plt.ylabel('Satisfactory Level')
plt.legend(title='Number Of Projects')
plt.show()
