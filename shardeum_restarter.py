import argparse
import time

import httpx


print("BOZE BLAGOSLAVI SVINARNIK_DAO_SOFTWARE\n" * 5)

parser = argparse.ArgumentParser(description="Shardeum Node Restarter")
parser.add_argument("-p", "--password", help="Enter your dashboard password", required=False)

password = parser.parse_args().password or input("Enter your dashboard Password: ")
ip = httpx.get("https://ipinfo.io/ip", verify=False).text

print(f"Server ip: {ip}")


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Content-Type': 'application/json',
    'Origin': f'https://{ip}:8080',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
}

client = httpx.Client(verify=False, timeout=120)


def login() -> str:
    r = client.post(
        f"https://{ip}:8080/auth/login",
        json={"password": password},
        headers=headers
    )
    assert r.status_code == 200, "Enter a valid password"

    return r.json()["accessToken"]


def start():
    r = client.post(
        f"https://{ip}:8080/api/node/start",
        headers=headers
    )
    assert r.json()["status"] == "ok", "Failed to start node"


def get_status():
    r = client.get(
        f"https://{ip}:8080/api/node/status",
        headers=headers
    )

    return r.json()


def main():
    access_token = login()
    headers["X-Api-Token"] = access_token
    
    while True:
        status = get_status()

        if status["state"] == "stopped":
            start()
            print("Node is restarted")

        time.sleep(10)


if __name__ == "__main__":
    main()
