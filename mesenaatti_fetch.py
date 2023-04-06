import requests
import time
import sys
from datetime import datetime

WAIT = 5

def get_mesenaatti_data(campaing):
    response = requests.get(f'https://api-mesenaatti.karolina.io/agitator/campaigns/{campaing}/fi/')
    return response

def get_data(campaing):
    while True:
        resp = get_mesenaatti_data().json()
        summa_nyt = resp["campaign"]["funding_reached"]
        tavoite_max = resp["campaign"]["target_goal"]
        osallistujia = resp["campaign"]["number_of_backers"]

        now = datetime.now()
        print(f"Yhteensä: {summa_nyt}\nLisää tullut: {summa_nyt-ex_summa}")
        #print(f"""Saavutettu: {summa_nyt}\nJäljellä ennen 10 000 €: {10000-summa_nyt}\nOsallistujia: {osallistujia}\nRahaa per osallistuja: {summa_nyt/osallistujia}""")
        for remaining in range(WAIT, 0, -1):
            sys.stdout.write("\r")
            sys.stdout.write("{:2d} seconds remaining".format(remaining))
            sys.stdout.flush()
            time.sleep(1)
        print("\n")
        
get_data(campaing=0) # Campaing id
