import os
from crewai import LLM
from langchain_community.llms import Ollama
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from crewai_tools import SerperDevTool, WebsiteSearchTool, ScrapeWebsiteTool

llm = LLM(
    model="ollama/llama3:latest",
    base_url="http://localhost:11434"
)




@CrewBase
class Techpartner():
    """Techpartner crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

#=================================Agents======================================#

    @agent
    def tech_talent_diagnostics_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['tech_talent_diagnostics_agent'], # type: ignore[index]
            #tools = [SerperDevTool()],
            verbose=True,
            llm=llm,
        )

    @agent
    def education_content_curation_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['education_content_curation_agent'], # type: ignore[index]
            #tools = [WebsiteSearchTool(), SerperDevTool()],
            verbose=True,
            llm=llm,
        )
    
    @agent
    def talent_opportunity_connector_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['talent_opportunity_connector_agent'], # type: ignore[index]
            #tools = [WebsiteSearchTool(), SerperDevTool()],
            verbose=True,
            llm=llm,
        )
    
    @agent
    def ai_advisor_for_position_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['ai_advisor_for_position_agent'], # type: ignore[index]
            #tools = [WebsiteSearchTool(), SerperDevTool()],
            verbose=True,
            llm=llm,
        )
    
    @agent
    def ai_business_value_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['ai_business_value_agent'], # type: ignore[index]
            #tools = [WebsiteSearchTool(), SerperDevTool()],
            verbose=True,
            llm=llm,
        )
    
    @agent
    def final_report_generator_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['final_report_generator_agent'], # type: ignore[index]
            #tools = [WebsiteSearchTool(), SerperDevTool()],
            verbose=True,
            llm=llm,
        )
    

    

#=================================Tasks======================================#
    @task
    def identify_relevant_tech_positions(self) -> Task:
        """Encuentra posiciones en demanda"""
        return Task(
            config=self.tasks_config['identify_relevant_tech_positions'], # type: ignore[index]
        )

    @task
    def curate_learning_path(self) -> Task:
        """Genera ruta de aprendizaje"""
        return Task(
            config=self.tasks_config['curate_learning_path'], # type: ignore[index]
            
        )
    
    @task
    def connector_task(self) -> Task:
        """Busca vacantes y empresas"""
        return Task(
            config=self.tasks_config['connector_task'], # type: ignore[index]
            
        )
    
    @task
    def ai_advisor_task(self) -> Task:
        """Muestra casos de uso para esta posición"""
        return Task(
            config=self.tasks_config['ai_advisor_task'], # type: ignore[index]
            
        )
    
    @task
    def ai_impact_on_company_from_topic(self) -> Task:
        """Muestra el impacto de la adopción de la ia para esta posición"""
        return Task(
            config=self.tasks_config['ai_impact_on_company_from_topic'], # type: ignore[index]
            
        )
    
    @task
    def generate_final_tech_report(self) -> Task:
        """Genera un reporte final con todos los hallazgos"""
        return Task(
            config=self.tasks_config['generate_final_tech_report'], # type: ignore[index]
            

        )


    @crew
    def crew(self) -> Crew:
        """Crea el crew de nuestro proyecto"""

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            
        )
    

        
