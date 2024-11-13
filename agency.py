from agency_swarm import Agency, Agent
from utils import load_config
from tools.manager_tools import ManagerAgentTool
from tools.pen_test_planning_tools import PenetrationTestingPlanTool
from tools.text_analysis_tools import TextInsightTool
from tools.visualization_tools import ChartGenerationTool, GraphGenerationTool
from datetime import datetime, timezone
from prompts import (
    manager_description, 
    manager_instructions,
    pentestplanner_description,
    pentestplanner_instructions,
    textanalyzer_description,
    textanalyzer_instructions,
    chartgenerator_description,
    chartgenerator_instructions,
    mission_statement_prompt
)

# loads API keys from config.yaml
load_config(file_path="./config.yaml")

def get_current_utc_datetime():
    now_utc = datetime.now(timezone.utc)
    current_time_utc = now_utc.strftime("%Y-%m-%d %H:%M:%S %Z")
    return current_time_utc

manager_instructions_with_datetime = manager_instructions.format(datetime=get_current_utc_datetime())


# manager agent
manager = Agent(
            name="Manager",
            description=manager_description, 
            instructions=manager_instructions_with_datetime, 
            #tools=[ManagerAgentTool], 
            model="gpt-4o"
        )

            
# expert agents 
pen_test_plnner = Agent(
            name="PenTestPlanner",
            description=pentestplanner_description, 
            instructions=pentestplanner_instructions,
            tools=[PenetrationTestingPlanTool],
            model="gpt-4o"
        )

text_analyzer = Agent(
            name="TextAnalyzer",
            description=textanalyzer_description, 
            instructions=textanalyzer_instructions,
            tools=[TextInsightTool],
            model="gpt-4o"
        )

chart_generator = Agent(
            name="ChartGenerator",
            description=chartgenerator_description, 
            instructions=chartgenerator_instructions,
            tools=[ChartGenerationTool],
            model="gpt-4o"
        )


agency = Agency([
        manager,
        [manager, pen_test_plnner],
        [manager, text_analyzer],
        [manager, chart_generator],
     ], 
     shared_instructions=mission_statement_prompt,
     temperature=0,
)

if __name__ == "__main__":
    agency.run_demo()