class Player:

    # Initializer / Instance Attributes
    def __init__(self):
        self.name = 'N/a'
        self.race = 'N/a'
        self.classType = 'N/a'
        self.armorType = 'N/a'
        self.weaponProf = 'N/a'
        self.str=0
        self.ath=0
        self.wis=0
        self.char=0
        self.hp=0
        
    def __str__():
        myPrint(('-'*14)+'\n'+'Player Details:')
        myPrint("Name: "+name+"\tRace: "+race+"\tCurrent HP: "+hp+"\tClass: "+classType+"\tArmor proficiency: "+armorType+"\tWeapon proficiency: "+weaponProf+"\t")
        myPrint(('-'*14)+'\n'+'Player Details:')

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self,_name):
        self.name=_name     

    @property
    def race(self):
        return race

    @race.setter
    def race(self,_race):
        self.race=raceStats[_race]['name'] 
        self.str=raceStats[_race]['STR']
        self.ath=raceStats[_race]['ATH']
        self.wis=raceStats[_race]['WIS']
        self.char=raceStats[_race]['CHAR']
        self.hp=raceStats[_race]['HP']

    @property
    def classType(self):
        return classType

    @classType.setter
    def classType(self,_classType):
        self.classType = classStats[_classType]['Name']
        self.armorType = classStats[_classType]['ArmorType']
        self.weaponProf = classStats[_classType]['WeaponProf']#Tuple
        self.str+=classStats[_classType]['STR']
        self.ath+=classStats[_classType]['ATH']
        self.wis+=classStats[_classType]['WIS']
        self.char+=classStats[_classType]['CHAR']
        self.hp+=10*classStats[_classType]['HP']            


    @property
    def armorType(self):
        return armorType

    @armorType.setter
    def armorType(self,_armorType):
        self.armorType=_armorType

    @property
    def weaponProf(self):
        return weaponProf

    @weaponProf.setter
    def weaponProf(self,_weaponProf):
        self.weaponProf=_weaponProf

    @property
    def str(self):
        return str

    @str.setter
    def str(self,_str):
        self.str=_str 
    
    @property
    def ath(self):
        return ath

    @ath.setter
    def ath(self,_ath):
        self.ath=_ath 
    
    @property
    def wis(self):
        return wis

    @wis.setter
    def wis(self,_wis):
        self.wis=_wis 
    
    @property
    def char(self):
        return char

    @char.setter
    def char(self,_char):
        self.char=_char 
    
    @property
    def hp(self):
        return hp

    @hp.setter
    def hp(self,_hp):
        self.hp=_hp 
    
