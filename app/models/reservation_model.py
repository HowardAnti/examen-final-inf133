from app.database import db



class Reservation(db.Model):
    __tablename__ = "restaurants"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, unique=True, nullable=False)
    restaurant_id = db.Column(db.Integer, unique=True, nullable=False)
    reservation_date = db.Column(db.Date, nullable=False)
    num_guests =db.Column(db.Integer, nullable=False)
    special_requests= db.Column(db.String(100), nullable=False)
    status=db.Column(db.Column(db.String(100)), nullable=False)
       
    
def __init__(self, user_id, restaurant_id, reservation_date, num_guests, special_requests, status):
        self.user_id=user_id
        self.restaurant_id=restaurant_id
        self.reservation_date= reservation_date
        self.num_guests=num_guests
        self.special_requests=special_requests
        self.status=status

def save(self):
        db.session.add(self)
        db.session.commit()

@staticmethod
def get_all():
    return Reservation.query.all()

@staticmethod
def get_by_id(id):
    return Reservation.query.get(id)


def update(self, user_id=None, restaurant_id=None, reservation_date=None, nusm_guest=None, special_requests=None, status=None):
    if user_id is not None:
        self.user_id=user_id
    if restaurant_id is not None:
        self.restaurant_id=restaurant_id
    if reservation_date is not None:
        self.reservation_date=reservation_date
    if nusm_guest is not None:
        self.nusm_guest=nusm_guest
    if special_requests is not None:
        self.special_requests=special_requests
    if status is not None:
        self.status=status
            
    db.session.commit()

def delete(self):
    db.session.delete(self)
    db.session.commit()

    


    

    

    