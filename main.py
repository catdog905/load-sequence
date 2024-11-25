from locustfiles.make_orders_and_scan_containers import ScanContainers, MakeOrder
from locust import task, between, run_single_user

if __name__ == "__main__":
    run_single_user(ScanContainers)
