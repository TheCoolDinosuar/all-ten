from math import floor
from random import choice
import time

import requests

from all_ten import all_ten

if __name__ == '__main__':
    # number of days since June 13, 2022
    num_days = floor((time.time() - 1655103600) / (60*60*24))
    website = None
    try:
        website = requests.get("https://beastacademy.com/all-ten")
    except Exception:
        pass # lol
    nums = []
    if website:
        # <Dumb text processing>
        begin = website.text.find("5556")
        end = website.text.find(']', begin)
        processed = ""
        for char in website.text[begin:end]:
            if char in [f'{i}' for i in range(10)]:
                processed += char
        for i in range(len(processed) // 4):
            nums.append(processed[4*i : 4*i + 4])

        # </Dumb text processing>
        
    else:
        print(f"An error occured.")
        print("Resorting to accessing static storage.")
        with open("nums.txt", "r") as f:
            while line := f.readline():
                nums.append(line[:-1])
    
    da_numbers = list(map(int, list(nums[num_days + 40])))
    # the expression for da_numbers might be different because of time
    # zones, not sure

    # Gets all solutions, chooses random ones
    results = all_ten(*da_numbers)
    print(f"Todays numbers are: {''.join(map(str, da_numbers))}")
    for i in range(1, 11):
        print(f"{i}: " + choice(list(results[i])))
            
            
