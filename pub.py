import paho.mqtt.client as mqtt  
import time                               #import paho mqtt
import ssl
import random
 
#MQTT CREDENTIALS

host          = "ioticos.org"
port          = 1883
clean_session = True
cliente       = "varClima"
user_name     = "wKhj0dyPEhaXgT5"
password      = "VVkfFKYZAzEV7t0"    
topic         = "3Rgxx48mXbo1xia"

def conexion_exitosa(client, userdata, flags, rc):

    client.publish("ambiente/temp") 

cliente = mqtt.Client()
cliente.on_connect = conexion_exitosa 
cliente.username_pw_set(user_name, password)                    #Pasww y user 
cliente.connect(host, port, 60)          #Public broker of hiveMQ

while True:
    temperature = random.randrange(18, 22)
    air = random.randrange(92, 100)   
    humidity = random.randrange(60, 70)
    cliente.publish(topic + "/temperature", temperature)
    cliente.publish(topic + "/air", air)
    cliente.publish(topic + "/humidity", humidity)
    time.sleep(1)
cliente.loop()                                       