class Agent:
    def __init__(self, codename, score):
        self.codename = codename
        self.score = score

agents = []
for _ in range(5):
    codename, score = input().split()
    score = int(score)
    agents.append(Agent(codename, score))

lowest_agent = min(agents, key=lambda agent: agent.score)

print(f"{lowest_agent.codename} {lowest_agent.score}")