print("calculate sallary")

import sys

def main(hours, wage, bonus):
    print((hours*wage)+bonus)

if __name__ == "__main__":
    main(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))