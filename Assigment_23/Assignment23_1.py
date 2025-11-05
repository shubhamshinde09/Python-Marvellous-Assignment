import pandas as pd



def main():
    data = {'Name' : ['Amit', 'Sagar', 'Pooja'], 'Math' : [85,90,75], 'Science' : [92,88,80], 'English' : [75,80,82]}

    df = pd.DataFrame(data)     # dataframe 'df' created
    print(df)

    print("Shape of the dataframe : ", df.shape)
    print("Columns in the dataframe : ", df.columns.tolist())
    print("Data Type : ")
    print(df.dtypes)
    



if __name__ == "__main__":
    main()