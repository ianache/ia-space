from config import Config 
import requests
from requests.exceptions import HTTPError

class DeviceService:
    def __init__(self, config: Config):
        self.config = config

    def get_device(self, id: str):
        """
        Get device information by id (imei or OBC)
        :param id: Device ID (IMEI or OBC)
        :return: Device information
        """
        return {
            "imei": id,
            "obc": id,
            "linenumber": "1234567890",
            "operator": "CLARO",
            "status": "active",
        }
    
    def add_device(self, imei: str, obc: str, linenumber: str, operator: str):
        """
        Add a new device (GPS, Dashcam, etc.)
        :param imei: IMEI number of the device
        :param obc: OBC number of the device
        :param linenumber: Line number of the device
        :param operator: Operator of the device
        :return: Response from the device repository
        """
        return {
            "imei": imei,
            "obc": obc,
            "linenumber": linenumber,
            "operator": operator,
            "status": "active",
        }

    def update_device(self, obc: str, imei: str, linenumber: str, operator: str, status: str):
        """
        Update device information
        :param obc: OBC number of the device
        :param imei: IMEI number of the device
        :param linenumber: Line number of the device
        :param operator: Operator of the device
        :param status: Status of the device
        :return: Response from the device repository
        """   
        return {
            "imei": imei,
            "obc": obc,
            "linenumber": linenumber,
            "operator": operator,
            "status": status,
        }
