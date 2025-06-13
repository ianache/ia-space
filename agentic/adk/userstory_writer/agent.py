"""UserStory_Writer: An agent that writes user stories based on user input."""
from google.adk.agents import Agent, LlmAgent
from google.adk.tools.agent_tool import AgentTool

from . import prompt

MODEL = "gemini-2.5-flash-preview-04-17"

userstory_writer = Agent(
    name="userstory_writer",
    description="An agent that writes user stories based on user input.",
    model=MODEL,
    instruction=prompt.REQUIREMENTS_SPECIFICATION_COORDINATOR,
    output_key="user_story",
    tools=[
#        AgentTool(
#            name="UserStoryWriter",
#            description="Writes user stories based on user input.",
#            func=prompt.write_user_story,
#        )
    ],
)

root_agent = userstory_writer