"""
Uzrakstiet programmu definējot klasi,lai veselu skaitli pārveidotu par romiešu ciparu.

1) Kādus ciparus jūs zinat? Arābu.  10 cipari.    21
2) Kādus romiešu ciparus ziniet? I V C M X L D   XXI
3) Kas ir klase? programmēšanas struktūra kas var definēt datu uzvedību un metodes.
4) Klase sastāv no konstruktora/desturktora un metodēm (iekšējām funkcijām).
iekavas raksta parametrus, parametri ir klases mainigie
konstruktros parda kadi ieksejie mainigie darbosis
5) kadas datu strukturas zinat?
-list(sarakts) a=""
-arry(masīvs)
-dict(vārdnīca) a={} a=dict()
vardnicu var saprast kā tabula ar 2 kolonam
viena kolona ir atslega. otra kolona ir tās vērtība
"""
class AAA:
    # jādefinē konstruktors
    def __init__(self):
        self.roma_sk={
            1:'I',
            4:'IV',
            5:'V',
            9:'IX',
            10: 'X', 
            40: 'XL', 
            50: 'L', 
            90: 'XC', 
            100: 'C', 
            400: 'CD', 
            500: 'D', 
            900: 'CM', 
            1000: 'M'


        }
    #Definē nepieciešamās metodes
    def to_roman(self, num): 
        result = "" 
        for value, numeral in sorted(self.roma_sk.items(), key=lambda x: x[0], reverse=True): 
            while num >= value: 
                result += numeral 
                num -= value  #num=num-value
        return result

#piemērs
skaitlis=21
#define objekty
kk=AAA()
#jaunajam objektam jaizsacuc klases metode
romieshu=kk.to_roman(skaitlis)

# noformēt izdruku
print(f"{skaitlis} ar romiešu cipariem ir {romieshu}.")