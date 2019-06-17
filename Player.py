class Player:

    # Initializer / Instance Attributes
    def __init__(self):
        self.name = 'N/a'
        self.species = 'N/a'
        self.hp = 0
        self.className = 'N/a'
        self.armorType = 'N/a'
        self.weaponProf = 'N/a'

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self,name):
        self.name=name     


    def get_species(self):
        return _species
    def set_species(self,species):
        self._species=species        
    def get_hp(self):
        return _hp
    def get_class(self):
        return _className
    def set_class(self,className):
        self._className=className
    def get_armorType(self):
        return _armorType
    def set_armorType(self,armorType):
        self._armorType=armorType
    def get_weaponProf(self):
        return _weaponProf