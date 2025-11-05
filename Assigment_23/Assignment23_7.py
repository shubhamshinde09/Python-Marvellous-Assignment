
import pandas as pd
import matplotlib.pyplot as plt

def main():
    data = {'Name' : ['Amit', 'Sagar', 'Pooja'], 'Math' : [85,90,75], 'Science' : [92,88,80], 'English' : [75,80,82]}

    df = pd.DataFrame(data)     # dataframe 'df' create

    df['Total'] = df['Math'] + df['Science'] + df['English']
    print(df)

    # bar plot
    plt.figure(figsize=(8, 5))
    plt.bar(df['Name'], df['Total'])
    plt.title("Student name and Marks")
    plt.xlabel("Name of Student")
    plt.ylabel("Total Marks")

    plt.show()

            

if __name__ == "__main__":
    main()