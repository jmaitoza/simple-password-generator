import string
import secrets

passLen = int(input("Input desired password length: "))
alphabet = string.ascii_letters + string.digits + string.punctuation
#Secrets.choice securly and randomly chooses char from desired range
generatedPassword = ''.join(secrets.choice(alphabet) for i in range (passLen))
print('Suggested password: ' + generatedPassword)
