
import requests
import json


def get_metar(ifdecoded):
    hdr = {"X-API-Key": "5e40fddcdfd44fbf8dc82f4e78"}
    if ifdecoded:
        req = requests.get("https://api.checkwx.com/metar/CYKF/decoded", headers=hdr)
    else:
        req = requests.get("https://api.checkwx.com/metar/CYKF", headers=hdr)

    print("Response from CheckWX.... \n")

    try:
        req.raise_for_status()
        resp = json.loads(req.text)
        data = json.dumps(resp, indent=1)
        # write data to json file
        with open('cykf_metar.json', 'w') as outfile:
            outfile.write(data)


    except requests.exceptions.HTTPError as e:
        print(e)

def get_taf(ifdecoded):
    hdr = {"X-API-Key": "5e40fddcdfd44fbf8dc82f4e78"}
    if (ifdecoded):
        req = requests.get("https://api.checkwx.com/taf/CYKF/decoded", headers=hdr)
    else:
        req = requests.get("https://api.checkwx.com/taf/CYKF", headers=hdr)

    print("Response from CheckWX.... \n")

    try:
        req.raise_for_status()
        resp = json.loads(req.text)
        data = json.dumps(resp, indent=1)
        # print(data)
        # write data to json file
        with open('cykf_taf.json', 'w') as outfile:
            outfile.write(data)

    except requests.exceptions.HTTPError as e:
        print(e)

def get_runway():
    return

def wind_pass(data):
    return True
def visibility_pass(data):
    
    return True



#------------------------------------------------
get_taf(True)
get_metar(True)


