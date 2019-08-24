from netmiko import ConnectHandler

file = open('inv.txt', 'r') 
for line in file: 
    print ("Processing for the device: ", line)
    print ("Before connecting")
    device1 = ConnectHandler(device_type='cisco_ios', host=line.rstrip('\r\n'), username='developer', password='C1sco12345', port=8181, timeout=30 )
    output = device1.send_command("show running-config | include exec-timeout")
    print (output)


    print ("Configruing now")
    configcmds=["line vty 0 4", "exec-timeout 30 0"] 
    print (configcmds)
    device1.send_config_set(configcmds)


    print ("After configuring")
    output = device1.send_command("show running-config | include exec-timeout")
    print (output)

    print ("Closing Connection")

    device1.disconnect()




print ("End of Inventory")
