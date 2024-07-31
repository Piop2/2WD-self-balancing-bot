import asyncio

from bleak import BleakClient

ADDRESS = "B4:BC:7C:3F:7C:52"
UUID = "0000ffe1-0000-1000-8000-00805f9b34fb"

def disconnected_handler(client:BleakClient):
    print(f"{client.address} disconnected")

async def main(address: str):
    client = BleakClient(address_or_ble_device=address, disconnected_callback=disconnected_handler)

    try:
        await client.connect()
        print("connected")

        # for service in await client.get_services():
        #     print(service)
        #     print('\tuuid:', service.uuid)
        #     print('\tcharacteristic list:')
        #     for characteristic in service.characteristics:
        #         print('\t\t', characteristic)
        #         print('\t\tuuid:', characteristic.uuid)
        #         print('\t\tdescription :', characteristic.description)
        #         print('\t\tproperties :', characteristic.properties)

        characteristic = client.services.get_characteristic(UUID)
        await client.read_gatt_char(characteristic)
        await client.write_gatt_char(characteristic, bytes(b"hello"))

    except Exception as e:
        print(e)
    finally:
        await client.disconnect()

asyncio.run(main(address))