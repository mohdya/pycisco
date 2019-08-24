from netmiko import ConnectHandler

print ("Before connecting")
device1 = ConnectHandler(device_type='cisco_ios', host='ios-xe-mgmt-latest.cisco.com', username='developer', password='C1sco12345', port=8181)
output = device1.send_command("show running-config | be line vty")
print (output)


print ("Configruing now")
configcmds=["line vty 0 4", "exec-timeout 50 0"] 
print (configcmds)
device1.send_config_set(configcmds)


print ("After configuring")
output = device1.send_command("show running-config | be line vty")
print (output)

print ("Closing")

device1.disconnect()



