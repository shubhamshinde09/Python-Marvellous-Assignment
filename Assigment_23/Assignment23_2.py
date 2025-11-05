
import pandas as pd


def main():
    data = {'Name' : ['Amit', 'Sagar', 'Pooja'], 'Math' : [85,90,75], 'Science' : [92,88,80], 'English' : [75,80,82]}

    df = pd.DataFrame(data)     # dataframe 'df' created

    print("Statistical Data of the Dataset: ")
    print(df.describe())        # descriptive statistics

if __name__ == "__main__":
    main()