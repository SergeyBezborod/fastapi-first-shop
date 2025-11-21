from pydantic import BaseModel, Field


class CategoryBase(BaseModel):
    # ... - поле обязательное
    name: str = Field(..., min_length=5, max_length=255, description="Category name")
    slug: str = Field(..., min_length=5, max_length=255, description="URL-friendly category name")


class CategoryCreate(CategoryBase):
    pass


class CategoryResponse(CategoryBase):
    id: int = Field(..., description="Unique category identifier")

    class Config:
        from_attributes = True