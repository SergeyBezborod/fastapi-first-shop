from pydantic import BaseModel, Field


class CategotyBase(BaseModel):
    # ... - поле обязательное
    name: str = Field(..., min_length=5, max_length=255, description="Category name")
    slug: str = Field(..., min_length=5, max_length=255, description="URL-friendly category name")


class CategoryCreate(CategotyBase):
    pass


class CategoryResponse(CategotyBase):
    id: int = Field(..., description="Unique category identifier")

    class Config:
        form_attributes = True