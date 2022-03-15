print("Info function")

class User():
    def __init__(self, name, surname, year, city, email, mobile):
        self.name = name
        self.surname = surname
        self.year = year
        self.city = city
        self.email = email
        self.mobile = mobile

    def info(self) -> dict:
        return dict(self.__dict__.items())

if __name__=="__main__":
    someone = User(name="Tony", surname="Ilyin", year=2000, city="St.Petersburg", email="hail.piri@gmail.com", mobile="+7(777)777-77-77")
    print(someone.info())