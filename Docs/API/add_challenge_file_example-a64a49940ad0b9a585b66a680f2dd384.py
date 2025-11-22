import requests

url = "CTFD URL"
token = "CTFD ACCESS TOKEN"
challenge_id = 0  # Challenge ID
r = requests.post(
    f"{url}/api/v1/files",
    headers={"Authorization": f"Token {token}"},
    files=[
    	("file", open("test.txt", mode="rb"))
    ],
    data={"challenge_id": challenge_id, "type": "challenge"},
)
print(r.json())
