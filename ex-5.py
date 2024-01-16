def main():
    lst = []
    with open('lorem.txt', 'r') as file:
        for row in file:
            print(row)
    print('End')


if __name__ == '__main__':
    main()
