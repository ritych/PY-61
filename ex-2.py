def main():
    file = open('lorem.txt')
    for row in file:
        print(row)
    file.close()


if __name__ == "__main__":
    main()
