#!/usr/bin/python3
if __name__ == "__main__":
    with open("2.csv", 'r') as f:
        flag = 0
        id = 2
        for line in f:
            #print(line)
            if not line == '\n':
                if not str(id) in line:
                    print("User ID: Incorrect / ", end='')
                    flag = 1
                if not str("Ervin") in line:
                    print("Username: Incorrect")
                    flag = 1
        if flag == 0:
            print("User ID and Username: OK")
