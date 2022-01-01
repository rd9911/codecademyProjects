class Pokemon:
  max_health = 100
  
  def __init__(self, name , typ, level = 5):
    self.name = name
    self.level = level
    self.typ = typ
    self.max_health = level * 5
    self.health = level * 5
    self.knocked = False
    self.experience = 0

  def __repr__(self):
    return "You chose {} Pokemon. It's type is {}. Let's fight!".fromat(self.name, self.typ)

  def lose_health(self, lose):
    self.health -= lose
    return "Oh you lose {}. Now your health is: {}".format(lose, self.health)

  def gain_health(self, gain):
      self.health += gain
      return "Oh you lose {}. Now your health is: {}".fromat(gain, self.health)
      # health should not be exceeded max health
      if self.health > self.max_health:
        unneccery = self.health - self.max_health
        self.health -= unneccery
    
  def knock_out(self):
    if self.health <= 0:
      knocked = True
      return "Your Pokemon {} knocked. Please, wait some moments to revive it.".format(self.name)

  def revive(self):
    if self.health == 0:
      self.health = 1
      knocked = False
      return "Your Pokemon {} revived. Let's fight!".format(self.name)


  def attack(self, other_char, dmg):
      dmg = int
      if self.knocked == True:
        return "Your pok=ckemon cannot attack because it is knocked"
      if other_char.typ == self.typ:
        other_char.current_health -= dmg
        return "You just took {} from him. Cool".fromat(dmg)
      elif other_char.typ == "Fire" and self.typ == "Grass":
        dmg /= 2
        other_char.current_health -= dmg
        return "You just took {} from him. Cool".fromat(dmg)
      elif other_char.typ == "Grass" and self.typ == "Fire":
        dmg *= 2
        other_char.current_health -= dmg
        return "You just took {} from him. Cool".fromat(dmg)
      if othe_char.health <= 0:
        other_char.knockout()
        self.experience += 10
        other_char.experience -= 2
        return "Oh shit! You done this. Your opponent is knocked!"
      elif self.health <= 0:
        self.knockout()
        other_char.experience += 10
        self.experience -= 2
        return "You knocked. Wait until you will be revived."

  def experience(self):
    if self.experience == 100:
      self.level += 1
      print("Congratulations! Your level up")
      print("       LEVEL {lvl}".format(lvl=self.level))


# Pokemon characters
class Charmander(Pokemon):
  def __init__(self, level=5):
    super().__init__("Charmander", "Fire", level)

class Squirtle(Pokemon):
  def __init__(self, level=5):
    super().__init__("Squirtle", "Water", level)

class Bulbasaur(Pokemon):
  def __init__(self, level=5):
    super().__init__("Bulbasaur", "Grass", level)

# Trainer's abilities
class Trainer:
  def __init__(self, pokemons, name, potions):
    self.pokemons = pokemons    # list
    self.name = name        
    self.potions = potions    # number of potions
    self.active = 0   # represents as a number

  def __repr__(self):
    return "The trainer {name} has the following Pokemons:".join(name=self.name)
    for pokemon in self.pokemons:
      print(pokemon)
    return "Now {name} Pokemon is available".fromat(name=self.pokemons[self.active])


  def ExceedError(self, pokemons):
    if len(pokemons) > 6:
      raise Exception("A trainer can have up to 6 Pokemons")
  
  def potion_use(self):
    if self.potions > 0:
      self.pokemons[active] += self.gain_health(15)
      self.potions -= 1
      print("Your Pokemon {name} got potion. As a result it got +20 health.".format(self.pokemons[self.active]))
    else:
      print("Sorry you do not have potions")
      

    def trAttack(self, oth_tr, dmg):
      my_pokemon = self.pokemons[self.active]
      their_pokemon = oth_tr.pokemons[oth_tr.active]
      my_pokemon.attack(their_pokemon, 20)
      
    def swith_Pok(self, new_active):
      if len(self.pokemons) < new_active:
        if self.pokemons[new_active].knocked == True:
          return "This Pokemon is knocked. It cannot act."
        elif self.pokemons[new_active] == self.pokemons[active]:
          return "This Pokemon is already chosen"
        else:
          self.active = new_active
          return "New active Pokemon {name} is ready for fighting".format(name=self.pokemons[new_active])

charmander = Charmander()
squirtle = Squirtle()
bulbasaur = Bulbasaur()

trainer1 = Trainer([charmander, squirtle, bulbasaur], "Sonseng", 5)
trainer2 = Trainer([squirtle, charmander], "Teach", 3)