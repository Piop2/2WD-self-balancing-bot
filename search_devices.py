import asyncio
from bleak import BleakScanner
from bleak.backends.device import BLEDevice
from bleak.backends.scanner import AdvertisementData

def detection_handler(device: BLEDevice, advertisement_data: AdvertisementData):
    print(f"addr={device.address} uuid={advertisement_data.service_uuids}")

async def main():
    scanner = BleakScanner(detection_callback=detection_handler)
    await scanner.start()
    await asyncio.sleep(0.5)
    await scanner.stop()

asyncio.run(main())