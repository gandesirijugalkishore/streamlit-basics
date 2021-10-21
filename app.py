import streamlit as st
import pandas as pd
import numpy as np
import pickle
st.write("""
# STATISTICS FOR LIFE GRADES

STUDNET GRADE ANALYTICS

""")
user_input = st.number_input("NUMBER OF ASSIGNMENTS COMPLETED")
user_input=int(user_input)+1
st.sidebar.header('User Input Features')

st.sidebar.markdown("""
[Example CSV input file](https://raw.githubusercontent.com/dataprofessor/data/master/penguins_example.csv)
""")

# Collects user input features into dataframe
uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
# if uploaded_file is not None:
if uploaded_file is not None:
    input_df = pd.read_csv(uploaded_file)
    st.write(input_df.head())
    st.write("NUMBER OF STUDNETS",input_df["Student ID"].nunique())
    #filtering columns that starts with specific names and converted into a dataframe
    colsToScale=["Username","ASSIGNMENT", "LAB", "Assignment","Assignment","ASIGNMENT","Lab"]
    assign_df=input_df[input_df.columns[input_df.columns.str.startswith(tuple(colsToScale))]]
    st.write("USERNAME AND GRADES FOR COMPLETED LABS",assign_df)
    #NO.of students who have not submitted assignments
    no_of_rows = assign_df.shape[0]
    percentage_of_missing_data = assign_df.isnull().sum()
    st.write("NO.of students who have not submitted assignments",percentage_of_missing_data)
    #NO.of Assignments need to be graded
    st.write("NO.of Assignments need to be graded",assign_df.isin(['Needs Grading','Needs Grading(99.00)']).sum(axis=0))
    #Student Details with Username
    inp_uname = st.text_input("Username")
    st.write(input_df.loc[input_df['Username'] == inp_uname])
    
#     st.write(input_df.select_dtypes('object').nunique())
#     data=input_df.dropna(axis=1, how='all')
#     #filtering columns that starts with specific names and converted into a dataframe
#     colsToScale=["Username","ASSIGNMENT", "LAB", "Assignment","USERNAME","Lab"]
#     assign_df=data[data.columns[data.columns.str.startswith(tuple(colsToScale))]]
#     st.write(assign_df)
    
#     # lets check the percentage of missing data in each columns present in the data

#     no_of_rows = assign_df.shape[0]
#     percentage_of_missing_data = assign_df.isnull().sum()
#     st.write(percentage_of_missing_data)
    
#     #get stats based on assignemtn number
#     inp = st.number_input("ASSIGNMENTS NUMBER")
#     inp=int(inp)
#     x=assign_df.columns
#     print(x[inp])
#     no_of_rows = assign_df.shape[0]
#     sum_of_missing_data = assign_df[x[inp]].isnull().sum()
#     st.write("NUMBER OF STUDENTS WHO DID NOT SUBMIT",sum_of_missing_data)
    
#     #Total assignmetns
#     assign_user_df =  assign_df[["Username"]]
#     assign_user_df["Number of assignments not submitted"] = assign_df.isnull().sum(axis=1)
#     st.write(assign_user_df)
    
#     #User
#     user_input = st.text_input("Name")
#     assign_user_df.loc[assign_user_df['Username'] == user_input]
#     st.write(assign_user_df)

#     c=['Username',
#         'ASSIGNMENT # 1 [Total Pts: 100 Score] |1344236',
#        'ASSIGNMENT # 2 [Total Pts: 100 Score] |1344237',
#        'ASSIGNMENT # 3 [Total Pts: 100 Score] |1344238',
#        'Assignment # 4 [Total Pts: 100 Score] |1344239',
#        'Assignment # 5 [Total Pts: 100 Score] |1344240',
#        'ASSIGNMENT # 6 [Total Pts: 100 Score] |1344241',
#        'ASSIGNMENT # 7 [Total Pts: 100 Score] |1344242',
#        'ASSIGNMENT # 8 [Total Pts: 100 Score] |1344243',
#        'ASSIGNMENT # 9 [Total Pts: 100 Score] |1344244',
#        'ASSIGNMENT # 10 [Total Pts: 100 Score] |1344245']

#     st.write(input_df[c].isna().sum().rename("No. OF STUDNETS WHO DID NOT SUBMIT THE ASSIGNEMNT"))
#     grouped_df=input_df.groupby('Username')
#     grp=grouped_df.first()
#     st.write(grp.isnull().sum(axis=1).rename("Number of assignments not submitted"))
#     st.write(input_df["ASSIGNMENT # 1 [Total Pts: 100 Score] |1344236"].isna().groupby(input_df['Username']).sum())
#     df = input_df[c[0:user_input]].copy()
#     st.write(df)
#     st.write(input_df[input_df[c[user_input]].isna() == 1]["Username"].rename("STUDNETS NAMES"))
    
                                                 
else:
    st.write("""
# STATS LAB App

This app Give STATS FOR STATS LAB
""")
 


# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
# tickerSymbol = 'GOOGL'
#get data on this ticker
# tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
# tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open	High	Low	Close	Volume	Dividends	Stock Splits

# st.write("""
# ## Closing Price
# """)
# st.line_chart(tickerDf.Close)
# st.write("""
# ## Volume Price
# """)
# st.line_chart(tickerDf.Volume)












# import joblib
# import matplotlib.pyplot as plt
# import pandas as pd
# import streamlit as st

# st.title('Titanic Survival Analysis and Prediction')
# # load dataset
# df = pd.read_csv('titanic_train.csv')

# # show the entire dataframe
# st.write(df)

# # f-string
# st.subheader('Survival Rate')
# survival_count = df['Survived'].value_counts()
# st.text(f'Survival rate = {survival_count.values[1]/sum(survival_count):.2%}')

# # simple plotting
# fig, ax = plt.subplots(1, 2, figsize=(15, 5))
# survival_count.plot.bar(ax=ax[0])
# df['Age'].plot.hist(ax=ax[1])
# st.pyplot(fig)

# # markdown
# st.subheader('Making Prediction')
# st.markdown('**Please provide passenger information**:')  # you can use markdown like this

# # load models
# tree_clf = joblib.load('tree-clf.pickle')

# # get inputs

# sex = st.selectbox('Sex', ['female', 'male'])
# age = int(st.number_input('Age:', 0, 120, 20))
# sib_sp = int(st.number_input('# of siblings / spouses aboard:', 0, 10, 0))
# par_ch = int(st.number_input('# of parents / children aboard:', 0, 10, 0))
# pclass = st.selectbox('Ticket class (1 = 1st, 2 = 2nd, 3 = 3rd)', [1, 2, 3])
# fare = int(st.number_input('# of parents / children aboard:', 0, 100, 0))
# embarked = st.selectbox('Port of Embarkation (C = Cherbourg, Q = Queenstown, S = Southampton)', ['C', 'Q', 'S'])

# # this is how to dynamically change text
# prediction_state = st.markdown('calculating...')

# passenger = pd.DataFrame(
#     {
#         'Pclass': [pclass],
#         'Sex': [sex],
#         'Age': [age],
#         'SibSp': [sib_sp],
#         'Parch': [par_ch],
#         'Fare': [fare],
#         'Embarked': [embarked],
#     }
# )

# y_pred = tree_clf.predict(passenger)

# if y_pred[0] == 0:
#     msg = 'This passenger is predicted to be: **died**'
# else:
#     msg = 'This passenger is predicted to be: **survived**'

# prediction_state.markdown(msg)
