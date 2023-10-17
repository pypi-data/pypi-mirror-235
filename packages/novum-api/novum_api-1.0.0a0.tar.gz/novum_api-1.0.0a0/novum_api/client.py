# pylint: disable=C0115
# pylint: disable=C0116
# pylint: disable=C0301
# flake8: noqa

import json
import requests
from novum_api.base_client import BaseAPIClient
from novum_api.api_type import TBattery, TBatteryType

PRODUCTION_API_HOST: str = "https://novum-batteries.com"


class NovumAPIClient(BaseAPIClient):
    def __init__(self, user=None, host=PRODUCTION_API_HOST):
        super().__init__(user, host)

    # ********************************************************
    # Section for the Service Center info
    # ********************************************************

    def ping(self) -> dict:
        return self._get_json("/api/batman/v1/")

    def get_info(self) -> dict:
        return self._get_json("/api/batman/v1/info")

    def get_version(self) -> dict:
        return self._get_json("/api/batman/v1/version")

    # ********************************************************
    # Section for the users
    # ********************************************************

    def login(
        self, email: str, password: str, store_user=True, timeout: float = 4
    ) -> dict:
        header = {"authorization": "auth", "content-type": "application/json"}
        payload = {"username": email, "password": password}
        response = requests.post(
            self.host + "/api/batman/v1/login",
            data=json.dumps(payload),
            headers=header,
            timeout=timeout,
        )

        if store_user is True:
            self.user = response.json()
            self._install_token_refresh_procedure(self.user)
            self.headers = dict(
                {
                    "Content-Type": "application/json",
                    "Authorization": "Bearer " + str(self.user.get("jwt")),
                }
            )
        return self.user

    def logout(self) -> str:
        return self._get_json("/api/batman/v1/logout")

    def check_current_user_still_authenticated(self) -> dict:
        return self._get_json("/api/batman/v1/check_token")

    # ********************************************************
    # Section for the Battery Types
    # ********************************************************

    def get_battery_types(
        self,
        filter_types: dict = None,
        option: dict = None,
        fields: dict = None,
        timeout: float = 4.0,
    ) -> dict:
        return self._get_json(
            "/api/batman/v1/batteryTypes",
            filter_json=filter_types,
            option=option,
            fields=fields,
            timeout=timeout,
        )

    def get_battery_types_count(
        self,
        filter_types: dict = None,
        option: dict = None,
        fields: dict = None,
        timeout: float = 4.0,
    ) -> dict:
        return self._get_json(
            "/api/batman/v1/batteryTypes/count",
            filter_json=filter_types,
            option=option,
            fields=fields,
            timeout=timeout,
        )

    def get_battery_types_by_id(
        self, battery_type_id: str, timeout: float = 4.0
    ) -> dict:
        return self._get_json(
            f"/api/batman/v1/batteryTypes/{battery_type_id}", timeout=timeout
        )

    def remove_battery_types_by_id(self, battery_type_id: str, timeout: float = 4.0):
        self._delete_json(
            f"/api/batman/v1/batteryTypes/{battery_type_id}", timeout=timeout
        )
        return print("The battery type was removed.")

    def create_battery_type(
        self,
        battery_type: TBatteryType,
        timeout: float = 4.0,
    ) -> dict:
        response = self._post_json(
            "/api/batman/v1/batteryTypes", data=battery_type, timeout=timeout
        )
        return response

    def update_battery_type_by_id(
        self,
        battery_type_id: str,
        battery_type_update: TBatteryType,
        timeout: float = 4.0,
    ) -> dict:
        return self._put_json(
            f"/api/batman/v1/batteryTypes/{battery_type_id}",
            data=battery_type_update,
            timeout=timeout,
        )

    # ********************************************************
    # Section for the Datasets
    # ********************************************************

    def dataset_exists_on_remote(self, dataset_id: str, timeout: float = 4.0) -> bool:
        response = self._get_json(
            f"/api/batman/v1/datasets/{dataset_id}", timeout=timeout
        )
        try:
            if len(response["measured"]["measurement_cycles"]) != 0:
                return True
        except KeyError:
            return False

    def create_dataset(self, dataset: dict, timeout: float = 4.0) -> dict:
        return self._post_json(
            "/api/batman/v1/datasets/", data=dataset, timeout=timeout
        )

    def get_dataset_by_id(self, dataset_id: str, timeout: float = 4.0) -> dict:
        return self._get_json(f"/api/batman/v1/datasets/{dataset_id}", timeout=timeout)

    def get_datasets(
        self,
        filter_datasets: dict = None,
        option: dict = None,
        fields: dict = None,
        timeout: float = 4.0,
    ) -> dict:
        return self._get_json(
            "/api/batman/v1/datasets",
            filter_json=filter_datasets,
            option=option,
            fields=fields,
            timeout=timeout,
        )

    def get_datasets_count(
        self,
        filter_datasets: dict = None,
        option: dict = None,
        fields: dict = None,
        timeout: float = 4.0,
    ) -> dict:
        return self._get_json(
            "/api/batman/v1/datasets/count",
            filter_json=filter_datasets,
            option=option,
            fields=fields,
            timeout=timeout,
        )

    def get_datasets_count_by_battery(
        self,
        battery: TBattery,
        filter_datasets: dict = None,
        option: dict = None,
        fields: dict = None,
        timeout: float = 4.0,
    ) -> dict:
        filter_with_id = {"meta.battery._id": battery["id"]}
        if filter_datasets is not None:
            filter_with_id.update(filter_datasets)
        response = self._get_json(
            "/api/batman/v1/datasets/count",
            filter_json=filter_with_id,
            option=option,
            fields=fields,
            timeout=timeout,
        )
        return response

    def update_dataset_by_id(
        self, dataset_id: str, dataset: dict, timeout: float = 4.0
    ) -> dict:
        return self._post_json(
            f"/api/batman/v1/datasets/{dataset_id}", data=dataset, timeout=timeout
        )

    def remove_dataset_by_id(self, dataset_id: str, timeout: float = 4.0):
        self._delete_json(f"/api/batman/v1/datasets/{dataset_id}", timeout=timeout)
        return print("The data set was removed.")

    # ********************************************************
    # Section for the Battery
    # ********************************************************

    def create_battery(self, battery: TBattery, timeout: float = 4.0) -> dict:
        return self._post_json(
            "/api/batman/v1/batteries", data=battery, timeout=timeout
        )

    def get_battery_by_id(self, battery_id: str, timeout: float = 4.0) -> dict:
        return self._get_json(f"/api/batman/v1/batteries/{battery_id}", timeout=timeout)

    def update_battery(self, battery: TBattery, timeout: float = 4.0) -> dict:
        return self._put_json(
            f"/api/batman/v1/batteries/{battery['id']}", data=battery, timeout=timeout
        )

    def update_battery_by_id(
        self, battery_id: str, battery_update: dict, timeout: float = 4.0
    ) -> dict:
        return self._put_json(
            f"/api/batman/v1/batteries/{battery_id}",
            data=battery_update,
            timeout=timeout,
        )

    def remove_battery_by_id(self, battery_id: str, timeout: float = 4.0) -> str:
        self._delete_json(f"/api/batman/v1/batteries/{battery_id}", timeout=timeout)
        return print("The battery was removed.")

    def get_batteries(
        self,
        filter_batteries: dict = None,
        option: dict = None,
        timeout: float = 4.0,
    ) -> dict:
        return self._get_json(
            "/api/batman/v1/batteries",
            filter_json=filter_batteries,
            option=option,
            timeout=timeout,
        )

    def get_batteries_count(
        self,
        filter_batteries: dict = None,
        option: dict = None,
        fields: dict = None,
        timeout: float = 4.0,
    ) -> dict:
        return self._get_json(
            "/api/batman/v1/batteries/count",
            filter_json=filter_batteries,
            option=option,
            fields=fields,
            timeout=timeout,
        )

    def get_children_of_battery_by_id(
        self,
        parent_battery_id: str,
        filter_batteries: dict = None,
        option: dict = None,
        fields: dict = None,
        timeout: float = 4.0,
    ) -> dict:
        filter_with_id = {"tree.parent": parent_battery_id}
        if filter_batteries is not None:
            filter_with_id.update(filter_batteries)
        print(filter_with_id)
        return self._get_json(
            "/api/batman/v1/batteries",
            filter_json=filter_with_id,
            option=option,
            fields=fields,
            timeout=timeout,
        )

    def get_children_of_battery_by_id_count(
        self,
        parent_battery_id: str,
        filter_batteries: dict = None,
        option: dict = None,
        fields: dict = None,
        timeout: float = 4.0,
    ) -> dict:
        filter_with_id = {"tree.parent": parent_battery_id}
        if filter_batteries is not None:
            filter_with_id.update(filter_batteries)
        response = self._get_json(
            "/api/batman/v1/batteries/count",
            filter_json=filter_with_id,
            option=option,
            fields=fields,
            timeout=timeout,
        )
        return response

    def get_leaves_of_battery_by_id(
        self,
        ancestor_battery_id: str,
        filter_batteries: dict = None,
        option: dict = None,
        fields: dict = None,
        timeout: float = 4.0,
    ) -> dict:
        filter_with_id = {"tree.is_leaf": True, "tree.ancestors": ancestor_battery_id}
        if filter_batteries is not None:
            filter_with_id.update(filter_batteries)
        response = self._get_json(
            "/api/batman/v1/batteries",
            filter_json=filter_with_id,
            option=option,
            fields=fields,
            timeout=timeout,
        )
        return response

    def get_leaves_of_battery_by_id_count(
        self,
        ancestor_battery_id: str,
        filter_batteries: dict = None,
        option: dict = None,
        fields: dict = None,
        timeout: float = 4.0,
    ) -> dict:
        filter_with_id = {"tree.is_leaf": True, "tree.ancestors": ancestor_battery_id}
        if filter_batteries is not None:
            filter_with_id.update(filter_batteries)
        response = self._get_json(
            "/api/batman/v1/batteries/count",
            filter_json=filter_with_id,
            option=option,
            fields=fields,
            timeout=timeout,
        )
        return response

    def get_descendants_of_battery_by_id(
        self,
        ancestor_battery_id: str,
        filter_batteries: dict = None,
        option: dict = None,
        fields: dict = None,
        timeout: float = 4.0,
    ) -> dict:
        filter_with_id = {"tree.ancestors": ancestor_battery_id}
        filter_with_id.get(filter_batteries)
        response = self._get_json(
            "/api/batman/v1/batteries",
            filter_json=filter_with_id,
            option=option,
            fields=fields,
            timeout=timeout,
        )
        return response

    def get_descendants_of_battery_by_id_count(
        self,
        ancestor_battery_id: str,
        filter_batteries: dict = None,
        option: dict = None,
        fields: dict = None,
        timeout: float = 4.0,
    ) -> dict:
        filter_with_id = {"tree.ancestors": ancestor_battery_id}
        if filter_batteries is not None:
            filter_with_id.get(filter_batteries)
        response = self._get_json(
            "/api/batman/v1/batteries/count",
            filter_json=filter_with_id,
            option=option,
            fields=fields,
            timeout=timeout,
        )
        return response

    # ********************************************************
    # Section for the CapacityMeasurement
    # ********************************************************

    def create_capacity_measurement(
        self, capacity_measurement: dict, timeout: float = 4.0
    ) -> dict:
        response = self._post_json(
            "/api/batman/v1/capacityMeasurements",
            data=capacity_measurement,
            timeout=timeout,
        )
        return response

    def update_capacity_measurement_by_id(
        self,
        capacity_measurement_id: str,
        capacity_measurement: dict,
        timeout: float = 4.0,
    ) -> dict:
        response = self._put_json(
            f"/api/batman/v1/capacityMeasurements/{capacity_measurement_id}",
            data=capacity_measurement,
            timeout=timeout,
        )
        return response

    def remove_capacity_measurement_by_id(
        self, capacity_measurement_id: str, timeout: float = 4.0
    ):
        self._delete_json(
            f"/api/batman/v1/capacityMeasurements/{capacity_measurement_id}",
            timeout=timeout,
        )
        return print("Capacity measurement was removed.")

    def get_capacity_measurement(
        self,
        filter_measurements: dict = None,
        option: dict = None,
        fields: dict = None,
        timeout: float = 4.0,
    ) -> dict:
        response = self._get_json(
            "/api/batman/v1/capacityMeasurements",
            filter_json=filter_measurements,
            option=option,
            fields=fields,
            timeout=timeout,
        )
        return response

    def get_capacity_measurement_count(
        self,
        filter_measurements: dict = None,
        option: dict = None,
        fields: dict = None,
        timeout: float = 4.0,
    ) -> dict:
        response = self._get_json(
            "/api/batman/v1/capacityMeasurements/count",
            filter_json=filter_measurements,
            option=option,
            fields=fields,
            timeout=timeout,
        )
        return response

    def get_capacity_measurement_by_id(
        self, capacity_measurement_id: str, timeout: float = 4.0
    ) -> dict:
        response = self._get_json(
            f"/api/batman/v1/capacityMeasurements/{capacity_measurement_id}",
            timeout=timeout,
        )
        return response

    def get_capacity_measurements_count_by_battery(
        self, battery_id: str, timeout: float = 4.0
    ) -> dict:
        filter_by_id = {"battery._id": battery_id}
        response = self._get_json(
            "/api/batman/v1/capacityMeasurements/count",
            filter_json=filter_by_id,
            timeout=timeout,
        )
        return response

    def capacity_measurement_exists_on_remote(
        self, capacity_measurement_id: dict, timeout: float = 4.0
    ) -> bool:
        response = self._get_json(
            f"/api/batman/v1/capacityMeasurements/{capacity_measurement_id}",
            timeout=timeout,
        )
        return response.id == capacity_measurement_id

    # ********************************************************
    # Section for the Measurements
    # ********************************************************

    def get_latest_measurements(
        self, device_id: str, count: int = 1, timeout: float = 4.0
    ) -> dict:
        return self._get_json(
            f"/api/time-series/v1/devices/{device_id}/measurements/last/{count}",
            timeout=timeout,
        )

    def write_device_measurements(
        self, device_measurements: dict, timeout: float = 4.0
    ) -> dict:
        return self._post_json(
            "/api/time-series/v1/measurements",
            data=device_measurements,
            timeout=timeout,
        )

    def read_device_measurements(
        self,
        device_filter: list,
        option=None,
        fields: dict = None,
        timeout: float = 4.0,
    ) -> dict:
        return self._get_json(
            "/api/time-series/v1/measurements",
            filter_json=device_filter,
            option=option,
            fields=fields,
            timeout=timeout,
        )

    def read_device_measurements_by_id(  # TODO
        self, battery_id, device_filter: list, fields: dict = None, timeout: float = 4.0
    ) -> dict:
        return self._get_json(
            f"/api/time-series/v1/measurements/{battery_id}",
            filter_json=device_filter,
            fields=fields,
            timeout=timeout,
        )

    # ********************************************************
    # Section for the reports
    # ********************************************************

    def create_report(self, report, headers=None, timeout: float = 4.0):
        return self._post_json(
            "/api/batman/v1/reports", report, headers, timeout=timeout
        )

    def update_report_by_id(
        self, report_id: str, report, headers=None, timeout: float = 4
    ):
        return self._put_json(
            f"/api/batman/v1/reports/{report_id}", report, headers, timeout=timeout
        )

    def get_reports(
        self, report_filter=None, option=None, fields: dict = None, timeout: float = 4
    ):
        return self._get_json(
            "/api/batman/v1/reports",
            filter_json=report_filter,
            fields=fields,
            option=option,
            timeout=timeout,
        )

    def get_reports_count(
        self, report_filter=None, option=None, fields: dict = None, timeout: float = 4
    ) -> int:
        return self._get_json(
            "/api/batman/v1/reports/count",
            report_filter,
            option=option,
            fields=fields,
            timeout=timeout,
        )

    def get_reports_count_by_battery(
        self, battery: TBattery, timeout: float = 4
    ) -> int:
        return self._get_json(
            "/api/batman/v1/reports/count",
            filter_json={"origin_id": battery["id"]},
            timeout=timeout,
        )

    def get_report_by_id(self, report_id: str, timeout: float = 4) -> dict:
        return self._get_json(f"/api/batman/v1/reports/{report_id}", timeout=timeout)

    def get_reports_by_origin_id(
        self,
        origin_id: str,
        report_filter: dict = None,
        option=None,
        fields: dict = None,
        timeout: float = 4,
    ) -> dict:
        return self._get_json(
            f"/api/batman/v1/reports/byOriginId/{origin_id}",
            report_filter,
            option,
            fields=fields,
            timeout=timeout,
        )

    def get_reports_by_origin_id_count(
        self,
        origin_id: str,
        report_filter: dict = None,
        option=None,
        fields: dict = None,
        timeout: float = 4,
    ) -> dict:
        return self._get_json(
            f"/api/batman/v1/reports/byOriginId/{origin_id}/count",
            report_filter,
            option,
            fields=fields,
            timeout=timeout,
        )

    def remove_report_by_id(
        self, report_id: str, report_filter=None, option=None, timeout: float = 4
    ) -> dict:
        return self._delete_json(
            f"/api/batman/v1/reports/{report_id}",
            filter_json=report_filter,
            option=option,
            timeout=timeout,
        )

    # ********************************************************
    # Section for inferences
    # ******************************************************/

    def write_inference(self, data: dict):
        return self._post_json("/api/time-series/v1/inferences", data)

    def read_inference_by_id(
        self, inference_id: str, fields: dict = None, timeout: float = 4
    ):
        return self._get_json(
            f"/api/time-series/v1/inferences/{inference_id}",
            fields=fields,
            timeout=timeout,
        )

    def read_inferred_data_by_device_id(
        self,
        inference_filter: dict = None,
        option=None,
        fields: dict = None,
        timeout: float = 4,
    ):
        return self._get_json(
            "/api/time-series/v1/inferences",
            filter_json=inference_filter,
            option=option,
            fields=fields,
            timeout=timeout,
        )

    def update_inference(self, inference_id: str, data: dict, timeout: float = 4):
        return self._put_json(
            f"/api/time-series/v1/inferences/{inference_id}", data, timeout=timeout
        )

    def write_inference_by_id(self, inference_id: str, data: dict, timeout: float = 4):
        return self._post_json(
            f"/api/time-series/v1/inferences/{inference_id}", data, timeout=timeout
        )
