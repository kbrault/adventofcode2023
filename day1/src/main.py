import re

def part1(filename: str) -> int: 
    with open(filename,'r') as file:
        total = 0
        for line in enumerate(file, 1):
            first_number = last_number = None
            for char in line[1]:
                if str(char).isdigit():
                    if first_number is None:
                        first_number = char
                    else:
                        last_number = char
                        
            if first_number is not None and last_number is not None:
                concatenated_int = int(str(first_number) + str(last_number))
            else:
                concatenated_int = int(str(first_number) + str(first_number))
                
            total += concatenated_int
            #print(f"{line} : {first_number} / {last_number} -> add {concatenated_int}, for a total of {total}")
        print(total)
            
def part1_oneliner(filename):
    print(sum([(listDigit:=re.findall(r'\d',line)) and int(listDigit[0]+listDigit[-1]) for line in {1:open(filename).read().strip() }[1].split('\n')]))
       
def main():
    part1("../input.txt")
    part1_oneliner("../input.txt")

if __name__ == "__main__":
    main()