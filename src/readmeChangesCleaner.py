import os
from pathlib import Path

if __name__ == "__main__":
  readme_path = Path(__file__).parent.parent.joinpath("README.md")
  with open(readme_path, "r") as file:
    lines: list[str] = file.readlines()
    for i in range(len(lines)):
      if lines[i].find("## API Endpoint Changes") != -1:
        break
    
    lines = lines[:i + 1]

  with open(readme_path, "w") as file:
    file.writelines(lines)
