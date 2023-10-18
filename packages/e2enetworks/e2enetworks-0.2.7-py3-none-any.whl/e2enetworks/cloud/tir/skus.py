import requests
from e2enetworks.constants import BASE_GPU_URL
from e2enetworks.cloud.tir import client
from .utils import prepare_object


class Skus:
    def __init__(self):
        client_not_ready = (
            "Client is not ready. Please initiate client by:"
            "\n- Using e2enetworks.cloud.tir.init(...)"
        )
        if not client.Default.ready():
            raise ValueError(client_not_ready)

    def list(self, image_id, service):

        if type(image_id) != int:
            print(f"Image ID - {image_id} Should be Integer")
            return

        if type(service) != str:
            print(f"Service - {service} Should be String")
            return

        url = f"{BASE_GPU_URL}gpu_service/sku/?image_id={image_id}&service={service}&"
        req = requests.Request('GET', url)
        response = client.Default.make_request(req)
        if response.status_code == 200:
            skus = response.json()["data"]
            print("\nCPU PLANS\n")
            for sku in skus["CPU"]:
                print(sku)
            print("\nGPU PLANS\n")
            for sku in skus["GPU"]:
                print(sku)

    @staticmethod
    def help():
        print("Sku Class Help")
        print("\t\t================")
        print("\t\tThis class provides functionalities to interact with Skus.")
        print("\t\tAvailable methods:")

        print("\t\t1. list(image_id, service): Lists all Skus for given image_id and service.")
        print("\t\t Allowed Services List - ['notebook', 'inference']")
        # Example usages
        print("\t\tExample usages:")
        print("\t\tskus = Skus()")
        print("\t\tskus.list(image_id, service)")
