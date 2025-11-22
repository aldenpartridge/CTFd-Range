import requests


def main():
    url = "FILL IN CTFD URL"
    token = "FILL IN TOKEN"

    # Create API Session
    url = url.strip("/")
    s = requests.Session()
    s.headers.update({"Authorization": f"Token {token}"})

    users = []
    q = s.get(f"{url}/api/v1/users").json()
    total_pages = q["meta"]["pagination"]["pages"]
    for i in range(1, total_pages + 1):
        users += s.get(f"{url}/api/v1/users?page={i}").json()["data"]

    print(f"Editting {len(users)} users")

    for user in users:
        r = s.patch(
            f"{url}/api/v1/users/{user['id']}",
            json={
                "website": "https://ctfd.io",
            },
            headers={"Content-Type": "application/json"},
        )
        print(r.json())


main()
