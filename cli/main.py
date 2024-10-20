import cmd
from getpass import getpass

import requests

HTTP_STATUS_OK = 200
AUTH_URL = "http://localhost:8000/api/token/"
FAVLINKS_URL = "http://localhost:8000/api/favorite_urls/"
CATEGORIES_URL = "http://localhost:8000/api/categories/"
TAGS_URL = "http://localhost:8000/api/tags/"


class FavLinkCLI(cmd.Cmd):
    prompt = ">> "
    intro = 'Welcome to FavLinkCLI. Type "help" for available commands.'
    access_token = None
    refresh_token = None

    def check_auth(self):
        if not self.access_token:
            print("Please authenticate first.")
            self.do_auth(None)

    def do_auth(self, line):
        """Authentication with your username and password."""
        username = input("Username: ")
        password = getpass("Password: ")
        response = requests.post(
            AUTH_URL,
            json={
                "username": username,
                "password": password,
            },
            timeout=5,
        )

        if response.status_code == HTTP_STATUS_OK:
            tokens = response.json()
            self.access_token = tokens.get("access")
            self.refresh_token = tokens.get("refresh")
            print("Authentication successful.")
        else:
            print("Authentication failed. Please check your credentials.")

    def do_favlinks(self, line):
        """Get list of favorited links."""
        self.check_auth()

        headers = {
            "Authorization": f"Bearer {self.access_token}",
        }
        response = requests.get(
            FAVLINKS_URL,
            headers=headers,
            timeout=5,
        )
        print("Favorited links: ")
        print(response.json())

    def do_categories(self, line):
        """Get list of categories."""
        self.check_auth()

        headers = {
            "Authorization": f"Bearer {self.access_token}",
        }
        response = requests.get(
            CATEGORIES_URL,
            headers=headers,
            timeout=5,
        )
        print("Categories: ")
        print(response.json())

    def do_tags(self, line):
        """Get list of tags."""
        self.check_auth()

        headers = {
            "Authorization": f"Bearer {self.access_token}",
        }
        response = requests.get(
            TAGS_URL,
            headers=headers,
            timeout=5,
        )
        print("Tags: ")
        print(response.json())

    def do_q(self, line):
        """Exit the CLI."""
        return True


if __name__ == "__main__":
    FavLinkCLI().cmdloop()
