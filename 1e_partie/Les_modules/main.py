from pathlib import Path

p = Path.cwd().parent /"Le_logging"
p.mkdir(exist_ok=True)
# p.touch(exist_ok=True)
print(p)

