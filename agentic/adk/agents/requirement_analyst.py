# agentic/adk/agents/requirement_analyst.py

class RequirementAnalyst:
    """Agente para generar especificaciones de historias de usuario en formato canónico."""
    def generate_user_story(self, person: str, requirement: str, goal: str) -> str:
        return f"As {person}, I need {requirement} in order to {goal}."
