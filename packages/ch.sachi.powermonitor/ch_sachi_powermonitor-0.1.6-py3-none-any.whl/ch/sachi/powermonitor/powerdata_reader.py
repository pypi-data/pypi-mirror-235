import asyncio
import logging
from asyncio import Event

from victron_ble.devices import BatteryMonitorData, DeviceData

from ch.sachi.victron_ble.powermonitor_scanner import PowermonitorScanner

logger = logging.getLogger(__name__)

class PowerdataReader:
    result: BatteryMonitorData = None
    result_written: Event = Event()

    def __init__(self, id: str, key: str):
        self.id = id
        self.key = key

    async def read(self) -> BatteryMonitorData:
        keys = {self.id: self.key}
        scanner = self.create_scanner(keys)
        logger.debug('Scanner created')
        await scanner.start()
        logger.debug('Scanner started')
        # await scanner.stop()
        loop = asyncio.get_event_loop()
        task = loop.create_task(self.setResultAfter(3))
        await self.result_written.wait()
        return self.result

    async def setResultAfter(self, sleep):
        logger.debug('Sleep for %ssec', sleep)
        await asyncio.sleep(sleep)
        logger.debug('Now send some mock data')
        data = {
            'voltage': 12.7,
            'current': 1.23,
            'soc': 97.31,
            'consumed_ah': 7.3,
            'starter_voltage': 12.4
        }
        self.cb(BatteryMonitorData(1234, data))

    def create_scanner(self, keys):
        return PowermonitorScanner(self.cb, keys)

    def cb(self, device_data: DeviceData):
        if isinstance(device_data, BatteryMonitorData):
            self.result = device_data
            self.result_written.set()
