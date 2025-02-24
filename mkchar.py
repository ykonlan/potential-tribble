class mkchar:
    def __init__(self,name,realm,faction):
        self.name = name
        self.realm = realm
        self.faction = faction

    def isfromearth(self):
        if self.realm == "Earthrealm":
            print("Earthrealmer wai")
            return True
        else:
            print("Intruder alert")
            return False