import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)


def main():
    data = pd.read_csv('bikes.csv')
    summ = 0
    for el in data['Rachel1']:
        summ += el
    print(f'Sum = {summ}')


if __name__ == '__main__':
    main()
