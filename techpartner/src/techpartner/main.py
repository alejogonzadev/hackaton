#!/usr/bin/env python
import sys
import warnings
import os
from dotenv import load_dotenv



#Cargar las variables de entorno
load_dotenv()

serperdev_api = os.getenv("SERPERDEV_API")

#Importar las tools necesarias para los agentes
from crewai_tools import WebsiteSearchTool


websiteSearch =WebsiteSearchTool()

from datetime import datetime

from techpartner.crew import Techpartner

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'Full Stack Developer',
        'city': 'Medellin',
        'current_year': str(datetime.now().year)
    }
    
    try:
        Techpartner().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "Full Stack Developer",
        'city': 'Medellin',
        'current_year': str(datetime.now().year)
    }
    try:
        Techpartner().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Techpartner().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI Developer",
        'city': 'Medellin',
        "current_year": str(datetime.now().year)
    }
    
    try:
        Techpartner().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")


if __name__ == "__main__":
    run()  # Llama directamente a la ejecución principal
