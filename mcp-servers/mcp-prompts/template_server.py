import os
import logging
import yaml

class TemplatesServer():
    def __init__(self):
        self.templates = self._load_templates()

    def _load_templates(self):
        templates = {}
        templates_path = os.path.join(os.path.dirname(__file__), "templates")
        for category in os.listdir(templates_path):
            category_path = os.path.join(templates_path, category)
            logging.info(category_path)
            # config.yaml and prompts.md must be present in the directory
            if "config.yaml" in os.listdir(category_path) and \
               "prompts.md" in os.listdir(category_path):
                # Load config
                with open(os.path.join(category_path, "config.yaml"), "r") as file:
                    config = yaml.safe_load(file)
                with open(os.path.join(category_path, "prompts.md"), "r") as file:
                    prompt_text = file.read()
                
                templates[category] = {
                    "config": config,
                    "prompt_text": prompt_text
                }
        return templates
                 
    def get_template(self, name):
        return self.templates.get(name)
