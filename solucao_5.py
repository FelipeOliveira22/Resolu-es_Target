import sys
import locale

sys.stdout.reconfigure(encoding='utf-8')

def inverter_string(s):
    invertida = ""
    for i in range(len(s) - 1, -1, -1):
        invertida += s[i]
    return invertida

string = input("Informe uma string para inverter: ")
print(f"String invertida: {inverter_string(string)}")
