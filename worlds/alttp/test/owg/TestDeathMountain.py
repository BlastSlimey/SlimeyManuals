from .TestVanillaOWG import TestVanillaOWG


class TestDeathMountain(TestVanillaOWG):

    def testWestDeathMountain(self):
        self.run_location_tests([
            ["Ether Tablet", False, []],
            ["Ether Tablet", False, ['Progressive Sword'], ['Progressive Sword']],
            ["Ether Tablet", False, [], ['Book of Mudora']],
            ["Ether Tablet", False, [], ['Pegasus Boots', 'Progressive Glove', 'Flute']],
            ["Ether Tablet", False, [], ['Pegasus Boots', 'Lamp', 'Flute']],
            ["Ether Tablet", False, [], ['Pegasus Boots', 'Magic Mirror', 'Hookshot']],
            ["Ether Tablet", False, [], ['Pegasus Boots', 'Magic Mirror', 'Hammer']],
            ["Ether Tablet", True, ['Pegasus Boots', 'Book of Mudora', 'Progressive Sword', 'Progressive Sword']],
            ["Ether Tablet", True, ['Flute', 'Magic Mirror', 'Book of Mudora', 'Progressive Sword', 'Progressive Sword']],
            ["Ether Tablet", True, ['Progressive Glove', 'Lamp', 'Magic Mirror', 'Book of Mudora', 'Progressive Sword', 'Progressive Sword']],
            ["Ether Tablet", True, ['Flute', 'Hammer', 'Hookshot', 'Book of Mudora', 'Progressive Sword', 'Progressive Sword']],
            ["Ether Tablet", True, ['Progressive Glove', 'Lamp', 'Hammer', 'Hookshot', 'Book of Mudora', 'Progressive Sword', 'Progressive Sword']],

            ["Old Man", False, []],
            ["Old Man", False, [], ['Lamp']],
            ["Old Man", False, [], ['Pegasus Boots', 'Progressive Glove', 'Flute']],
            ["Old Man", True, ['Pegasus Boots', 'Lamp']],
            ["Old Man", True, ['Flute', 'Lamp']],
            ["Old Man", True, ['Progressive Glove', 'Lamp']],

            ["Spectacle Rock Cave", False, []],
            ["Spectacle Rock Cave", False, [], ['Pegasus Boots', 'Progressive Glove', 'Flute']],
            ["Spectacle Rock Cave", False, [], ['Pegasus Boots', 'Lamp', 'Flute']],
            ["Spectacle Rock Cave", True, ['Pegasus Boots']],
            ["Spectacle Rock Cave", True, ['Flute']],
            ["Spectacle Rock Cave", True, ['Progressive Glove', 'Lamp']],

            ["Spectacle Rock", False, []],
            ["Spectacle Rock", False, [], ['Pegasus Boots', 'Progressive Glove', 'Flute']],
            ["Spectacle Rock", False, [], ['Pegasus Boots', 'Lamp', 'Flute']],
            ["Spectacle Rock", False, [], ['Pegasus Boots', 'Magic Mirror']],
            ["Spectacle Rock", True, ['Pegasus Boots']],
            ["Spectacle Rock", True, ['Flute', 'Magic Mirror']],
            ["Spectacle Rock", True, ['Progressive Glove', 'Lamp', 'Magic Mirror']],
        ])

    def testEastDeathMountain(self):
        self.run_location_tests([
            ["Mimic Cave", False, []],
            ["Mimic Cave", False, [], ['Magic Mirror']],
            ["Mimic Cave", False, [], ['Hammer']],
            ["Mimic Cave", False, [], ['Pegasus Boots', 'Flute', 'Lamp']],
            ["Mimic Cave", False, [], ['Pegasus Boots', 'Flute', 'Progressive Glove']],
            ["Mimic Cave", False, [], ['Bomb Upgrade (+5)', 'Bomb Upgrade (+10)', 'Bomb Upgrade (50)', 'Hookshot', 'Hammer']],
            ["Mimic Cave", True, ['Bomb Upgrade (+5)', 'Magic Mirror', 'Hammer', 'Pegasus Boots']],
            ["Mimic Cave", True, ['Bomb Upgrade (+5)', 'Magic Mirror', 'Hammer', 'Progressive Glove', 'Lamp']],
            ["Mimic Cave", True, ['Bomb Upgrade (+5)', 'Magic Mirror', 'Hammer', 'Flute']],

            ["Spiral Cave", False, []],
            ["Spiral Cave", False, [], ['Pegasus Boots', 'Progressive Glove', 'Flute']],
            ["Spiral Cave", False, [], ['Pegasus Boots', 'Magic Mirror', 'Hookshot']],
            ["Spiral Cave", True, ['Pegasus Boots']],
            ["Spiral Cave", True, ['Flute', 'Hookshot']],
            ["Spiral Cave", True, ['Progressive Glove', 'Lamp', 'Hookshot']],
            ["Spiral Cave", True, ['Progressive Glove', 'Lamp', 'Magic Mirror']],
            ["Spiral Cave", True, ['Flute', 'Magic Mirror']],

            ["Paradox Cave Lower - Far Left", False, []],
            ["Paradox Cave Lower - Far Left", False, [], ['Pegasus Boots', 'Progressive Glove', 'Flute']],
            ["Paradox Cave Lower - Far Left", False, [], ['Pegasus Boots', 'Magic Mirror', 'Hookshot']],
            ["Paradox Cave Lower - Far Left", False, ['Bomb Upgrade (+5)', 'Bomb Upgrade (+10)', 'Bomb Upgrade (50)', 'Progressive Sword', 'Progressive Bow', 'Fire Rod', 'Cane of Somaria']],
            ["Paradox Cave Lower - Far Left", True, ['Fire Rod', 'Pegasus Boots']],
            ["Paradox Cave Lower - Far Left", True, ['Cane of Somaria', 'Flute', 'Hookshot']],
            ["Paradox Cave Lower - Far Left", True, ['Progressive Sword', 'Progressive Sword', 'Progressive Glove', 'Lamp', 'Hookshot']],
            ["Paradox Cave Lower - Far Left", True, ['Progressive Bow', 'Progressive Glove', 'Lamp', 'Magic Mirror']],
            ["Paradox Cave Lower - Far Left", True, ['Bomb Upgrade (+5)', 'Flute', 'Magic Mirror']],

            ["Paradox Cave Lower - Left", False, []],
            ["Paradox Cave Lower - Left", False, [], ['Pegasus Boots', 'Progressive Glove', 'Flute']],
            ["Paradox Cave Lower - Left", False, [], ['Pegasus Boots', 'Magic Mirror', 'Hookshot']],
            ["Paradox Cave Lower - Left", False, ['Bomb Upgrade (+5)', 'Bomb Upgrade (+10)', 'Bomb Upgrade (50)', 'Progressive Sword', 'Progressive Bow', 'Fire Rod', 'Cane of Somaria']],
            ["Paradox Cave Lower - Left", True, ['Fire Rod', 'Pegasus Boots']],
            ["Paradox Cave Lower - Left", True, ['Cane of Somaria', 'Flute', 'Hookshot']],
            ["Paradox Cave Lower - Left", True, ['Progressive Sword', 'Progressive Sword', 'Progressive Glove', 'Lamp', 'Hookshot']],
            ["Paradox Cave Lower - Left", True, ['Progressive Bow', 'Progressive Glove', 'Lamp', 'Magic Mirror']],
            ["Paradox Cave Lower - Left", True, ['Bomb Upgrade (+5)', 'Flute', 'Magic Mirror']],

            ["Paradox Cave Lower - Middle", False, []],
            ["Paradox Cave Lower - Middle", False, [], ['Pegasus Boots', 'Progressive Glove', 'Flute']],
            ["Paradox Cave Lower - Middle", False, [], ['Pegasus Boots', 'Magic Mirror', 'Hookshot']],
            ["Paradox Cave Lower - Middle", False, ['Bomb Upgrade (+5)', 'Bomb Upgrade (+10)', 'Bomb Upgrade (50)', 'Progressive Sword', 'Progressive Bow', 'Fire Rod', 'Cane of Somaria']],
            ["Paradox Cave Lower - Middle", True, ['Fire Rod', 'Pegasus Boots']],
            ["Paradox Cave Lower - Middle", True, ['Cane of Somaria', 'Flute', 'Hookshot']],
            ["Paradox Cave Lower - Middle", True, ['Progressive Sword', 'Progressive Sword', 'Progressive Glove', 'Lamp', 'Hookshot']],
            ["Paradox Cave Lower - Middle", True, ['Progressive Bow', 'Progressive Glove', 'Lamp', 'Magic Mirror']],
            ["Paradox Cave Lower - Middle", True, ['Bomb Upgrade (+5)', 'Flute', 'Magic Mirror']],

            ["Paradox Cave Lower - Right", False, []],
            ["Paradox Cave Lower - Right", False, [], ['Pegasus Boots', 'Progressive Glove', 'Flute']],
            ["Paradox Cave Lower - Right", False, [], ['Pegasus Boots', 'Magic Mirror', 'Hookshot']],
            ["Paradox Cave Lower - Right", False, ['Bomb Upgrade (+5)', 'Bomb Upgrade (+10)', 'Bomb Upgrade (50)', 'Progressive Sword', 'Progressive Bow', 'Fire Rod', 'Cane of Somaria']],
            ["Paradox Cave Lower - Right", True, ['Fire Rod', 'Pegasus Boots']],
            ["Paradox Cave Lower - Right", True, ['Cane of Somaria', 'Flute', 'Hookshot']],
            ["Paradox Cave Lower - Right", True, ['Progressive Sword', 'Progressive Sword', 'Progressive Glove', 'Lamp', 'Hookshot']],
            ["Paradox Cave Lower - Right", True, ['Progressive Bow', 'Progressive Glove', 'Lamp', 'Magic Mirror']],
            ["Paradox Cave Lower - Right", True, ['Bomb Upgrade (+5)', 'Flute', 'Magic Mirror']],

            ["Paradox Cave Lower - Far Right", False, []],
            ["Paradox Cave Lower - Far Right", False, [], ['Pegasus Boots', 'Progressive Glove', 'Flute']],
            ["Paradox Cave Lower - Far Right", False, [], ['Pegasus Boots', 'Magic Mirror', 'Hookshot']],
            ["Paradox Cave Lower - Far Right", False, ['Bomb Upgrade (+5)', 'Bomb Upgrade (+10)', 'Bomb Upgrade (50)', 'Progressive Sword', 'Progressive Bow', 'Fire Rod', 'Cane of Somaria']],
            ["Paradox Cave Lower - Far Right", True, ['Fire Rod', 'Pegasus Boots']],
            ["Paradox Cave Lower - Far Right", True, ['Cane of Somaria', 'Flute', 'Hookshot']],
            ["Paradox Cave Lower - Far Right", True, ['Progressive Sword', 'Progressive Sword', 'Progressive Glove', 'Lamp', 'Hookshot']],
            ["Paradox Cave Lower - Far Right", True, ['Progressive Bow', 'Progressive Glove', 'Lamp', 'Magic Mirror']],
            ["Paradox Cave Lower - Far Right", True, ['Bomb Upgrade (+5)', 'Flute', 'Magic Mirror']],

            ["Paradox Cave Upper - Left", False, []],
            ["Paradox Cave Upper - Left", False, [], ['Pegasus Boots', 'Progressive Glove', 'Flute']],
            ["Paradox Cave Upper - Left", False, [], ['Pegasus Boots', 'Magic Mirror', 'Hookshot']],
            ["Paradox Cave Upper - Left", False, [], ['Bomb Upgrade (+5)', 'Bomb Upgrade (+10)', 'Bomb Upgrade (50)']],
            ["Paradox Cave Upper - Left", True, ['Bomb Upgrade (+5)', 'Pegasus Boots']],
            ["Paradox Cave Upper - Left", True, ['Bomb Upgrade (+5)', 'Flute', 'Hookshot']],
            ["Paradox Cave Upper - Left", True, ['Bomb Upgrade (+5)', 'Progressive Glove', 'Lamp', 'Hookshot']],
            ["Paradox Cave Upper - Left", True, ['Bomb Upgrade (+5)', 'Progressive Glove', 'Lamp', 'Magic Mirror']],
            ["Paradox Cave Upper - Left", True, ['Bomb Upgrade (+5)', 'Flute', 'Magic Mirror']],

            ["Paradox Cave Upper - Right", False, []],
            ["Paradox Cave Upper - Right", False, [], ['Pegasus Boots', 'Progressive Glove', 'Flute']],
            ["Paradox Cave Upper - Right", False, [], ['Pegasus Boots', 'Magic Mirror', 'Hookshot']],
            ["Paradox Cave Upper - Right", False, [], ['Bomb Upgrade (+5)', 'Bomb Upgrade (+10)', 'Bomb Upgrade (50)']],
            ["Paradox Cave Upper - Right", True, ['Bomb Upgrade (+5)', 'Pegasus Boots']],
            ["Paradox Cave Upper - Right", True, ['Bomb Upgrade (+5)', 'Flute', 'Hookshot']],
            ["Paradox Cave Upper - Right", True, ['Bomb Upgrade (+5)', 'Progressive Glove', 'Lamp', 'Hookshot']],
            ["Paradox Cave Upper - Right", True, ['Bomb Upgrade (+5)', 'Progressive Glove', 'Lamp', 'Magic Mirror']],
            ["Paradox Cave Upper - Right", True, ['Bomb Upgrade (+5)', 'Flute', 'Magic Mirror']],
        ])

    def testWestDarkWorldDeathMountain(self):
        self.run_location_tests([
            ["Spike Cave", False, []],
            ["Spike Cave", False, [], ['Progressive Glove']],
            ["Spike Cave", False, [], ['Moon Pearl']],
            ["Spike Cave", False, [], ['Hammer']],
            ["Spike Cave", False, [], ['Cape', 'Cane of Byrna']],
            ["Spike Cave", True, ['Bottle', 'Moon Pearl', 'Hammer', 'Progressive Glove', 'Lamp', 'Cape']],
            ["Spike Cave", True, ['Bottle', 'Moon Pearl', 'Hammer', 'Progressive Glove', 'Flute', 'Cape']],
            ["Spike Cave", True, ['Bottle', 'Moon Pearl', 'Hammer', 'Progressive Glove', 'Lamp', 'Cane of Byrna']],
            ["Spike Cave", True, ['Bottle', 'Moon Pearl', 'Hammer', 'Progressive Glove', 'Flute', 'Cane of Byrna']],
            ["Spike Cave", True, ['Magic Upgrade (1/2)', 'Moon Pearl', 'Hammer', 'Progressive Glove', 'Lamp', 'Cape']],
            ["Spike Cave", True, ['Magic Upgrade (1/2)', 'Moon Pearl', 'Hammer', 'Progressive Glove', 'Flute', 'Cape']],
            ["Spike Cave", True, ['Magic Upgrade (1/2)', 'Moon Pearl', 'Hammer', 'Progressive Glove', 'Lamp', 'Cane of Byrna']],
            ["Spike Cave", True, ['Magic Upgrade (1/2)', 'Moon Pearl', 'Hammer', 'Progressive Glove', 'Flute', 'Cane of Byrna']],
            ["Spike Cave", True, ['Magic Upgrade (1/4)', 'Moon Pearl', 'Hammer', 'Progressive Glove', 'Lamp', 'Cape']],
            ["Spike Cave", True, ['Magic Upgrade (1/4)', 'Moon Pearl', 'Hammer', 'Progressive Glove', 'Flute', 'Cape']],
            ["Spike Cave", True, ['Magic Upgrade (1/4)', 'Moon Pearl', 'Hammer', 'Progressive Glove', 'Lamp', 'Cane of Byrna']],
            ["Spike Cave", True, ['Magic Upgrade (1/4)', 'Moon Pearl', 'Hammer', 'Progressive Glove', 'Flute', 'Cane of Byrna']],
        ])

    def testEastDarkWorldDeathMountain(self):
        self.run_location_tests([
            ["Superbunny Cave - Top", False, []],
            ["Superbunny Cave - Top", True, ['Progressive Glove', 'Progressive Glove', 'Pegasus Boots']],
            ["Superbunny Cave - Top", True, ['Hammer', 'Pegasus Boots']],
            ["Superbunny Cave - Top", True, ['Moon Pearl', 'Pegasus Boots']],
            ["Superbunny Cave - Top", True, ['Progressive Glove', 'Progressive Glove', 'Hookshot', 'Flute']],
            ["Superbunny Cave - Top", True, ['Magic Mirror', 'Flute']],
            ["Superbunny Cave - Top", True, ['Progressive Glove', 'Progressive Glove', 'Hookshot', 'Lamp']],
            ["Superbunny Cave - Top", True, ['Progressive Glove', 'Magic Mirror', 'Lamp']],

            ["Superbunny Cave - Bottom", False, []],
            ["Superbunny Cave - Bottom", True, ['Progressive Glove', 'Progressive Glove', 'Pegasus Boots']],
            ["Superbunny Cave - Bottom", True, ['Hammer', 'Pegasus Boots']],
            ["Superbunny Cave - Bottom", True, ['Moon Pearl', 'Pegasus Boots']],
            ["Superbunny Cave - Bottom", True, ['Progressive Glove', 'Progressive Glove', 'Hookshot', 'Flute']],
            ["Superbunny Cave - Bottom", True, ['Magic Mirror', 'Flute']],
            ["Superbunny Cave - Bottom", True, ['Progressive Glove', 'Progressive Glove', 'Hookshot', 'Lamp']],
            ["Superbunny Cave - Bottom", True, ['Progressive Glove', 'Magic Mirror', 'Lamp']],

            ["Hookshot Cave - Bottom Right", False, []],
            ["Hookshot Cave - Bottom Right", False, [], ['Progressive Glove', 'Pegasus Boots']],
            ["Hookshot Cave - Bottom Right", False, [], ['Moon Pearl']],
            ["Hookshot Cave - Bottom Right", True, ['Moon Pearl', 'Pegasus Boots', 'Bomb Upgrade (50)']],
            ["Hookshot Cave - Bottom Right", True, ['Moon Pearl', 'Progressive Glove', 'Progressive Glove', 'Hookshot', 'Flute']],
            ["Hookshot Cave - Bottom Right", True, ['Moon Pearl', 'Progressive Glove', 'Progressive Glove', 'Hookshot', 'Lamp']],

            ["Hookshot Cave - Bottom Left", False, []],
            ["Hookshot Cave - Bottom Left", False, [], ['Progressive Glove', 'Pegasus Boots']],
            ["Hookshot Cave - Bottom Left", False, [], ['Moon Pearl']],
            ["Hookshot Cave - Bottom Left", False, [], ['Hookshot']],
            ["Hookshot Cave - Bottom Left", True, ['Moon Pearl', 'Pegasus Boots', 'Hookshot', 'Bomb Upgrade (50)']],
            ["Hookshot Cave - Bottom Left", True, ['Moon Pearl', 'Progressive Glove', 'Progressive Glove', 'Hookshot', 'Flute']],
            ["Hookshot Cave - Bottom Left", True, ['Moon Pearl', 'Progressive Glove', 'Progressive Glove', 'Hookshot', 'Lamp']],

            ["Hookshot Cave - Top Left", False, []],
            ["Hookshot Cave - Top Left", False, [], ['Progressive Glove', 'Pegasus Boots']],
            ["Hookshot Cave - Top Left", False, [], ['Moon Pearl']],
            ["Hookshot Cave - Top Left", False, [], ['Hookshot']],
            ["Hookshot Cave - Top Left", True, ['Moon Pearl', 'Pegasus Boots', 'Hookshot', 'Bomb Upgrade (50)']],
            ["Hookshot Cave - Top Left", True, ['Moon Pearl', 'Progressive Glove', 'Progressive Glove', 'Hookshot', 'Flute']],
            ["Hookshot Cave - Top Left", True, ['Moon Pearl', 'Progressive Glove', 'Progressive Glove', 'Hookshot', 'Lamp']],

            ["Hookshot Cave - Top Right", False, []],
            ["Hookshot Cave - Top Right", False, [], ['Progressive Glove', 'Pegasus Boots']],
            ["Hookshot Cave - Top Right", False, [], ['Moon Pearl']],
            ["Hookshot Cave - Top Right", False, [], ['Hookshot']],
            ["Hookshot Cave - Top Right", True, ['Moon Pearl', 'Pegasus Boots', 'Hookshot', 'Bomb Upgrade (50)']],
            ["Hookshot Cave - Top Right", True, ['Moon Pearl', 'Progressive Glove', 'Progressive Glove', 'Hookshot', 'Flute']],
            ["Hookshot Cave - Top Right", True, ['Moon Pearl', 'Progressive Glove', 'Progressive Glove', 'Hookshot', 'Lamp']],
        ])