from grpc import StatusCode, ServicerContext
from config import YeelightBulb
from domain.yeelight_bulb import YeelightBulbDTO
from services import bulb_service_pb2
from services import bulb_service_pb2_grpc


class YeeligthBulbPropertiesService(bulb_service_pb2_grpc.BulbServiceServicer):
    def GetProperties(self, request, context: ServicerContext) -> bulb_service_pb2.BulbProperties:
        try:
            bulb_device = YeelightBulb.get_bulb()
            real_time_properties = bulb_device.get_properties(["power", "bright"])
            YeeligthBulbObject = YeelightBulbDTO(real_time_properties[0], real_time_properties[1])
            return bulb_service_pb2.BulbProperties(power=YeeligthBulbObject.power, brightness=YeeligthBulbObject.bright)
        except Exception as e:
            context.set_code(StatusCode.INTERNAL)
            context.set_details(str(e))
            return bulb_service_pb2.BulbProperties()
