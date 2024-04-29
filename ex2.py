class ChangeTeamName:
    def somar(self, user, newName):
        team = user.getTeam()
        team.setName(newName)
        return 0
