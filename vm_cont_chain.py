
import paho.mqtt.client as mqtt
import time
from datetime import datetime
import socket


def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))
    client.subscribe("mianjunz/ping")
    client.message_callback_add("mianjunz/ping", on_message)
    

def on_message(client, userdata, msg):
    print("Default callback - topic: " + msg.topic + "   msg: " + str(msg.payload, "utf-8"))
    message = int(msg.payload.decode())
    message += 1
    client.publish("mianjunz/pong",message)
    print(f"{message} published")
    time.sleep(1)

if __name__ == '__main__':
    
    client = mqtt.Client()
    client.on_connect = on_connect
    time.sleep(2)
    client.connect(host="10.0.2.15", port=1883, keepalive=60)
    client.loop_forever()
    
    
       
        
