#! python
import requests
from csv import DictReader


def main():
    url = "FILL IN CTFD URL"
    token = "FILL IN TOKEN"

    # Create API Session
    url = url.strip("/")
    s = requests.Session()
    s.headers.update({"Authorization": f"Token {token}"})

    # See users.csv example template at https://docs.ctfd.io/docs/imports/csv#users
    users = DictReader(open("users.csv"))

    for user in users:
        # Note that the notify parameter is being passed here so CTFd will send the 
        # user an email with their credentials after the account is created
        r = s.post(
            f"{url}/api/v1/users?notify=true",
            json={
                "name": user["name"],
                "email": user["email"],
                "password": user["password"],
                "type": "user",
                "verified": True,
                "hidden": False,
                "banned": False,
                "fields": [],
            },
            headers={"Content-Type": "application/json"},
        )
        print(r.json())


if __name__ == "__main__":
    main()
