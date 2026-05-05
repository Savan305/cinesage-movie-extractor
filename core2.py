from dotenv import load_dotenv
load_dotenv()

from typing import List, Optional
from pydantic import BaseModel
from langchain_core.output_parsers import PydanticOutputParser
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

# Model
model = ChatMistralAI(
    model="mistral-small-2506",
    temperature=0
)

# Schema
class Movie(BaseModel):
    title: str
    release_year: Optional[int]
    genre: List[str]
    director: Optional[str]
    cast: List[str]
    rating: Optional[float]
    summary: Optional[str]

# Parser
parser = PydanticOutputParser(pydantic_object=Movie)

# Prompt
prompt = ChatPromptTemplate.from_messages([

    ("system", """You are an expert information extraction system.

Extract movie information from the given paragraph.

{format_instructions}
"""),

    ("human", """Paragraph:
{paragraph}
""")
])

# Chain
chain = prompt | model

# Input
para = input("Give your paragraph: ")

# Invoke
response = chain.invoke({
    "paragraph": para,
    "format_instructions": parser.get_format_instructions()
})
model_data = parser.parse(response.content)

print("\n🔹 Extracted Information:\n")
print(model_data)