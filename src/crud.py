from sqlalchemy.orm import Session

from src import models, schemas


def create_commander(db: Session, commander: schemas.AircraftCommanderCreate):

    db_commander = models.AircraftCommander(aircraft_num=commander.aircraft_num, name=commander.name, address = commander.adress, number = commander.number, experience = commander.experience)
    db.add(db_commander)
    db.commit()
    db.refresh(db_commander)
    return db_commander

def create_passanger(db: Session, passanger: schemas.PassangerCreate):

    db_passanger = models.Passenger(passport=passanger.passport, name=passanger.name, address = passanger.adress, number = passanger.number)
    db.add(db_passanger)
    db.commit()
    db.refresh(db_passanger)
    return db_passanger

def create_flight(db: Session, flight: schemas.FlightCreate):

    db_flight = models.Flight(flight_num=flight.flight_num, date_time=flight.date_time, is_canceled = flight.is_canceled)
    db.add(db_flight)
    db.commit()
    db.refresh(db_flight)
    return db_flight

def create_airplane(db: Session, airplane: schemas.AirplaneCreate):

    db_airplane = models.Airplane(airplane_num=airplane.airplane_num, name=airplane.name, address = airplane.adress, number = airplane.number)
    db.add(db_airplane)
    db.commit()
    db.refresh(db_airplane)
    return db_airplane

def create_route(db: Session, route: schemas.RouteCreate):

    db_route = models.Route(route_num=route.route_num, airport_from=route.airport_from, airport_to=route.airport_to, price = route.price, duration = route.duration)
    db.add(db_route)
    db.commit()
    db.refresh(db_route)
    return db_route

"""
def create_route_flight(db: Session, flight: schemas.FlightCreate):

    db_route = models.Route(route_num=route.route_num, airport_from=route.airport_from, airport_to=route.airport_to, price = route.price, duration = route.duration)
    db.add(db_route)
    db.commit()
    db.refresh(db_route)
    return db_route  
"""










def create_user(db: Session, user: schemas.UserCreate):
    """
    Добавление нового пользователя
    """
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    """
    Добавление нового Item пользователю
    """
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def get_user(db: Session, user_id: int):
    """
    Получить пользователя по его id
    """
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    """
    Получить пользователя по его email
    """
    return db.query(models.User).filter(models.User.email == email).first()


def get_items(db: Session, skip: int = 0, limit: int = 100):
    """
    Получить список предметов из БД
    skip - сколько записей пропустить
    limit - маскимальное количество записей
    """
    return db.query(models.Item).offset(skip).limit(limit).all()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    """
    Получить список пользователей из БД
    skip - сколько записей пропустить
    limit - маскимальное количество записей
    """
    return db.query(models.User).offset(skip).limit(limit).all()