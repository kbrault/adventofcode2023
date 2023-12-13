import re

# very quick, unoptimized algo, I should have split(\n) the file to have a list of line
def part1(filename: str) -> int: 
    total = 0
    for line in open(filename).read().strip().split('\n'):                  # read line by line
        first_number = last_number = None                   
        for char in line:                                                   # read character by character
            if str(char).isdigit():                                         # if digit
                if first_number is None:                                    # if no first number setted
                    first_number = char
                else:
                    last_number = char                                      # anyway, last character is the last digit
                    
        if first_number is not None and last_number is not None:            # if both numbers are set, just parse theme
            concatenated_int = int(str(first_number) + str(last_number))
        else:
            concatenated_int = int(str(first_number) + str(first_number))   # if one of them is not setted, then the result is the same number twice
            
        total += concatenated_int
        #print(f"{line} : {first_number} / {last_number} -> add {concatenated_int}, for a total of {total}")
    print(total)
            
# one liner because why not
def part1_oneliner(filename):
    print(sum([(listDigit:=re.findall(r'\d',line)) and int(listDigit[0]+listDigit[-1]) for line in {1:open(filename).read().strip() }[1].split('\n')]))
       
# probably a better way to do it without regex
def part2(filename):
    numbers = {'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine': '9'}
    total = 0
    
    for line in open(filename).read().strip().split('\n'):
        digits = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)
        current = ''.join([numbers[digit] if digit.isalpha() else digit for digit in [digits[0], digits[-1]]])
        total += int(current)
        #print(f"{line} -> {current}, total = {total}")
    
    print(total)
    
       
def main():
    part1("../input.txt")
    part1_oneliner("../input.txt")
    part2("../input.txt")

if __name__ == "__main__":
    main()