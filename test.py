class Email:
    _name: str
    _affiliation: str

    def __init__(self, name: str, aff: str) -> None:
        self._name = name
        self._affiliation = aff

    def emailstr(self) -> str:
        return self._name + "@" + self._affiliation

    def __str__(self) -> str:
        return self._name + "@" + self._affiliation


class User:
    _email_addr: "Email"
    _username: str
    _password: str

    def __init__(self, email_addr: "Email", username: str, password: str) -> None:
        self._email_addr = email_addr
        self._username = username
        self._password = password

    def __str__(self) -> str:
        return self._email_addr.__str__() + " - " + self._username + " - " + str(hash(self._password))