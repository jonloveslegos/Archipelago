# This file is auto generated. More info: https://github.com/Daivuk/apdoom

from typing import List
from BaseClasses import TypedDict

class RegionDict(TypedDict, total=False): 
    name: str
    connects_to_hub: bool
    connections: List[str]


regions:List[RegionDict] = [
    # Hangar (E1M1)
    {"name":"Hangar (E1M1) Main",
     "connects_to_hub":True,
     "connections":[]},

    # Nuclear Plant (E1M2)
    {"name":"Nuclear Plant (E1M2) Main",
     "connects_to_hub":True,
     "connections":["Nuclear Plant (E1M2) Red"]},
    {"name":"Nuclear Plant (E1M2) Red",
     "connects_to_hub":False,
     "connections":["Nuclear Plant (E1M2) Main"]},

    # Toxin Refinery (E1M3)
    {"name":"Toxin Refinery (E1M3) Main",
     "connects_to_hub":True,
     "connections":["Toxin Refinery (E1M3) Blue"]},
    {"name":"Toxin Refinery (E1M3) Blue",
     "connects_to_hub":False,
     "connections":[
        "Toxin Refinery (E1M3) Yellow",
        "Toxin Refinery (E1M3) Main"]},
    {"name":"Toxin Refinery (E1M3) Yellow",
     "connects_to_hub":False,
     "connections":["Toxin Refinery (E1M3) Blue"]},

    # Command Control (E1M4)
    {"name":"Command Control (E1M4) Main",
     "connects_to_hub":True,
     "connections":[
        "Command Control (E1M4) Blue",
        "Command Control (E1M4) Yellow"]},
    {"name":"Command Control (E1M4) Blue",
     "connects_to_hub":False,
     "connections":["Command Control (E1M4) Main"]},
    {"name":"Command Control (E1M4) Yellow",
     "connects_to_hub":False,
     "connections":["Command Control (E1M4) Main"]},

    # Phobos Lab (E1M5)
    {"name":"Phobos Lab (E1M5) Main",
     "connects_to_hub":True,
     "connections":["Phobos Lab (E1M5) Yellow"]},
    {"name":"Phobos Lab (E1M5) Yellow",
     "connects_to_hub":False,
     "connections":[
        "Phobos Lab (E1M5) Main",
        "Phobos Lab (E1M5) Blue",
        "Phobos Lab (E1M5) Green"]},
    {"name":"Phobos Lab (E1M5) Blue",
     "connects_to_hub":False,
     "connections":[
        "Phobos Lab (E1M5) Green",
        "Phobos Lab (E1M5) Yellow"]},
    {"name":"Phobos Lab (E1M5) Green",
     "connects_to_hub":False,
     "connections":[
        "Phobos Lab (E1M5) Main",
        "Phobos Lab (E1M5) Blue"]},

    # Central Processing (E1M6)
    {"name":"Central Processing (E1M6) Main",
     "connects_to_hub":True,
     "connections":[
        "Central Processing (E1M6) Yellow",
        "Central Processing (E1M6) Red",
        "Central Processing (E1M6) Blue",
        "Central Processing (E1M6) Nukage"]},
    {"name":"Central Processing (E1M6) Red",
     "connects_to_hub":False,
     "connections":["Central Processing (E1M6) Main"]},
    {"name":"Central Processing (E1M6) Blue",
     "connects_to_hub":False,
     "connections":["Central Processing (E1M6) Main"]},
    {"name":"Central Processing (E1M6) Yellow",
     "connects_to_hub":False,
     "connections":["Central Processing (E1M6) Main"]},
    {"name":"Central Processing (E1M6) Nukage",
     "connects_to_hub":False,
     "connections":["Central Processing (E1M6) Yellow"]},

    # Computer Station (E1M7)
    {"name":"Computer Station (E1M7) Main",
     "connects_to_hub":True,
     "connections":[
        "Computer Station (E1M7) Red",
        "Computer Station (E1M7) Yellow"]},
    {"name":"Computer Station (E1M7) Blue",
     "connects_to_hub":False,
     "connections":["Computer Station (E1M7) Yellow"]},
    {"name":"Computer Station (E1M7) Red",
     "connects_to_hub":False,
     "connections":["Computer Station (E1M7) Main"]},
    {"name":"Computer Station (E1M7) Yellow",
     "connects_to_hub":False,
     "connections":[
        "Computer Station (E1M7) Blue",
        "Computer Station (E1M7) Courtyard",
        "Computer Station (E1M7) Main"]},
    {"name":"Computer Station (E1M7) Courtyard",
     "connects_to_hub":False,
     "connections":["Computer Station (E1M7) Yellow"]},

    # Phobos Anomaly (E1M8)
    {"name":"Phobos Anomaly (E1M8) Main",
     "connects_to_hub":False,
     "connections":[]},
    {"name":"Phobos Anomaly (E1M8) Start",
     "connects_to_hub":True,
     "connections":["Phobos Anomaly (E1M8) Main"]},

    # Military Base (E1M9)
    {"name":"Military Base (E1M9) Main",
     "connects_to_hub":True,
     "connections":[
        "Military Base (E1M9) Blue",
        "Military Base (E1M9) Yellow",
        "Military Base (E1M9) Red"]},
    {"name":"Military Base (E1M9) Blue",
     "connects_to_hub":False,
     "connections":["Military Base (E1M9) Main"]},
    {"name":"Military Base (E1M9) Red",
     "connects_to_hub":False,
     "connections":["Military Base (E1M9) Main"]},
    {"name":"Military Base (E1M9) Yellow",
     "connects_to_hub":False,
     "connections":["Military Base (E1M9) Main"]},

    # Deimos Anomaly (E2M1)
    {"name":"Deimos Anomaly (E2M1) Main",
     "connects_to_hub":True,
     "connections":[
        "Deimos Anomaly (E2M1) Red",
        "Deimos Anomaly (E2M1) Blue"]},
    {"name":"Deimos Anomaly (E2M1) Blue",
     "connects_to_hub":False,
     "connections":["Deimos Anomaly (E2M1) Main"]},
    {"name":"Deimos Anomaly (E2M1) Red",
     "connects_to_hub":False,
     "connections":["Deimos Anomaly (E2M1) Main"]},

    # Containment Area (E2M2)
    {"name":"Containment Area (E2M2) Main",
     "connects_to_hub":True,
     "connections":[
        "Containment Area (E2M2) Yellow",
        "Containment Area (E2M2) Blue",
        "Containment Area (E2M2) Red"]},
    {"name":"Containment Area (E2M2) Blue",
     "connects_to_hub":False,
     "connections":["Containment Area (E2M2) Main"]},
    {"name":"Containment Area (E2M2) Red",
     "connects_to_hub":False,
     "connections":["Containment Area (E2M2) Main"]},
    {"name":"Containment Area (E2M2) Yellow",
     "connects_to_hub":False,
     "connections":["Containment Area (E2M2) Main"]},

    # Refinery (E2M3)
    {"name":"Refinery (E2M3) Main",
     "connects_to_hub":True,
     "connections":["Refinery (E2M3) Blue"]},
    {"name":"Refinery (E2M3) Blue",
     "connects_to_hub":False,
     "connections":["Refinery (E2M3) Main"]},

    # Deimos Lab (E2M4)
    {"name":"Deimos Lab (E2M4) Main",
     "connects_to_hub":True,
     "connections":["Deimos Lab (E2M4) Blue"]},
    {"name":"Deimos Lab (E2M4) Blue",
     "connects_to_hub":False,
     "connections":[
        "Deimos Lab (E2M4) Main",
        "Deimos Lab (E2M4) Yellow"]},
    {"name":"Deimos Lab (E2M4) Yellow",
     "connects_to_hub":False,
     "connections":["Deimos Lab (E2M4) Blue"]},

    # Command Center (E2M5)
    {"name":"Command Center (E2M5) Main",
     "connects_to_hub":True,
     "connections":[]},

    # Halls of the Damned (E2M6)
    {"name":"Halls of the Damned (E2M6) Main",
     "connects_to_hub":True,
     "connections":[
        "Halls of the Damned (E2M6) Blue Yellow Red",
        "Halls of the Damned (E2M6) Yellow",
        "Halls of the Damned (E2M6) One way Yellow"]},
    {"name":"Halls of the Damned (E2M6) Yellow",
     "connects_to_hub":False,
     "connections":["Halls of the Damned (E2M6) Main"]},
    {"name":"Halls of the Damned (E2M6) Blue Yellow Red",
     "connects_to_hub":False,
     "connections":["Halls of the Damned (E2M6) Main"]},
    {"name":"Halls of the Damned (E2M6) One way Yellow",
     "connects_to_hub":False,
     "connections":["Halls of the Damned (E2M6) Main"]},

    # Spawning Vats (E2M7)
    {"name":"Spawning Vats (E2M7) Main",
     "connects_to_hub":True,
     "connections":[
        "Spawning Vats (E2M7) Blue",
        "Spawning Vats (E2M7) Entrance Secret",
        "Spawning Vats (E2M7) Red",
        "Spawning Vats (E2M7) Yellow"]},
    {"name":"Spawning Vats (E2M7) Blue",
     "connects_to_hub":False,
     "connections":["Spawning Vats (E2M7) Main"]},
    {"name":"Spawning Vats (E2M7) Yellow",
     "connects_to_hub":False,
     "connections":["Spawning Vats (E2M7) Main"]},
    {"name":"Spawning Vats (E2M7) Red",
     "connects_to_hub":False,
     "connections":["Spawning Vats (E2M7) Main"]},
    {"name":"Spawning Vats (E2M7) Entrance Secret",
     "connects_to_hub":False,
     "connections":["Spawning Vats (E2M7) Main"]},

    # Tower of Babel (E2M8)
    {"name":"Tower of Babel (E2M8) Main",
     "connects_to_hub":True,
     "connections":[]},

    # Fortress of Mystery (E2M9)
    {"name":"Fortress of Mystery (E2M9) Main",
     "connects_to_hub":True,
     "connections":[
        "Fortress of Mystery (E2M9) Blue",
        "Fortress of Mystery (E2M9) Red",
        "Fortress of Mystery (E2M9) Yellow"]},
    {"name":"Fortress of Mystery (E2M9) Blue",
     "connects_to_hub":False,
     "connections":["Fortress of Mystery (E2M9) Main"]},
    {"name":"Fortress of Mystery (E2M9) Red",
     "connects_to_hub":False,
     "connections":["Fortress of Mystery (E2M9) Main"]},
    {"name":"Fortress of Mystery (E2M9) Yellow",
     "connects_to_hub":False,
     "connections":["Fortress of Mystery (E2M9) Main"]},

    # Hell Keep (E3M1)
    {"name":"Hell Keep (E3M1) Main",
     "connects_to_hub":True,
     "connections":["Hell Keep (E3M1) Narrow"]},
    {"name":"Hell Keep (E3M1) Narrow",
     "connects_to_hub":False,
     "connections":["Hell Keep (E3M1) Main"]},

    # Slough of Despair (E3M2)
    {"name":"Slough of Despair (E3M2) Main",
     "connects_to_hub":True,
     "connections":["Slough of Despair (E3M2) Blue"]},
    {"name":"Slough of Despair (E3M2) Blue",
     "connects_to_hub":False,
     "connections":["Slough of Despair (E3M2) Main"]},

    # Pandemonium (E3M3)
    {"name":"Pandemonium (E3M3) Main",
     "connects_to_hub":True,
     "connections":["Pandemonium (E3M3) Blue"]},
    {"name":"Pandemonium (E3M3) Blue",
     "connects_to_hub":False,
     "connections":["Pandemonium (E3M3) Main"]},

    # House of Pain (E3M4)
    {"name":"House of Pain (E3M4) Main",
     "connects_to_hub":True,
     "connections":["House of Pain (E3M4) Blue"]},
    {"name":"House of Pain (E3M4) Blue",
     "connects_to_hub":False,
     "connections":[
        "House of Pain (E3M4) Main",
        "House of Pain (E3M4) Yellow",
        "House of Pain (E3M4) Red"]},
    {"name":"House of Pain (E3M4) Red",
     "connects_to_hub":False,
     "connections":["House of Pain (E3M4) Blue"]},
    {"name":"House of Pain (E3M4) Yellow",
     "connects_to_hub":False,
     "connections":["House of Pain (E3M4) Blue"]},

    # Unholy Cathedral (E3M5)
    {"name":"Unholy Cathedral (E3M5) Main",
     "connects_to_hub":True,
     "connections":[
        "Unholy Cathedral (E3M5) Yellow",
        "Unholy Cathedral (E3M5) Blue"]},
    {"name":"Unholy Cathedral (E3M5) Blue",
     "connects_to_hub":False,
     "connections":["Unholy Cathedral (E3M5) Main"]},
    {"name":"Unholy Cathedral (E3M5) Yellow",
     "connects_to_hub":False,
     "connections":["Unholy Cathedral (E3M5) Main"]},

    # Mt. Erebus (E3M6)
    {"name":"Mt. Erebus (E3M6) Main",
     "connects_to_hub":True,
     "connections":["Mt. Erebus (E3M6) Blue"]},
    {"name":"Mt. Erebus (E3M6) Blue",
     "connects_to_hub":False,
     "connections":["Mt. Erebus (E3M6) Main"]},

    # Limbo (E3M7)
    {"name":"Limbo (E3M7) Main",
     "connects_to_hub":True,
     "connections":[
        "Limbo (E3M7) Red",
        "Limbo (E3M7) Blue"]},
    {"name":"Limbo (E3M7) Blue",
     "connects_to_hub":False,
     "connections":["Limbo (E3M7) Main"]},
    {"name":"Limbo (E3M7) Red",
     "connects_to_hub":False,
     "connections":[
        "Limbo (E3M7) Main",
        "Limbo (E3M7) Yellow"]},
    {"name":"Limbo (E3M7) Yellow",
     "connects_to_hub":False,
     "connections":["Limbo (E3M7) Red"]},

    # Dis (E3M8)
    {"name":"Dis (E3M8) Main",
     "connects_to_hub":True,
     "connections":[]},

    # Warrens (E3M9)
    {"name":"Warrens (E3M9) Main",
     "connects_to_hub":True,
     "connections":[
        "Warrens (E3M9) Red",
        "Warrens (E3M9) Blue",
        "Warrens (E3M9) Blue trigger"]},
    {"name":"Warrens (E3M9) Red",
     "connects_to_hub":False,
     "connections":["Warrens (E3M9) Main"]},
    {"name":"Warrens (E3M9) Blue",
     "connects_to_hub":False,
     "connections":["Warrens (E3M9) Main"]},
    {"name":"Warrens (E3M9) Blue trigger",
     "connects_to_hub":False,
     "connections":["Warrens (E3M9) Main"]},
]
