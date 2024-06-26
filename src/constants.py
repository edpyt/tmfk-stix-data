from enum import Enum
from pathlib import Path
from typing import Literal

CREATOR_IDENTITY = "identity--5dcf0a7a-875b-470b-8a01-7c6a84c5e68e"

TMFK_PATH = Path(__file__).parent.parent / "ms-matrix" / "Threat-Matrix-for-Kubernetes"
TACTICS_PATH = TMFK_PATH / "docs" / "tactics"
TECHNIQUES_PATH = TMFK_PATH / "docs" / "techniques"
MITIGATIONS_PATH = TMFK_PATH / "docs" / "mitigations"

TMFK_TACTICS_MAP = {
    "InitialAccess": "MS-T0100",
    "Execution": "MS-T0200",
    "Persistence": "MS-T0300",
    "PrivilegeEscalation": "MS-T0400",
    "DefenseEvasion": "MS-T0500",
    "CredentialAccess": "MS-T0600",
    "Discovery": "MS-T0700",
    "LateralMovement": "MS-T0800",
    "Collection": "MS-T0900",
    "Impact": "MS-T1000",
}

TMFK_VERSION = "0.1"
ATTACK_SPEC_VERSION = "2.1.0"
TMFK_PLATFORM = "Kubernetes"


class Mode(Enum):
    STRICT: int = 1
    ATTACK_COMPATIBLE: int = 2


ModeEnumAttribute = Literal[Mode.STRICT, Mode.ATTACK_COMPATIBLE]

# DEFAULT_MODE = Mode.STRICT
DEFAULT_MODE = Mode.ATTACK_COMPATIBLE


class UnexpectedMode(Exception): ...


def get_collection_id(mode: ModeEnumAttribute = DEFAULT_MODE) -> str:
    match mode:
        case Mode.STRICT:
            return "x-mitre-collection--8702c9a3-cf7b-4e79-99e2-191d79c6042b"
        case Mode.ATTACK_COMPATIBLE:
            return "x-mitre-collection--704a5def-03fc-45c2-8513-e863d808c363"
        case _:
            raise UnexpectedMode("Unexpected mode")


def get_tmfk_domain(mode: ModeEnumAttribute = DEFAULT_MODE) -> str:
    match mode:
        case Mode.STRICT:
            return "tmfk"
        case Mode.ATTACK_COMPATIBLE:
            return "enterprise-attack"
        case _:
            raise UnexpectedMode("Unexpected mode")


def get_tmfk_source(mode: ModeEnumAttribute = DEFAULT_MODE) -> str:
    match mode:
        case Mode.STRICT:
            return "tmfk"
        case Mode.ATTACK_COMPATIBLE:
            return "mitre-attack"
        case _:
            raise UnexpectedMode("Unexpected mode")


def get_kill_chain_name(mode: ModeEnumAttribute = DEFAULT_MODE) -> str:
    match mode:
        case Mode.STRICT:
            return "tmfk"
        case Mode.ATTACK_COMPATIBLE:
            return "mitre-attack"
        case _:
            raise UnexpectedMode("Unexpected mode")


DEFAULT_CREATOR_JSON = f"""
{{
    "id": "{CREATOR_IDENTITY}",
    "type": "identity",
    "identity_class": "organization",
    "created": "2024-02-05T14:00:00.188Z",
    "modified": "2024-02-05T14:00:00.188Z",
    "name": "aw350m33d (Security Experts Community)",
    "spec_version": "2.1",
    "x_mitre_attack_spec_version": "2.1.0",
    "x_mitre_domains": [
        "{get_tmfk_domain()}"
    ],
    "x_mitre_version": "{TMFK_VERSION}"
}}
"""
