# agentic/adk/agents/requirement_reviewer.py

class RequirementReviewer:
    """Agente para revisar historias de usuario y sugerir ajustes al analyst."""
    def review_user_story(self, user_story: str) -> str:
        # Validación simple de formato canónico
        if user_story.startswith("As ") and " I need " in user_story and " in order to " in user_story:
            return "La historia de usuario cumple el formato canónico."
        else:
            return "La historia de usuario NO cumple el formato canónico. Por favor, ajusta la redacción."
