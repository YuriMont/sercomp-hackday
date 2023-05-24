# -*- coding: utf-8 -*-f
from zapv2 import ZAPv2
import time

zap = ZAPv2(apikey="7fcie5ps9cd8jhdns4tpukqtam", proxies={"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"})

target = "http://127.0.0.1:8080"

print("Iniciando ZAP Proxy...")
zap.core.new_session()
zap.core.access_url(target)
print("ZAP Proxy iniciado!")


zap.ascan.scan(target)


while int(zap.ascan.status()) < 100:
    print("Progresso do escaneamento: ",zap.ascan.status(), "%", sep="")
    time.sleep(5)

print("Escaneamento concluído!")

alerts = zap.core.alerts()
for alert in alerts:
    if alert['risk'] == 'Medium' or alert['risk'] == 'High':
        print("---")
        print("Severidade:", alert['risk'])
        print("")
        print("Descricao:", alert['description'])


print("ZAP encerrado.")