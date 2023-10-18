from pydantic import BaseModel, Extra


class DeploymentBaseModel(BaseModel):
    class Config:
        extra = Extra.forbid
