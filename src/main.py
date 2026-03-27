# main.py
import os

def main():
    value = os.getenv("MY_ENV")

    print("MY_ENV =", value)

if __name__ == "__main__":
    main()
