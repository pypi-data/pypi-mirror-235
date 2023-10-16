from pydantic import BaseModel, field_validator


class Dependency(BaseModel):
    name: str
    depends_on: set[str] = {}

    def __hash__(self):
        return self.name.__hash__()

    @field_validator("depends_on", mode="before")
    def convert_depends_to_set(cls, depends_on_raw, _info) -> set[str]:
        if isinstance(depends_on_raw, list):
            return set(depends_on_raw)
        return depends_on_raw
