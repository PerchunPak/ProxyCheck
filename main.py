"""
Если честно я сам не до конца понимаю что тут хотел сделать автор, однако явно он эксперементировал
с модулем proxycheck, останется в репозитории скорее всего просто чтобы было
"""
from proxycheck import Blocking
import geoip2.database

ips_to_check = ['1.1.1.1', '8.8.8.8']
ips_found = []

PROXYCHECK_IO_TOKEN = ''

client = Blocking(
    key=PROXYCHECK_IO_TOKEN
)

for checkip in ips_to_check:
    print('Проверяю ' + checkip)
    ip = client.ip(checkip)
    risk = ip.risk()
    print('Риск IP: ' + str(risk))
    if risk == 100:
        ips_found.append(f"Риск IP: {str(risk)} у IP {checkip}, прокси: {ip.proxy()}")

    if risk:
       print('Найдено ' + checkip)
       ips_found.append(checkip)

print(ips_found)
client.close()


ips_found = []

with geoip2.database.Reader('./proxycheck/GeoIP2-City.mmdb') as reader:
   for checkip in ips_to_check:
       response = reader.anonymous_ip(checkip)
       ips_found.append(f'is_anonymous:{response.is_anonymous}'
                        f'is_anonymous_vpn:{response.is_anonymous_vpn}'
                        f'is_hosting_provider:{response.is_hosting_provider}'
                        f'is_public_proxy:{response.is_public_proxy}'
                        f'is_residential_proxy:{response.is_residential_proxy}'
                        f'is_tor_exit_node:{response.is_tor_exit_node}'
                        f'ip_address:{response.ip_address}')
print(ips_found)
