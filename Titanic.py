#==============================================================================
# """
# Created on Feb 2017
# @author: Daerim Yang
# 
# Titanic - what sorts of people were likely to survive?
# """
#==============================================================================



#****************************************************************
#contents 
#0. Parameter Setting
#1. Check data
#2. Data convert
#3. Create new variables
#4. Machine learning technique : Random forest
#****************************************************************


#*************************
#0. Parameter Setting
#*************************


#/* 0.A import library */
import pandas as pd
import numpy as np

from sklearn import tree
from sklearn.ensemble import RandomForestClassifier



#/* 0.B Data import */


#DataFrame object
train_path = "C:\Users\9001340\Desktop\Titanic\Titanic\Titanic_train.csv"
train = pd.read_csv(train_path)

test_path = "C:\Users\9001340\Desktop\Titanic\Titanic\Titanic_test.csv"
test = pd.read_csv(test_path)





#*************************
#1. Check data
#*************************

#Check which variables are there in database
print train.head()
#==============================================================================
#    PassengerId  Survived  Pclass  \
# 0            1         0       3   
# 1            2         1       1   
# 2            3         1       3   
# 3            4         1       1   
# 4            5         0       3   
# 
#                                                 Name     Sex   Age  SibSp  \
# 0                            Braund, Mr. Owen Harris    male  22.0      1   
# 1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1   
# 2                             Heikkinen, Miss. Laina  female  26.0      0   
# 3       Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0      1   
# 4                           Allen, Mr. William Henry    male  35.0      0   
# 
#    Parch            Ticket     Fare Cabin Embarked  
# 0      0         A/5 21171   7.2500   NaN        S  
# 1      0          PC 17599  71.2833   C85        C  
# 2      0  STON/O2. 3101282   7.9250   NaN        S  
# 3      0            113803  53.1000  C123        S  
# 4      0            373450   8.0500   NaN        S  
#==============================================================================



#The number of rows * columns : (891,12)
train.shape



#Summary of variables
train.describe()

#==============================================================================
#        PassengerId    Survived      Pclass         Age       SibSp  \
# count   891.000000  891.000000  891.000000  714.000000  891.000000   
# mean    446.000000    0.383838    2.308642   29.699118    0.523008   
# std     257.353842    0.486592    0.836071   14.526497    1.102743   
# min       1.000000    0.000000    1.000000    0.420000    0.000000   
# 25%     223.500000    0.000000    2.000000         NaN    0.000000   
# 50%     446.000000    0.000000    3.000000         NaN    0.000000   
# 75%     668.500000    1.000000    3.000000         NaN    1.000000   
# max     891.000000    1.000000    3.000000   80.000000    8.000000   
# 
#             Parch        Fare  
# count  891.000000  891.000000  
# mean     0.381594   32.204208  
# std      0.806057   49.693429  
# min      0.000000    0.000000  
# 25%      0.000000    7.910400  
# 50%      0.000000   14.454200  
# 75%      0.000000   31.000000  
# max      6.000000  512.329200  
#==============================================================================


# Age variable has null value



# Get a basic information 
# Share and Survival rate by variables : value_counts() method   
# Sex / Pclass / Embarked
 
print train["Survived"].value_counts(normalize = True)
#0    0.616162
#1    0.383838

print train["Survived"][train["Sex"] == "male"].value_counts(normalize = True)
#0    0.811092
#1    0.188908

print train["Survived"][train["Sex"] == "female"].value_counts(normalize = True)    
#1    0.742038
#0    0.257962    
    
 
print train["Pclass"].value_counts()
print train["Survived"][train["Pclass"] == 1].value_counts(normalize = True)
print train["Survived"][train["Pclass"] == 2].value_counts(normalize = True)
print train["Survived"][train["Pclass"] == 3].value_counts(normalize = True)


print train["Embarked"].value_counts()
print train["Survived"][train["Embarked"] == "S"].value_counts(normalize = True)
print train["Survived"][train["Embarked"] == "C"].value_counts(normalize = True)
print train["Survived"][train["Embarked"] == "Q"].value_counts(normalize = True)







#*************************
#2. Data convert
#*************************


#Sex
train["Sex"][train["Sex"] == "male"] = 0
train["Sex"][train["Sex"] == "female"] = 1


#Embarked 
train["Embarked"][train["Embarked"] == "S"] = 0
train["Embarked"][train["Embarked"] == "C"] = 1
train["Embarked"][train["Embarked"] == "Q"] = 2


#Age
train["Age"] = train["Age"].fillna(train["Age"].median())


#Embarked
train["Embarked"] = train["Embarked"].fillna(0)







#*************************
#3. Create new variables
#*************************

#Idea :
#    
#    1. Age :
#        - Null Y/N                                         Age_Null
train["Age_null"] = 0
train["Age_null"][train["Age"].isnull()] = 1

#        - 10, 20, 30, 40, ...                              Age_ten
train["Age_ten"] = 0
#train["Age_ten"] = int(train["Age_ten"]/10) ????????????

#        - Child Y/N                                        Age_child
train["Age_child"] = 0
train["Age_child"][train["Age"] < 15] = 1

