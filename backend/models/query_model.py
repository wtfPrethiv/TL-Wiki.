from pydantic import BaseModel, Field, field_validator
import re

class WikiInput(BaseModel):

    topic : str = Field(...,
                           min_length=1,
                           max_length=265, 
                           description="Enter the wiki topic to summarize")

@field_validator('topic')

@classmethod
def strCheck(cls, value):
    allowed_pattern = r"^[\w\s\-,.'?!]+$"
    
    if not re.match(allowed_pattern, value.strip):
        raise ValueError("Query Contains invalid error !!")
    
    return value.strip()

