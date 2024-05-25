def main():
    with open("numbers.txt", "r") as n:
        lines = "".join(n.readlines()).split(",")
        [print(n) for n in lines]

if __name__ == "__main__":
    main()       
   
