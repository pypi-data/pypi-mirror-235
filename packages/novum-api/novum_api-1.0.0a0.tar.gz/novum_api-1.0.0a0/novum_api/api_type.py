# pylint: disable=C0115
# pylint: disable=C0116
# pylint: disable=C0301
# flake8: noqa

import datetime
from typing import Dict, List, Optional, Union


class TMinMax:
    def __init__(self, min: float, max: float):
        self.min = min
        self.max = max


class TGeometricDimension:
    def __init__(self, height: float, width: float, depth: float):
        self.height = height
        self.width = width
        self.depth = depth


class TEISSetup:
    def __init__(
        self,
        start_frequency: Optional[float],
        end_frequency: Optional[float],
        number_of_frequencies: Optional[int],
        excitation_current_offset: Optional[float],
        excitation_current_amplitude: Optional[float],
        excitation_mode: Optional[int],
    ):
        self.start_frequency = start_frequency
        self.end_frequency = end_frequency
        self.number_of_frequencies = number_of_frequencies
        self.excitation_current_offset = excitation_current_offset
        self.excitation_current_amplitude = excitation_current_amplitude
        self.excitation_mode = excitation_mode


class TChargeSetup:
    def __init__(self, discharge_rate: float, charge_rate: float):
        self.discharge_rate = discharge_rate
        self.charge_rate = charge_rate


class TUserDocument:
    def __init__(
        self,
        original_file_name: str,
        file_name: str,
        file_url: str,
        file_md5: Optional[str],
        file_type: Optional[Dict[str, Union[str, int, float]]],
        file_size: int,
        aws_file_url: str,
        aws_file_name: str,
    ):
        self.original_file_name = original_file_name
        self.file_name = file_name
        self.file_url = file_url
        self.file_md5 = file_md5
        self.file_type = file_type
        self.file_size = file_size
        self.aws_file_url = aws_file_url
        self.aws_file_name = aws_file_name


class TBaseDocModel:
    def __init__(
        self,
        creator_id: str,
        updater_id: str,
        id: str,
        created_at: Union[datetime.datetime, str],
        updated_at: Union[datetime.datetime, str],
    ):
        self.creator_id = creator_id
        self.updater_id = updater_id
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at


class TDetails:
    def __init__(
        self,
        code: Optional[int] = None,
        error: Optional[str] = None,
        details: Optional[str] = None,
        headers: Optional[Dict[str, str]] = None,
    ):
        self.code = code
        self.error = error
        self.details = details
        self.headers = headers


class TAPIError:
    def __init__(self, error: Optional[str], details: Optional[TDetails]):
        self.error = error
        self.details = details


class TIDAndTimes(TAPIError):
    def __init__(
        self,
        id: str,
        created_at: Union[datetime.datetime, str],
        updated_at: Union[datetime.datetime, str],
        error: Optional[str] = None,
        details: Optional[TDetails] = None,
    ):
        super().__init__(error=error, details=details)
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at


# TBaseDocModel type
TBaseDocModel = Dict[str, Union[str, TIDAndTimes]]


class TLatLng:
    def __init__(self, planet: str, lat: float, lng: float):
        self.planet = planet
        self.lat = lat
        self.lng = lng


class TAddress:
    def __init__(
        self,
        country: str,
        country_code: str,
        city: str,
        state: str,
        postal_code: str,
        street: str,
        street_number: str,
    ):
        self.country = country
        self.country_code = country_code
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.street = street
        self.street_number = street_number


class TLocation:
    def __init__(self, geo: TLatLng, address: TAddress):
        self.geo = geo
        self.address = address


class TMetrics:
    def __init__(
        self,
        measured_at: datetime.datetime,
        state_of_health: float,
        state_of_charge: float,
        temperature: float,
    ):
        self.measured_at = measured_at
        self.state_of_health = state_of_health
        self.state_of_charge = state_of_charge
        self.temperature = temperature


class TIndicatorProperty:
    def __init__(self, scale: float, top: float, left: float):
        self.scale = scale
        self.top = top
        self.left = left


class TIndicatorProperties:
    def __init__(self, properties: Dict[str, TIndicatorProperty]):
        self.properties = properties


class TInsights:
    def __init__(
        self,
        enabled: bool,
        image: Optional[str] = None,
        image_styles: Optional[str] = None,
        indicator_properties: Optional[TIndicatorProperties] = None,
    ):
        self.enabled = enabled
        self.image = image
        self.image_styles = image_styles
        self.indicator_properties = indicator_properties


class TAtomicState:
    def __init__(
        self,
        updated_at: Union[datetime.datetime, str],
        value: float,
        origin_id: Optional[str] = None,
    ):
        self.updated_at = updated_at
        self.value = value
        self.origin_id = origin_id


class TBatteryState:
    def __init__(
        self,
        state_of_health: Optional[TAtomicState] = None,
        state_of_charge: Optional[TAtomicState] = None,
        current: Optional[TAtomicState] = None,
        voltage: Optional[TAtomicState] = None,
        temperature: Optional[TAtomicState] = None,
    ):
        self.state_of_health = state_of_health
        self.state_of_charge = state_of_charge
        self.current = current
        self.voltage = voltage
        self.temperature = temperature


