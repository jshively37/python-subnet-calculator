

import random


def main():
    team_list = [1, 1, 2, 3, 3, 4, 4]
    presentations = ['api', 'rest', 'sdk', 'development', 'mdp', 'docker', 'cicd']

    for presentation in presentations:
        team = random.choice(team_list)
        print(f"Presentation {presentation} assigned to team {team}")
        team_list.pop(team_list.index(team))


if __name__ == "__main__":
    main()
