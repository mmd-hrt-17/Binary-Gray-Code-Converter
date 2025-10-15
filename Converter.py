def Gray_to_Binary(gray:str):
    binary = ""
    binary += gray[0]
    
    for i in range(len(gray)-1):
        binary += str(int(binary[i]) ^ int(gray[i+1]))
        
    return binary


def Binary_to_Gray(binary:str):
    gray = ""
    gray += binary[0]
    
    for i in range(len(binary)-1):
        gray += str(int(binary[i]) ^ int(binary[i+1]))
        
    return gray


from colorama import Fore, Style

print(Fore.GREEN + "========================================" + Style.RESET_ALL)
print(Fore.RED + "Welcome to the --(Gray Code)-- Converter" + Style.RESET_ALL)
print(Fore.GREEN + "========================================" + Style.RESET_ALL)

print("Select Function:")
print("1. Gray to Binary")
print("2. Binary to Gray\n")

function = int(input())

if function == 1:
    code = str(input("Enter the gray code: "))
    print(Fore.CYAN + f"Binary Code: {Gray_to_Binary(code)}" + Style.RESET_ALL)
    
elif function == 2:
    code = str(input("Enter the binary code: "))
    print(Fore.CYAN + f"Gray Code: {Binary_to_Gray(code)}" + Style.RESET_ALL)
    
else:
    print(Fore.RED + "Invalid function" + Style.RESET_ALL)