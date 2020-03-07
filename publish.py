import paho.mqtt.client as mqtt
import ssl

mqttclient = mqtt.Client("pyClient")
      
mqttclient.tls_set(tls_version=ssl.PROTOCOL_TLSv1_2)
mqttclient.username_pw_set("Username", "Passw0rd")
mqttclient.connect("mqtt.example.com", 8883)
mqttclient.publish("hello/world", "hi", qos=0, retain=False)

mqttclient.disconnect()
