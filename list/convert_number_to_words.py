def convert_to_words(num):  
    if int(num) == 0:  
        return "zero"  
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]  
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]  
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]  
    words = ""  
    if num>= 1000:  
        words += ones[num // 1000] + " thousand "  
    num %= 1000

    if num>= 100:  
        words += ones[num // 100] + " hundred "  
    num %= 100

    if num>= 20:  
        words += tens[num // 10] + " "  
        num %= 10

    if num>= 10 and num<= 19:  
        words += teens[num - 10] + " "  
        num = 0

    if num>= 1 and num<= 9:  
        words += ones[num] + " "

    return words.strip()  
num = int(input("Enter a number"))  
words = convert_to_words(num)  
print(words)
