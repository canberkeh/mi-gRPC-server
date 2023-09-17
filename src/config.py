import os
from dotenv import load_dotenv

from miio import device

load_dotenv('device.env')

DEVICE_IP = os.getenv("DEVICE_IP")
DEVICE_TOKEN = os.getenv("DEVICE_TOKEN")


class YeelightBulb:
    _bulb = None

    @classmethod
    def get_bulb(cls) -> device.Device:
        if cls._bulb is None:
            cls._bulb = device.Device(DEVICE_IP, DEVICE_TOKEN)
        return cls._bulb
