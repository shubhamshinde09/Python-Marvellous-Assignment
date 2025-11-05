import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    data = {'Name' : ['Amit', 'Sagar', 'Pooja'], 'Math' : [85,90,75], 'Science' : [92,88,80], 'English' : [75,80,82]}

    df = pd.DataFrame(data)     # dataframe 'df' created
    # print(df)
    # print(df.describe())
    df['Total'] = df['Math'] + df['Science'] + df['English']

    df.insert(0, 'Gender', ['Male', 'Male', 'Female'])
    # print("\nDataframe after inserting Gender column : ")
    # print(df)
    
    # One Hot Encoding on Gender Column
    df = pd.get_dummies(df, columns=['Gender'], dtype=int, drop_first=True)

    # print("\nData Frame after One-Hot-Encoding : ")
    print(df)

    # Grouping
    grouped_data = df.groupby(['Gender_Male'])['Total'].mean()
    print("Data after Grouping Gender and Marks : ")
    print(grouped_data)


    # pie chart of subject marks for Sagar
    # Sagar_Subject_Marks = [df.at[1, 'Math'], df.at[1, 'Science'], df.at[1, 'English']]
    # Sagar_Subject_Labels = df.columns.tolist()
    # Sagar_Subject_Labels.remove('Name') 
    # Sagar_Subject_Labels.remove('Total')
    # Sagar_Subject_Labels.remove('Gender_Male')

    # plt.pie(Sagar_Subject_Marks, labels=Sagar_Subject_Labels)    
    # plt.show()

    df['Status'] = 'Fail'
    for i in range(len(df)):
        if(df.at[i, 'Total'] >= 250):
            df.at[i, 'Status'] = 'Pass'
    # print(df)



if __name__ == "__main__":
    main()
