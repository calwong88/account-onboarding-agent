from dataclasses import dataclass, field

@dataclass
class RequiredDocument:
    doc_id: str
    name: str
    critical: bool = True
    classification_keywords: list = field(default_factory=list)

    