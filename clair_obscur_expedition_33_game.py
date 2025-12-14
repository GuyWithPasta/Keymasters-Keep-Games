from __future__ import annotations

import functools
from typing import List, Dict, Set

from dataclasses import dataclass

from Options import Toggle, OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


# Option Dataclass
@dataclass
class ClairObscurExpedition33ArchipelagoOptions:
    pass

# Main Class
class ClairObscurExpedition33Game(Game):
    name = "Clair Obscur: Expedition 33"
    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = [
        KeymastersKeepGamePlatforms.PS5,
        KeymastersKeepGamePlatforms.XSX,
    ]

    is_adult_only_or_unrated = False

    options_cls = ClairObscurExpedition33ArchipelagoOptions


    # Main Objectives
    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="In Lumière, do the following before walking to the pier: PROLOGUE1",
                data={
                    "PROLOGUE1": (self.prologue, 5),
                },
                weight=10,
            ),
            GameObjectiveTemplate(
                label="Before the Expedition commences, spend all three Festival Tokens",
                weight=10,
            ),
            GameObjectiveTemplate(
                label="In Spring Meadows, find and master the following Pictos: SMPICTOS",
                data={
                    "SMPICTOS": (self.area_1_pictos, 4),
                },
            ),
            GameObjectiveTemplate(
                label="In Spring Meadows, aquire the following Weapons: SMWEAPS",
                data={
                    "SMWEAPS": (self.area_1_weapons, 2),
                },
            ),
            GameObjectiveTemplate(
                label="In Spring Meadows, assist Jar, the first White Nevron",
            ),
            GameObjectiveTemplate(
                label="In Spring Meadows, Defeat Eveque",
            ),
            GameObjectiveTemplate(
                label="Reach Flying Waters",
            ),
            GameObjectiveTemplate(
                label="In Flying Waters, find and master the following Pictos: FWPICTOS",
                data={
                    "FWPICTOS": (self.area_2_pictos, 5),
                },
            ),
            GameObjectiveTemplate(
                label="In Flying Waters, dual Noco, then buy out his secret shop",
                weight=50000,
            ),
            GameObjectiveTemplate(
                label="In Flying Waters, find the following weapons: FWWEAPONS",
                data={
                    "FWWEAPONS": (self.area_2_weapons, 3),
                },
            ),
            GameObjectiveTemplate(
                label="In Flying Waters, assist Demineur Nevron, the second White Nevron",
            ),
            GameObjectiveTemplate(
                label="In Flying Waters, Defeat Goblu",
            ),
            GameObjectiveTemplate(
                label="Reach Ancient Sanctuary",
                data={
                    "FWWEAPONS": (self.area_2_weapons, 3),
                },
            ),
            GameObjectiveTemplate(
                label="In Ancient Sanctuary, find and master the following Pictos: ASPICTOS",
                data={
                    "ASPICTOS": (self.area_3_pictos, 3),
                },
            ),
            GameObjectiveTemplate(
                label="In Ancient Sanctuary, find the following weapon: ASWEAPONS",
                data={
                    "ASWEAPONS": (self.area_3_weapons, 1),
                },
            ),
            GameObjectiveTemplate(
                label="In Flying Waters, find the following weapons: FWWEAPONS",
                data={
                    "FWWEAPONS": (self.area_2_weapons, 3),
                },
            ),
            GameObjectiveTemplate(
                label="In Ancient Sanctuary, Defeat Ultimate Sakapatate",
            ),
            GameObjectiveTemplate(
                label="Gustave: Perform an Overcharge with 10 Charge",
            ),
            GameObjectiveTemplate(
                label="Lune: Use Immolation on a Marked foe",
            ),
            GameObjectiveTemplate(
                label="Lune: Consume Stains two turns in a row",
            ),
            GameObjectiveTemplate(
                label="Maelle: Use Percée on a Marked foe",
            ),
            GameObjectiveTemplate(
                label="Maelle: Use Spark while in Offensive Stance",
            ),
            GameObjectiveTemplate(
                label="In ZONE, defeat the Mime",
                data={
                    "ZONE": (self.zones, 1),
                },
            ),
        ]
   
    @staticmethod
    def prologue() -> List[str]:
        return [
            "Encounter a Mime",
            "Steal from a trash can",
            "Explode a Ball",
            "Duel 2 women",
            "Obtain a red uniform",
        ]
    def area_1_pictos() -> List[str]:
        return [
            "Dodger",
            "Critical Burn",
            "Augmented Attack",
            "Dead Energy 2",
            "Burning Shots",
            "Cleansing Tint",
            "Empowering Attack",
        ]
    def area_2_pictos() -> List[str]:
        return [
            "SOS Shell",
            "Marking Shots",
            "Exposing Attack",
            "Augmented Aim",
            "Staggering Attack",
            "Rewarding Mark",
            "Augmented Counter",
            "Energizing Break",
            "Versatile",
        ]
    def area_3_pictos() -> List[str]:
        return [
            "Energizing Jump",
            "Burning Mark",
            "Energizing Start 2",
            "Attack Lifesteal",
            "Breaker",
            "Stun Boost",
        ]
    def area_1_weapons() -> List[str]:
        return [
            "Lanceram",
            "Lighterim",
        ]
    def area_2_weapons() -> List[str]:
        return [
            "Brulerum",
            "Demimerim",
            "Cruleram",
            "Abysseram",
            "Troubadim",
        ]
    def area_3_weapons() -> List[str]:
        return [
            "Sakaram",
            "Trebuchim",
        ]
    def zones() -> List[str]:
        return [
            "Spring Meadows",
            "Flying Waters",
            "Ancient Sanctuary",
        ]

# Archipelago Options

# TODO: Add which zones can be rolled to extend/constrict required playtime
