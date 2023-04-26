from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base


Base = declarative_base()

class BaseModel(Base):
    """
    Абстартный базовый класс, где описаны все поля и методы по умолчанию
    """
    __abstract__ = True

    id = Column(Integer, primary_key=True, index=True)

    def __repr__(self):
        return f"<{type(self).__name__}(id={self.id})>"

class AircraftCommander(BaseModel):
    __tablename__ = "aircraftCommanders"

    aircraft_num = Column(Integer)
    name = Column(String)
    address = Column(String)
    number = Column(Integer)
    experience = Column(Integer)

    airplane_id = Column(Integer, ForeignKey("airplanes.id"))

class Passenger(BaseModel):
    __tablename__ = "passengers"

    passport = Column(Integer)
    name = Column(String)
    address = Column(String)
    number = Column(Integer)

    flight = relationship("flihgt", back_populates="passengers")


class Flight(BaseModel):
    __tablename__ = "flights"

    flight_num = Column(Integer)
    date_time = Column(DateTime)
    is_canceled = Column(Boolean, default=False)

    airplane_id = Column(Integer, ForeignKey("airplanes.id"))
    rout_id = Column(Integer, ForeignKey("routs.id"))
    passenger = relationship("passenger", back_populates="flights")

class Airplane(BaseModel):
    __tablename__ = "airplanes"

    airplane_num = Column(Integer)
    name = Column(String)
    address = Column(String)
    number = Column(Integer)

    flight = relationship("flihgt", back_populates="Airplanes")
    commander_id = Column(Integer, ForeignKey("aircraftCommanders.id"))


class Route(BaseModel):
    __tablename__ = "routs"

    route_num = Column(Integer)
    airport_from = Column(String)
    airport_to = Column(String)
    price = Column(Integer)
    duration = Column(Integer)

    flight = relationship("flihgt", back_populates="routs")
