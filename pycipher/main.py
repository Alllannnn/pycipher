from pycipher.adfgx import ADFGX 
from pycipher.adfgvx import ADFGVX 
from pycipher.simplesubstitution import SimpleSubstitution
from pycipher.caesar import Caesar 
from pycipher.affine import Affine
from pycipher.autokey import Autokey 
from pycipher.beaufort import Beaufort 
from pycipher.vigenere import Vigenere 
from pycipher.atbash import Atbash
from pycipher.bifid import Bifid as Bifid


cipher= input("Enter cipher mech: ")
plaintext= input ("Enter plaintext: ")
if cipher == "adfgvx":
            ciphertext = ADFGX('ph0qg64mea1yl2nofdxkr3cvs5zw7bj9uti8','HELLO').encipher(plaintext)  
if cipher== "affine":  
            ciphertext = Affine(a,b).encipher(plaintext)     
if cipher== "atbash":  
            ciphertext = Atbash().encipher(plaintext)     
if cipher== "autokey":  
            ciphertext = Autokey('HELLO').encipher(plaintext)     
if cipher== "beaufort":
            ciphertext = Beaufort('HELLO').encipher(plaintext)     

if cipher== "bfid":  
            ciphertext = Bifid('phqgmeaylnofdxkrcvszwbuti',5).encipher(plaintext)     

if cipher== "simple substitution": 
            ciphertext = SimpleSubstitution('AJPCZWRLFBDKOTYUQGENHXMIVS').encipher(plaintext)     
 
if cipher== "caesar":  
            ciphertext = Caesar(3).encipher(plaintext)     

if cipher== "vigenere":  
            ciphertext = Vigenere('HELLO').encipher(plaintext)     

print (ciphertext)





