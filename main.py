import proxycheck
import geoip2.database

# IPS to check
ips_to_check = ['1.1.1.1', '8.8.8.8']
ips_found = []

# Config
apitoken = '' # от proxycheck.io

# Code
client = proxycheck.Blocking(
    key=apitoken
)

for checkip in ips_to_check:
    print('Check ' + checkip)
    ip = client.ip(checkip)
    risk = ip.risk()
    print('IPs risk: ' + str(risk))
    if risk == 100:
        ips_found.append(f"IP's risk: {str(risk)} Checking IP: {checkip} Is proxy: {ip.proxy()}")
        break
    else:
        ips_found.append(str(risk))

    #if ip.risk():
    #    print('Find ' + checkip)
    #    ips_found.append(checkip)

    risk_score = ip.risk()
    latitude, longitude = ip.geological()

    data = ip.get()

    # A client should always be closed after being used!
print(ips_found)
client.close()



#with geoip2.database.Reader('./proxycheck/GeoIP2-City.mmdb') as reader:
#    for checkip in ips_to_check:
#        response = reader.anonymous_ip(checkip)
#        ips_found.append(f'is_anonymous:{response.is_anonymous}'
#                         f'is_anonymous_vpn:{response.is_anonymous_vpn}'
#                         f'is_hosting_provider:{response.is_hosting_provider}'
#                         f'is_public_proxy:{response.is_public_proxy}'
#                         f'is_residential_proxy:{response.is_residential_proxy}'
#                         f'is_tor_exit_node:{response.is_tor_exit_node}'
#                         f'ip_address:{response.ip_address}')
#print(ips_found)
