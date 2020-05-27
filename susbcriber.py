import sys
import RPi.GPIO as a
import ssl
import time
# Import standard python modules.
# Import Adafruit IO MQTT client
from Adafruit_IO import MQTTClient
a.setmode(a.BOARD);
a.setwarnings(False);
a.setup(8,a.OUT);
a.setup(10,a.OUT);
a.setup(12,a.OUT);
# Set to your Adafruit IO key.
# Remember, your key is a secret,
# so make sure not to publish it when you publish this code!
ADAFRUIT_IO_KEY = 'f7e59e61d15940a6823170821eb45bb2'
# Set to your Adafruit IO username.
# (go to https://accounts.adafruit.com to find your username)
ADAFRUIT_IO_USERNAME = 'Pawan_Raj'
# Set to the ID of the feed to subscribe to for updates.
FEED_ID = 'potValue'
# Define callback functions which will be called when certain events happen.
def connected(client):
    # Connected function will be called when the client is connected to Adafruit IO.
    # This is a good place to subscribe to feed changes.  The client parameter
    # passed to this function is the Adafruit IO MQTT client so you can make
    # calls against it easily.
    #print('Connected to Adafruit IO!  Listening for {0} changes...'.format(FEED_ID))
    # Subscribe to changes on a feed named DemoFeed.
    client.subscribe(FEED_ID)
def disconnected(client):
    # Disconnected function will be called when the client disconnects.
    print('Disconnected from Adafruit IO!')
    sys.exit(1)
def message(client, feed_id,payload):
    #print('Feed {0} received new value: {1}'.format(feed_id, payload))
    print(payload)
    if payload=="FULL":
        a.output(8,a.HIGH)
        a.output(10,a.LOW)
        a.output(12,a.LOW)
    elif payload=="HALF FILLED":
        a.output(10,a.HIGH)
        a.output(12,a.LOW)
        a.output(8,a.LOW)
    elif payload=="EMPTY":
        a.output(12,a.HIGH)
        a.output(10,a.LOW)
        a.output(8,a.LOW)
# Create an MQTT client instance.
client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
# Setup the callback functions defined above.
client.on_connect    = connected
client.on_disconnect = disconnected
client.on_message    = message
# Connect to the Adafruit IO server.
client.connect()
client.loop_blocking()
