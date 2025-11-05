
import pandas as pd


def main():
    data = {'Name' : ['Amit', 'Sagar', 'Pooja'], 'Math' : [85,90,75], 'Science' : [92,88,80], 'English' : [75,80,82]}

    df = pd.DataFrame(data)     # dataframe 'df' created

    print(df)
    df['Total'] = df['Math'] + df['Science'] + df['English']

    Result = []
    for i in range(len(df.index)):
        if(df.at[i, 'Science'] > 85):
            Result.append(df.at[i, 'Name'])

    print("Students who scored more than 85 in Science : ")
    for name in Result : 
        print(name)

            

if __name__ == "__main__":
    main()