#        - the old Y/N                                      Age_senior
train["Age_senior"] = 0
train["Age_senior"][train["Age"] > 50] = 1

#        
#    2. SibSp / Parch :
#        - a number of family member (SibSp + Parch + 1)    Family
train["Family"] = train["SibSp"] + train["Parch"] + 1 

#        - Parch > 0, else                                  Parch_YN
train["Parch_YN"] = 0
train["Parch_YN"][train["Parch"] > 0] = 1

#        
#    3. Ticket :
#        - first character                                  Ticket_frst
#        - Char / Num                                       Ticket_CharNum
#        
#    4. Fare :
#        - 10, 20, 30, ...                                  Fare_ten
#        - 50, 100, 150, 200, ...                           Fare_fifty
#        
#    5. Cabin :
#        - Null Y/N                                         Cabin_null
train["Cabin_null"] = 0
train["Cabin_null"][train["Cabin"].isnull()] = 1

#        - first character                                  Cabin_first
#        
#    6. Name :
#        - Last name                                        Name_last
#        - Mr. / Mrs. / Miss.                               Name_wedding
    






# Starts from here






#*************************
#4. Machine learning technique : Random forest
#*************************


# First Trial
target = train["Survived"].values
factors_forest = train[["Pclass", "Age", "Sex", "Fare", "SibSp", "Parch", "Embarked",]].values






# Build Random forest
forest = RandomForestClassifier(max_depth = 10, min_samples_split=2, n_estimators = 100, random_state = 1)
my_forest = forest.fit(factors_forest, target)


# Print the score of the fitted random forest
print(my_forest.score(factors_forest, target)) # 0.939393939394
print(my_forest.feature_importances_)
# [ 0.10384741  0.20139027  0.31989322  0.24602858  0.05272693  0.04159232  0.03452128]


# Which one is the most significant variable?
# -> Sex









# Make a prediction of the test dataset



test_features = test[["Pclass", "Age", "Sex", "Fare", "SibSp", "Parch", "Embarked"]].values
pred_forest = my_forest.predict(test_features)

# Create a data frame with two columns: PassengerId & Survived. Survived contains your predictions
PassengerId =np.array(test["PassengerId"]).astype(int)
my_solution = pd.DataFrame(pred_forest, PassengerId, columns = ["Survived"])
print(my_solution)

# Check that your data frame has 418 entries
print(my_solution.shape)

# Write your solution to a csv file with the name my_solution.csv
my_solution.to_csv("my_solution_one.csv", index_label = ["PassengerId"])












# =============================

# Second Trial

# Utilize not only default variables but also created variables :
#       Age_Null Age_ten Age_child Age_senior Family Parch_YN Ticket_frst Ticket_CharNum Fare_ten
#       Fare_fifty Cabin_YN Cabin_first Name_last Name_wedding


target = train["Survived"].values
factors_forest2 = train[["Pclass", "Age", "Sex", "Fare", "SibSp", "Parch", "Embarked", "Age_null", "Age_child", "Age_senior", "Family", "Parch_YN", "Cabin_null"]].values


# Build Random forest
forest2 = RandomForestClassifier(max_depth = 10, min_samples_split=10, n_estimators = 100, random_state = 1)
my_forest2 = forest2.fit(factors_forest2, target)


# Print the score of the fitted random forest
print(my_forest2.score(factors_forest2, target))
print(my_forest2.feature_importances_)





# Which one is the most significant variable?












# Make a prediction of the test dataset

# Data process 

test["Sex"][test["Sex"] == "male"] = 0
test["Sex"][test["Sex"] == "female"] = 1
test["Embarked"][test["Embarked"] == "S"] = 0
test["Embarked"][test["Embarked"] == "C"] = 1
test["Embarked"][test["Embarked"] == "Q"] = 2
test["Age"] = test["Age"].fillna(test["Age"].median())
test["Embarked"] = test["Embarked"].fillna(0)
test["Age_null"] = 0
test["Age_null"][test["Age"].isnull()] = 1
test["Age_ten"] = 0
test["Age_child"] = 0
test["Age_child"][test["Age"] < 15] = 1
test["Age_senior"] = 0
test["Age_senior"][test["Age"] > 50] = 1
test["Family"] = test["SibSp"] + test["Parch"] + 1 
test["Parch_YN"] = 0
test["Parch_YN"][test["Parch"] > 0] = 1
test["Cabin_null"] = 0
test["Cabin_null"][test["Cabin"].isnull()] = 1






test_features2 = test[["Pclass", "Age", "Sex", "Fare", "SibSp", "Parch", "Embarked", "Age_null", "Age_child", "Age_senior", "Family", "Parch_YN", "Cabin_null"]].values
pred_forest2 = forest2.predict(test_features2)

# Create a data frame with two columns: PassengerId & Survived. Survived contains your predictions
PassengerId =np.array(test["PassengerId"]).astype(int)
my_solution = pd.DataFrame(pred_forest2, PassengerId, columns = ["Survived"])
print(my_solution)

# Check that your data frame has 418 entries
print(my_solution.shape)

# Write your solution to a csv file with the name my_solution.csv
my_solution.to_csv("my_solution_one.csv", index_label = ["PassengerId"])




