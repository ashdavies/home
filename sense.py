import time

from envirophat import light, motion, weather, leds
from google.cloud import firestore

client = firestore.Client()
collection = client.collection(u'readings')
document = collection.document(time.time())


def rgb():
    leds.on()
    result = light.rgb()
    leds.off()
    return result


document.set({
    u'light': light.light(),
    u'colour': rgb(),
    u'accelerometer': motion.accelerometer(),
    u'heading': motion.heading(),
    u'magnetometer': motion.magnetometer(),
    u'temperature': weather.temperature(),
    u'pressure': weather.pressure()
})
