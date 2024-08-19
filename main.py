import requests
import sys
import random
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from rich.console import Console
from rich.text import Text

console = Console()

console.print(Text("""        _      _                       
  _ __ (_)_ _ (_)_ __ _ _ _____ ___  _ 
 | '  \| | ' \| | '_ \ '_/ _ \ \ / || |
 |_|_|_|_|_||_|_| .__/_| \___/_\_\\_, |
                |_|               |__/ 
""", style="bold magenta"))

def load(filename):
    try:
        with open(filename, 'r') as file:
            proxies = [line.strip() for line in file]
        return proxies
    except FileNotFoundError:
        console.print(Text(f"Error: The file '{filename}' was not found.", style="bold red"))
        sys.exit(1)

def testr(proxy):
    proxies = {
        'http': f'http://{proxy}',
        'https': f'http://{proxy}',
    }
    try:
        response = requests.get('http://example.com', proxies=proxies, timeout=3)
        if response.status_code == 200:
            console.print(Text(f"Success with proxy {proxy}", style="bold green"))
            return True
        else:
            console.print(Text(f"Proxy {proxy} returned status code {response.status_code}", style="bold red"))
            return False
    except requests.exceptions.RequestException:
        console.print(Text(f"Failed to connect using proxy {proxy}. Please try another.", style="bold red"))
        return False

def launch(proxy):
    options = Options()
    options.add_argument(f'--proxy-server={proxy}')
    driver = webdriver.Firefox(options=options)
    driver.get('http://example.com')

def prompt():
    while True:
        custom_proxy = console.input(Text("Custom proxy (ip:port): ", style="cyan"))
        if testr(custom_proxy):
            console.print(Text(f"Connecting to proxy: {custom_proxy}", style="bold green"))
            launch(custom_proxy)
            break
        else:
            console.print(Text("Proxy failed. Please enter a new proxy.", style="yellow"))

def main(proxies):
    for proxy in proxies:
        if testr(proxy):
            console.print(Text(f"Connecting to proxy: {proxy}", style="bold green"))
            launch(proxy)
            break
        else:
            console.print(Text("Trying next proxy...", style="yellow"))
    else:
        console.print(Text("No working proxies found. Exiting...", style="bold red"))

if __name__ == '__main__':
    c = console.input(Text("""[1] Use proxy from list
[2] Use custom proxy
[99] Exit
                      
> """, style="bold yellow"))

    if c == "1":
        proxies = load('proxies.txt')
        if not proxies:
            console.print(Text("No proxies found in the list.", style="bold red"))
            sys.exit(1)
        choice = console.input(Text("[1]Choice proxy from list\n[2]Random proxy\n>", style="yellow"))
        if choice == "1":
            selected = int(console.input(Text("Choose a proxy by number: ", style="cyan"))) - 1
            if 0 <= selected < len(proxies):
                main(proxies[selected:])
            else:
                console.print(Text("Invalid selection.", style="bold red"))
        elif choice == "2":
            selected = random.randint(0, len(proxies) - 1)
            main([proxies[selected]])
        else:
            console.print(Text("Invalid option. Returning to menu.", style="bold red"))

    elif c == "2":
        prompt()
    elif c == "99":
        sys.exit()
    else:
        console.print(Text("Invalid option.", style="bold red"))
