from pydantic import BaseModel


class QueryRequest(BaseModel):

    query: str
    output_language: str | None = None
