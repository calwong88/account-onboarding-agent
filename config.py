from dataclasses import dataclass, field
from enum import Enum

class Severity(Enum):
    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'
    NONE = "none"

@dataclass
class RequiredDocument:
    doc_id: str
    name: str
    critical: bool = True
    description: str = ""
    classification_keywords: list = field(default_factory=list)

VERIFICATION_METHODS = {
    "in_person": {
        "label": "Verified In Person (CTC)"
        # What documents does this method need?
        # What additional checks apply?
    },
    "dual_process": {
        "label": "Dual Process (Copies)"
    },
    "affiliate": {
        "label": "Affiliate (Existing BMO Product)"
    }
}

ACCOUNT_TYPES = {
    "individual": {
        "label": "Individual",
        "base_docs": [
            # Documents required REGARDLESS of verification method
            # This is your core checklist
        ],
        "verification_docs": {
            # Documents that depend on which method is used
            "in_person": [],
            "dual_process": [], 
            "affiliate": []
        },
    },
    # You'll add rrsp, joint, etc. later
}

POLICY_RULES = {
    "proof_of_address_max_age_days": 90,
    # What other rules do you enforce?
}