import grpc
from concurrent import futures
from services.get_properties import YeeligthBulbPropertiesService
from services import bulb_service_pb2_grpc


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    bulb_service_pb2_grpc.add_BulbServiceServicer_to_server(YeeligthBulbPropertiesService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
