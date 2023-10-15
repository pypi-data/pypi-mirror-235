import uuid
import datetime
from dataclasses import dataclass, field
from typing import List

from cc_py_commons.loads.location import Location
from cc_py_commons.loads.equipment import Equipment
from cc_py_commons.loads.freighthub_contact import FreightHubContact

@dataclass
class Load:
    """
    Representation of a freight-hub load.
    In freight-hub customer_id = C4 Account ID
    source_id comes from the freight-hub sources
    """
    reference_number: str
    # C4 Account ID
    customer_id: int
    origin: Location
    destination: Location
    pickup_date: datetime.date
    delivery_date: datetime.date
    status_id: uuid.UUID
    source_id: uuid.UUID
    equipment: List[Equipment]
    equipment_description: str     
    contact: FreightHubContact
    pickup_open_time: datetime.time = field(default=None)
    pickup_close_time: datetime.time = field(default=None)
    pickup_appointment_required: bool = field(default=False)
    delivery_open_time: datetime.time = field(default=None)
    delivery_close_time: datetime.time = field(default=None)
    delivery_appointment_required: bool = field(default=False)
    tracking_number: str = field(default=None)
    full_load: bool = field(default=True)
    length: int = field(default=None)
    width: int = field(default=None)
    height: int = field(default=None)
    weight: int = field(default=None)
    load_count: int = field(default=None)
    distance: int = field(default=None)
    stops_count: int = field(default=None)
    stops: list = field(default=None)
    rate: str = field(default=None)
    declared_value: int = field(default=None)
    comment: str = field(default=None)
    commodity: str = field(default=None)
    min_temperature: float = field(default=None)
    max_temperature: float = field(default=None)
    tarp_size: int = field(default=None)
    carrier_id: uuid.UUID = field(default=None)
    contact_id: uuid.UUID = field(default=None)
    url: str = field(default=None)
    demo_load: bool = field(default=False)
    team_service_required: bool = field(default=False)
    quote_id: uuid.UUID = field(default=None)
    truck_lane_search_id: uuid.UUID = field(default=None)
    truck_search_id: uuid.UUID = field(default=None)
    # generated by server and returned
    id: uuid.UUID = field(default=None)
    # generated by server and returned
    load_number: str = field(default=None)
    mcleod_movement_id: str = field(default=None)
    origin_pallets_required: bool = field(default=False)
    destination_pallets_required: bool = field(default=False)
    hazmat: bool = field(default=False)
    origin_location_id: str = field(default=None)
    origin_location_name: str = field(default=None)
    destination_location_id: str = field(default=None)
    destination_location_name: str = field(default=None)
    special_instructions: dict = field(default=None)
    customer_equipment_id: str = field(default=None)
    partial_load: bool = field(default=False)
    pieces: int = field(default=None)
    available_time: datetime.datetime = field(default=None)
    account_id: int = field(default=None)
    max_pay: int = field(default=None)
    linear_feet: int = field(default=None)
    revenue_code: str = field(default=None)
    customer_code: str = field(default=None)
    ltl: bool = field(default=False)
    request_id: uuid.UUID = field(default=None)
