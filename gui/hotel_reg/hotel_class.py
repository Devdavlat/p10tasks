class HotelGuest:
    def __init__(self, fullname, dob, where, date_of_stay, doj):
        self.fullname = fullname
        self.dob = dob
        self.where = where
        self.date_of_stay = date_of_stay
        self.doj = doj

    def get_attrs(self, as_dict=False):
        if as_dict:
            return {
                "Fullname": self.fullname,
                "DOB": self.dob,
                "Where": self.where,
                'Date of stay': self.date_of_stay,
                "DOJ": self.doj
            }
        return [
            self.fullname,
            self.dob,
            self.where,
            self.date_of_stay,
            self.doj
        ]
