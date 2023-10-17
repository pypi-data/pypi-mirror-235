import requests

class Discord:
    def __init__(self, token) -> None:
        self.token = token

    def get_sessions(self):        
        xsp = 'ewogICJvcyI6ICJXaW5kb3dzIiwKICAiY2xpZW50X2J1aWxkX251bWJlciI6IDQyMDQyMAp9'

        headers = {
                'authorization': self.token,
                'X-Super-Properties': xsp
        }

        url = 'https://discord.com/api/v10/auth/sessions'

        get_sessions = requests.get(url, headers=headers).json()

        try:
            sessions = get_sessions['user_sessions']
            return sessions
        
        except KeyError:
            print("Improper Token has been passed.")
            return []
