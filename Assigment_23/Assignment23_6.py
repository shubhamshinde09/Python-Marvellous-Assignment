
import pandas as pd


def main():
    data = {'Name' : ['Amit', 'Sagar', 'Pooja'], 'Math' : [85,90,75], 'Science' : [92,88,80], 'English' : [75,80,82]}

    df = pd.DataFrame(data)     # dataframe 'df' create

    df['Total'] = df['Math'] + df['Science'] + df['English']
    print(df)

    df.sort_values(by='Total', ascending=False, inplace=True)

    print("\nDataframe based on Total_Marks in Descending Order: ")
    print(df)

            

if __name__ == "__main__":
    main()