class TTreeProperties:
    def __init__(
        self,
        is_leaf: Optional[bool] = None,
        enabled: Optional[bool] = None,
        parent: Optional[str] = None,
        ancestors: Optional[List[str]] = None,
        children_topology: Optional[str] = None,
    ):
        self.is_leaf = is_leaf
        self.enabled = enabled
        self.parent = parent
        self.ancestors = ancestors
        self.children_topology = children_topology


class TEstimatorOverview:
    def __init__(
        self,
        file_name: Optional[str] = None,
        description: Optional[str] = None,
        time: Optional[Union[str, datetime.datetime]] = None,
        last_valid_time: Optional[Union[str, datetime.datetime]] = None,
        model_state: Optional[List[float]] = None,
        last_valid_model_state: Optional[List[float]] = None,
        report: Optional[str] = None,
    ):
        self.file_name = file_name
        self.description = description
        self.time = time
        self.last_valid_time = last_valid_time
        self.model_state = model_state
        self.last_valid_model_state = last_valid_model_state
        self.report = report


class TEstimators:
    def __init__(self, soc_estimator: Optional[TEstimatorOverview] = None):
        self.soc_estimator = soc_estimator


class TBatteryType(TBaseDocModel):
    def __init__(
        self,
        name: str,
        manufacturer: str,
        nominal_voltage: float,
        nominal_capacity: float,
        description: Optional[str] = None,
        cell_chemistry: Optional[str] = None,
        battery_design: Optional[str] = None,
        allowed_voltage_range_single_cell: Optional[TMinMax] = None,
        allowed_voltage_range_battery_pack: Optional[TMinMax] = None,
        allowed_peak_charge_current_range: Optional[TMinMax] = None,
        allowed_continuous_charge_current_range: Optional[TMinMax] = None,
        allowed_temperature_range_for_charging: Optional[TMinMax] = None,
        allowed_temperature_range_for_storage: Optional[TMinMax] = None,
        allowed_temperature_range_for_use: Optional[TMinMax] = None,
        internal_resistance: Optional[float] = None,
        self_discharge_rate_per_month: Optional[float] = None,
        allowed_cycles_for_100_depth_of_discharge: Optional[int] = None,
        mass_based_power_density: Optional[float] = None,
        cell_mass: Optional[float] = None,
        outer_geometric_dimension: Optional[TGeometricDimension] = None,
        default_eis_setup: Optional[TEISSetup] = None,
        default_charge_setup: Optional[TChargeSetup] = None,
        image: Optional[str] = None,
        user_docs: Optional[List[TUserDocument]] = None,
        user_doc_ids: Optional[List[str]] = None,
        public: Optional[bool] = None,
        tags: Optional[List[str]] = None,
    ):
        super().__init__(creator_id="", updater_id="")
        self.name = name
        self.manufacturer = manufacturer
        self.nominal_voltage = nominal_voltage
        self.nominal_capacity = nominal_capacity
        self.description = description
        self.cell_chemistry = cell_chemistry
        self.battery_design = battery_design
        self.allowed_voltage_range_single_cell = allowed_voltage_range_single_cell
        self.allowed_voltage_range_battery_pack = allowed_voltage_range_battery_pack
        self.allowed_peak_charge_current_range = allowed_peak_charge_current_range
        self.allowed_continuous_charge_current_range = (
            allowed_continuous_charge_current_range
        )
        self.allowed_temperature_range_for_charging = (
            allowed_temperature_range_for_charging
        )
        self.allowed_temperature_range_for_storage = (
            allowed_temperature_range_for_storage
        )
        self.allowed_temperature_range_for_use = allowed_temperature_range_for_use
        self.internal_resistance = internal_resistance
        self.self_discharge_rate_per_month = self_discharge_rate_per_month
        self.allowed_cycles_for_100_depth_of_discharge = (
            allowed_cycles_for_100_depth_of_discharge
        )
        self.mass_based_power_density = mass_based_power_density
        self.cell_mass = cell_mass
        self.outer_geometric_dimension = outer_geometric_dimension
        self.default_eis_setup = default_eis_setup
        self.default_charge_setup = default_charge_setup
        self.image = image
        self.user_docs = user_docs
        self.user_doc_ids = user_doc_ids
        self.public = public
        self.tags = tags


class TBattery(TBaseDocModel):
    def __init__(
        self,
        name: str,
        battery_type: TBatteryType,
        serial_number: Optional[str] = None,
        description: Optional[str] = None,
        location: Optional[TLocation] = None,
        image: Optional[str] = None,
        tags: Optional[List[str]] = None,
        metrics: Optional[TMetrics] = None,
        insights: Optional[TInsights] = None,
        state: Optional[TBatteryState] = None,
        tree: Optional[TTreeProperties] = None,
        estimators: Optional[TEstimators] = None,
        user_doc_ids: Optional[List[str]] = None,
    ):
        super().__init__(creator_id="", updater_id="")
        self.name = name
        self.battery_type = battery_type
        self.serial_number = serial_number
        self.description = description
        self.location = location
        self.image = image
        self.tags = tags
        self.metrics = metrics
        self.insights = insights
        self.state = state
        self.tree = tree
        self.estimators = estimators
        self.user_doc_ids = user_doc_ids
