from netmiko import ConnectHandler

print ("Before connecting")




device1 = ConnectHandler(device_type='cisco_ios', host='ios-xe-mgmt-latest.cisco.com', username='developer', password='C1sco12345', port=8181)
output = device1.send_command("show running-config | be line vty")
print (output)
device1.disconnect()


#configcmds=["line vty 0 4", "exec-timeout 0 0"] 
#print (configcmds)
#device.send_config_set(configcmds)

print ("Clsoing")

