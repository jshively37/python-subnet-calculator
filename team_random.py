

import random


def main():
    team_list = [1, 1, 2, 3, 3, 4, 4]
    presentations = ['api', 'rest', 'sdk', 'development',
                     'mdp', 'docker', 'cicd']
    presentation_dict = {}

    for presentation in presentations:
        team = random.choice(team_list)
        team_list.pop(team_list.index(team))
        presentation_dict.update({presentation: team})

    for key, value in presentation_dict.items():
        print(f"Presentation {key} assigned to team {value}")


if __name__ == "__main__":
    main()
