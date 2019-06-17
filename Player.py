from Tools import myPrint

class Player:

    # Initializer / Instance Attributes
    def __init__(self):
        self.name = 'N/a'
        self.race = 'N/a'
        self.hp = 0
        self.classType = 'N/a'
        self.armorType = 'N/a'
        self.weaponProf = 'N/a'

    def __str__():
        myPrint(('-'*14)+'\n'+'Player Details:')
        myPrint("Name: "+name+"\tRace: "+race+"\tCurrent HP: "+hp+"\tClass: "+classType+"\tArmor proficiency: "+armorType+"\tWeapon proficiency: "+weaponProf+"\t")
        myPrint(('-'*14)+'\n'+'Player Details:')

        

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self,name):
        self.name=name     

    @property
    def race(self):
        return race

    @race.setter
    def race(self,race):
        self.race=race  

    @property
    def hp(self):
        return hp

    @hp.setter
    def hp(self):
        self.hp=hp  

    @property
    def classType(self):
        return classType

    @classType.setter
    def classType(self,classType):
        self.classType=classType

    @property
    def armorType(self):
        return armorType

    @armorType.setter
    def armorType(self,armorType):
        self.armorType=armorType

    @property
    def weaponProf(self):
        return weaponProf

    @weaponProf.setter
    def weaponProf(self,weaponProf):
        self.weaponProf=weaponProf