from pydantic import BaseModel
from datetime import date, datetime

class AircraftCommanderBase(BaseModel):
    aircraft_num: int
    name: str
    adress: str
    number: int
    experience: int


class AircraftCommanderCreate(AircraftCommanderBase):
    pass


class AircraftCommander(AircraftCommanderBase):
    id: int

    airplane_id: int

    class Config:
        orm_mode = True




class PassengerBase(BaseModel):
    passport: int
    name: str
    address: str
    number: int

class PassengerCreate(PassengerBase):
    pass

class Passanger(PassengerBase):
    id: int

    flihts: list[Flight] = []

    class Config:
        orm_mode = True




class FlightBase(BaseModel):
    flight_num: int
    date_time: date
    is_canceled: bool

class FlightCreate(FlightBase):
    pass

class Flight(FlightBase):
    id: int 

    airplane_id: int
    route_id: int
    passangers: list[Passanger] = []

    class Config:
        orm_mode = True




class AirplaneBase(BaseModel):
    airplane_num: int
    name: str
    address: str
    number: int

class AirplaneCreate(AirplaneBase):
    pass

class Airplane(AirplaneBase):
    id: int

    commander_id: int
    flights: list[Flight] = []

    class Config:
        orm_mode = True




class RouteBase(BaseModel):
    route_num: int
    airport_from: str
    airport_to: str
    price: int
    duration: int

class RouteCreate(RouteBase):
    pass

class Route(RouteBase):
    id: int

    flights: list[Flight] = []
 
    class Config:
        orm_mode = True
