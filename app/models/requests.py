from pydantic import BaseModel, Field

class QueryRequest(BaseModel):
    query: str = Field(..., description="The research query to be processed")
    max_steps: int = Field(5, description="Maximum number of steps for the research process")
