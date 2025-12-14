from __future__ import annotations

from typing import List, Dict, Set

from dataclasses import dataclass

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


# Option Dataclass
@dataclass
class KirbyAirRidersArchipelagoOptions:
    pass

# Main Class
class KirbyAirRidersGame(Game):
    name = "Kirby Air Riders"
    platform = KeymastersKeepGamePlatforms.SW2

    platforms_other = None

    is_adult_only_or_unrated = False

    options_cls = KirbyAirRidersArchipelagoOptions

    # Optional Game Constraints
    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Complete all Trials Online! (Real people count as Level 10 CPUs)",
            ),
        ]

    # Main Objectives
    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Air Ride: Win a race on AIRTRACK as RIDER using MACHINE against level CPULEVEL CPUs",
                data={
                    "AIRTRACK": (self.air_ride_tracks, 1),
                    "RIDER": (self.riders, 1),
                    "MACHINE": (self.machine, 1),
                    "CPULEVEL": (self.cpu_level_all, 1),
                },
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Air Ride: Get a new Time Trial Record with the MACHINE or on AIRTRACK",
                data={
                    "AIRTRACK": (self.air_ride_tracks, 1),
                    "MACHINE": (self.machine, 1),
                },
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Top Ride: Get a new Time Trial Record with the MACHINE or on TOPTRACK",
                data={
                    "TOPTRACK": (self.top_ride_tracks, 1),
                    "MACHINE": (self.machine, 1),
                },
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Top Ride: Win a race on TOPTRACK as RIDER using MACHINE against level CPULEVEL CPUs",
                data={
                    "TOPTRACK": (self.top_ride_tracks, 1),
                    "RIDER": (self.riders, 1),
                    "MACHINE": (self.machine, 1),
                    "CPULEVEL": (self.cpu_level_all, 1),
                },
                weight=3,
            ),
            GameObjectiveTemplate(
                label="City Trial: As RIDER, find a MACHINE to Win the Stadium against level CPULEVEL CPUs",
                data={
                    "RIDER": (self.riders, 1),
                    "MACHINE": (self.machine, 1),
                    "CPULEVEL": (self.cpu_level_all, 1),
                },
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Road Trip: Complete a Stage as RIDER",
                data={
                    "RIDER": (self.riders_road_trip, 1),
                },
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Customize a new MACHINE",
                data={
                    "MACHINE": (self.machine, 1),
                },
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Check off LOWCOUNT new checkboxes in GAMEMODE",
                data={
                    "LOWCOUNT": (self.low_random, 1),
                    "GAMEMODE": (self.game_modes, 1),
                },
            ),
        ]

    # Datasets
    @staticmethod
    def air_ride_tracks() -> List[str]:
        return [
            "Floria Fields",
            "Waveflow Waters",
            "Airtopia Ruins",
            "Crystalline Fissure",
            "Steamgust Forge",
            "Cavernous Corners",
            "Cyberion Highway",
            "Mount Amberfalls",
            "Galactic Nova",
            "Fantasy Meadows",
            "Celestial Valley",
            "Sky Sands",
            "Frozen Hillside",
            "Magma Flows",
            "Beanstalk Park",
            "Machine Passage",
            "Checker Knights",
            "Nebula Belt",
        ]
    @staticmethod
    def top_ride_tracks() -> List[str]:
        return [
            "Flower",
            "Flow",
            "Air",
            "Crystal",
            "Steam",
            "Cave",
            "Cyber",
            "Mountain",
            "Nova",
        ]
    
    @staticmethod
    def riders() -> List[str]:
        return [
            "Kirby",
            "King Dedede",
            "Meta Knight",
            "Bandana Waddle Dee",
            "Waddle Doo",
            "Chef Kawasaki",
            "Knuckle Joe",
            "Gooey",
            "Cappy",
            "Starman",
            "Magalor",
            "Susie",
            "Waddle Dee",
            "Rick",
            "Rocky",
            "Scarfy",
            "Lololo and Lalala",
            "Marx",
            "Daroach",
            "Taranza",
            "Noir Dedede",
        ]
    @staticmethod    
    def riders_road_trip(self) -> List[str]:
        riders: List[str] = self.riders()
        riders.remove("Noir Dedede")
        return riders
    @staticmethod
    def machine(self) -> List[str]:
        return [
            "Warp Star",
            "Winged Star",
            "Shadow Star",
            "Wagon Star",
            "Slink Star",
            "Formula Star",
            "Bulk Star",
            "Rocket Star",
            "Swerve Star",
            "Turbo Star",
            "Jet Star",
            "Wheelie Bike",
            "Rex Wheelie",
            "Wheelie Scooter",
            "Hop Star",
            "Vampire Star",
            "Paper Star",
            "Chariot",
            "Battle Chariot",
            "Tank Star",
            "Bull Tank",
            "Transform Star",
        ]

    @staticmethod
    def cpu_level_all() -> range:
        return range(1, 10)
        
    @staticmethod
    def low_random() -> range:
        return range(2, 6)
        
    @staticmethod
    def game_modes() -> List[str]:
        return [
            "Air Ride",
            "Top Ride",
            "City Trial",
        ]

# Archipelago Options

# TODO: Learn how to restrict trials based on selected modes