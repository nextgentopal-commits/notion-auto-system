import json
from agency.agents.orchestrator import Orchestrator

if __name__ == "__main__":
    goal = input("Auftrag: ").strip()
    result = Orchestrator().run(goal)
    print(json.dumps(result, ensure_ascii=False, indent=2, default=str))
