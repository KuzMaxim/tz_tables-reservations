from repositories.reservations import ReservationRepository
class ReservationService:
    def __init__(self):
        self.repository = ReservationRepository()
    