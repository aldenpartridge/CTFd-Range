#! python
import requests
import sys

def main():
    try:
        url = sys.argv[1]
        token = sys.argv[2]
        user_id = sys.argv[3]
    except IndexError:
        print("Usage: python3 delete_user_example.py <url> <admin_token> <user_id>")
        sys.exit(1)

    # Create API Session
    url = url.strip("/")
    s = requests.Session()
    s.headers.update({"Authorization": f"Token {token}"})

    # NOTE: It is important below to set the json argument so that requests sets the Content-Type correctly.
    r = s.delete(f"{url}/api/v1/users/{user_id}", json="")
    print(r.json())


if __name__ == "__main__":
    main()
