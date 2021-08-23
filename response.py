import samino
from urllib.request import urlopen
from threading import Thread



while True:
   print("v2 sessão...")
   try: 
      f = urlopen("https://aarrgh.000webhostapp.com/doctxt/links.txt")
      for l in f.readlines():
            us = l.decode('utf-8')
            cut = us.index(":")
            cutend = us.index(";")
            link = us[0:cut]
            did = us[cut+1:cutend]
            print(link)
            print(did)
            client=samino.Client(deviceId=did)
            uid=client.get_from_link(link).objectId

            def c():
               client.watch_ad(uid)

            for _ in range(250):
                    Thread(target=c).start()
                    
   except Exception as er:
         print(er)
