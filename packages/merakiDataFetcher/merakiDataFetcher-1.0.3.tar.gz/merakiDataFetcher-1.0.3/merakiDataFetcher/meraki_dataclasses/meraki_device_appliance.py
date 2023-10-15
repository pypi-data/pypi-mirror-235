from dataclasses import dataclass
from merakiDataFetcher.meraki_dataclasses.meraki_device import MerakiDevice

@dataclass
class MerakiAppliance(MerakiDevice):
    wan1Ip: str
    wan2Ip: str
