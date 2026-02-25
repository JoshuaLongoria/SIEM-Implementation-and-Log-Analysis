#Any scripts used to generate failed login attempts or simulate traffic.
#like wirting a custom parser to translate raw logs into readable fields.

import datetime
import random
import time

ips = ["192.168.1.100", "10.0.0.5", "185.220.101.3", "192.168.1.103"]
users = ["admin", "user1", "guest", "root", "service_account"]

def generate_failed_login():                                            #Function to generate a failed login attempt
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ip = random.choice(ips)
    user = random.choice(users)
    
    log_entry = f"{timestamp} - Failed login attempt from {ip} for user {user}\n"

    with open("failed_logins.log", "a") as log_file:                   #Append the log entry to a file
        log_file.write(log_entry)               
    print(f"Generated log entry: {log_entry.strip()}")

if __name__ == "__main__":
    print("starting SIEM log generator...")
    while True:
        generate_failed_login()
        time.sleep(random.uniform(1, 5))                             # Sleep for a random time between 1 and 5 seconds before generating the next log entry