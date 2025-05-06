from tiger import Tiger
from gorilla import Gorilla

def main():
    tiger1 = Tiger("Shere Khan", 0, 5)
    gorilla1 = Gorilla("Koko", 1, 7)

    tiger1.eat()
    tiger1.sleep()
    tiger1.grow(3)
    tiger1.schleichen()

    print("-----")

    gorilla1.eat()
    gorilla1.sleep()
    gorilla1.grow(2)
    gorilla1.klettern()

if __name__ == "__main__":
    main()