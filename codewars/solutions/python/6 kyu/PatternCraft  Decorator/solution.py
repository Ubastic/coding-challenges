class Marine:
    def __init__(self, damage, armor):
        self.armor = armor
        self.damage = damage


class MarineDecorator:
    def __init__(self, marine):
        self.marine = marine

    @property
    def damage(self):
        return self.marine.damage

    @property
    def armor(self):
        return self.marine.armor


class Marine_weapon_upgrade(MarineDecorator):
    @property
    def damage(self):
        return super().damage + 1


class Marine_armor_upgrade(MarineDecorator):
    @property
    def armor(self):
        return super().armor + 1