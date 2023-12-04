from pydantic import BaseModel, Field

class DeleteUserDTO(BaseModel):
    id: str = Field(..., title="User ID")

    class Config:
        schema_extra = {
            "example": {
                "id": "unique_user_id"
            }
        }