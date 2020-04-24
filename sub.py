import paho.mqtt.client as mqtt
import time
import ssl
import sys
import random

host          = "ioticos.org"
port          = 1883
clean_session = True
client_id     = "CLIMA"
user_name     = "wKhj0dyPEhaXgT5"
password      = "VVkfFKYZAzEV7t0"    
topic         = "3Rgxx48mXbo1xia"

def on_connect (client, userdata, flags, rc):
  """ Callback called when connection/reconnection is detected """
  print ("Conected" % (host))
  client.subscribe(topic + '/temperature', qos=1)
  client.subscribe(topic + '/air', qos=1)
  client.subscribe(topic + '/humidity', qos=1)

 

def on_message(client, userdata, msg):
 
  print("message received " ,str(msg.payload.decode("utf-8")))


client = mqtt.Client (client_id = client_id, clean_session = clean_session)
client.username_pw_set (user_name, password)
client.on_connect = on_connect  
client.on_message = on_message


client.connect (host, port, keepalive = 60)


while True:
  client.loop ()