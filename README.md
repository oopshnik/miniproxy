# Miniproxy

**Miniproxy** is a versatile proxy management tool developed by Oopshnik. It allows users to select and connect to proxies for web scraping and browsing, with support for both custom and pre-defined proxy lists. It also handles proxy failures by allowing users to try different proxies until a working one is found.

## Features

- **Proxy Selection**: Choose proxies from a list or enter a custom proxy.
- **Proxy Testing**: Automatically tests proxies to ensure they are working before use.
- **Error Handling**: Provides clear feedback on proxy connection issues.
- **Random Proxy Selection**: Option to randomly select a proxy from the list.

## Requirements

- Python 3.6 or higher
- Selenium
- Requests
- Rich
- Firefox WebDriver (geckodriver)

## Installation

1. **Clone the repository**:

    ```sh
    git clone https://github.com/yourusername/miniproxy.git
    cd miniproxy
    ```

2. **Install the required packages**:

    ```sh
    pip install -r requirements.txt
    ```

    Create a `requirements.txt` file with the following content:

    ```
    requests
    selenium
    rich
    ```

3. **Download Firefox WebDriver**:

    - Download [geckodriver](https://github.com/mozilla/geckodriver/releases) suitable for your OS.
    - Place `geckodriver` in a directory included in your system's PATH or specify its location in the script.

## Usage

1. **Prepare a proxy list**:

    Create a file named `proxies.txt` in the same directory as the script, listing one proxy per line in the format `ip:port`.

2. **Run the script**:

    ```sh
    python miniproxy.py
    ```

3. **Follow the on-screen prompts**:

    - **[1] Use proxy from list**: Choose a proxy from a list or let the program select a random proxy.
    - **[2] Use custom proxy**: Enter a custom proxy when prompted.
    - **[99] Exit**: Exit the application.

## Example

```sh
[1] Use proxy from list
[2] Use custom proxy
[99] Exit
> 1
[1] Choice proxy from list
[2] Random proxy
> 2
