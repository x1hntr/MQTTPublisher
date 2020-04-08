import paho.mqtt.client as mqtt  
import time                               #import paho mqtt
import ssl
import random
 
cliente = "varClima"

def conexion_exitosa(client, userdata, flags, rc):
    #client.subscribe("ZHHDbfhBRGMGt7e") 
    client.publish("ambiente/temp") 
    
cliente = mqtt.Client()
cliente.on_connect = conexion_exitosa 
cliente.username_pw_set("x1hntr", "712189")                    #Pasww y user 
cliente.connect("broker.mqttdashboard.com", 1883, 60)          #Public broker of hiveMQ

while True:
    temp = random.randrange(18, 22)
    aire = random.randrange(92, 100)   
    hume = random.randrange(60, 70)
    cliente.publish("ambiente/temp", temp)
    cliente.publish("ambiente/aire", aire)
    cliente.publish("ambiente/hume", hume)
    time.sleep(1)
cliente.loop()                                       