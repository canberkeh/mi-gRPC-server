import grpc
from src.services import bulb_service_pb2
from src.services import bulb_service_pb2_grpc

def get_bulb_properties():
    with grpc.insecure_channel('localhost:50051') as channel:  # Replace with the server's address
        stub = bulb_service_pb2_grpc.BulbServiceStub(channel)
        response = stub.GetProperties(bulb_service_pb2.Empty())
        return response.power, response.brightness

if __name__ == '__main__':
    power, brightness = get_bulb_properties()
    print(f"Power: {power}, Brightness: {brightness}")
