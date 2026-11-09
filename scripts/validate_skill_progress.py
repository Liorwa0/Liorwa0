import json
from pathlib import Path

data = json.loads(Path("data/skill-progress.json").read_text(encoding="utf-8"))
allowed = {"learning", "practiced", "mastered"}
skills = [skill for group in data["categories"] for skill in group["skills"]]
for skill in skills:
    if skill["status"] not in allowed:
        raise SystemExit(f"Invalid status for {skill['name']}: {skill['status']}")
names = [skill["name"].lower() for skill in skills]
if len(names) != len(set(names)):
    raise SystemExit("Duplicate skill names found.")
print(f"Validated {len(skills)} skills across {len(data['categories'])} constellations.")
print(f"Projects recorded: {len(data.get('projects', []))}")
print("Skill progress data is ready. Update this JSON as skills are practiced or mastered.")
