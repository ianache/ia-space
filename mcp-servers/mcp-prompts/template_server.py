import os 
import logging

class TemplatesServer():
    def __init__(self):
        self.templates = self._load_templates()

    def _load_templates(self):
        templates = {}
        templates_path = os.path.join(os.path.dirname(__file__), "templates")
        for category in os.listdir(templates_path):
            category_path = os.path.join(templates_path, category)
            logging.info(category_path)
            if category in os.listdir(category_path):
                # Load config
                with open(os.path.join(category_path, "config.yaml"), "r") as file:
                    config = yaml.safe_load(file)
                with open(os.path.join(category_path, "template.md"), "r") as file:
                    template = file.read()
                
                templates[category] = {
                    "config": config,
                    "template": template
                }
        return templates
                 
    def get_template(self, name):
        return self.templates.get(name)
