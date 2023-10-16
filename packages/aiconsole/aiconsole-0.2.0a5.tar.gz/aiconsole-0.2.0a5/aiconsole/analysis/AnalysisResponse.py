from typing import List
from typing_extensions import TypedDict

class AgentDict(TypedDict):
    id: str
    name: str
    usage: str
    system: str
    execution_mode: str

class MaterialDict(TypedDict):
    id: str
    usage: str
    content: str

class AnalysisResponse(TypedDict):
    next_step: str
    agent: AgentDict | None
    materials: List[MaterialDict]
