from __future__ import annotations

from typing import List

from dataclasses import dataclass

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


# Option Dataclass
@dataclass
class MetroidPrime4BeyondArchipelagoOptions:
    pass

# Main Class
class MetroidPrime4BeyondGame(Game):
    name = "Metroid Prime 4: Beyond"
    platform = KeymastersKeepGamePlatforms.SW2

    platforms_other = [
        KeymastersKeepGamePlatforms.SW,
    ]

    is_adult_only_or_unrated = False

    options_cls = MetroidPrime4BeyondArchipelagoOptions

    # Main Objectives
    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Eliminate BOSS",
                data={
                    "BOSS": (self.boss, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
            ),
            GameObjectiveTemplate(
                label="Collect COUNT UPGRADE",
                data={
                    "COUNT": (self.upgrade_count, 1),
                    "UPGRADE": (self.upgrades, 1),
                },
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Obtain the KEYITEM",
                data={
                    "KEYITEM": (self.keyitems, 1),
                },
            ),
        ]

    # Datasets
    @staticmethod
    def upgrade_count() -> range:
        return range(1, 10)
    
    @staticmethod
    def upgrades() -> List[str]:
        return [
            "Energy Tank",
            "Missile Expansion",
            "Shot Expansion",
        ]
    
    @staticmethod
    def keyitems() -> List[str]:
        return [
            "Psychic Crystal",
            "Psychic Glove",
            "Control Beam",
            "Psychic Boots",
            "Fire Shot",
            "Ice Shot",
            "Thunder Shot",
            "Psychic Lasso",
            "Psychic Boost Ball",
        ]
        
    @staticmethod
    def boss() -> List[str]:
        return [
            "Aberax",
            "Carvex",
            "Xelios",
            "Keratos",
            "Phenoros",
            "Omega Griever",
        ]
    
# Archipelago Options
# ...