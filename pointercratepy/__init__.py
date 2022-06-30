import requests

api_v2 = "https://pointercrate.com/api/v2/"

class Client:
    """
    Main class in demonlist.py, used for interacting with the pointercrate REST API.
    """

    @staticmethod
    def get_demons(limit=50, name=None, name_contains=None, after=None, before=None, verifier_id=None, publisher_id=None,
                   publisher_name=None, listed=True):
        """

        Args:
            limit: The maximum amount of object to return. Must lie between 1 and 100. Default is 50.
            name: Filter with the name of the demon [!!!] Case sensitive [!!!]
            name_contains: Check if a demon has the specified string in its name, not case sensitive so it's a good alternative to name filter.
            after: Used for pagination, here is an example:
                    limit = 100: You will get the top 100 levels of the list (listed is True by default)
                    limit = 100 AND after = 100: You will get the levels from position 101 to 200 because it will skip the first 100.
            before: Also used for pagination, here is an example:
                        - limit = 100 AND before = 6: You will get the 5 first levels
                    You can use before and after to easily filter by the position:
                        - after=9 and before=25: 10th to 24th levels
            verifier_id: Filter with the verifier's id
            publisher_id: Filter with the publisher's id
            publisher_name: Filter with the name of the player who uploaded the level
            listed: Sort the levels by position. Default is True

        Returns:
            list: List of objects containing information about all list demons.
        """

        # Handling errors
        if limit < 1 or limit > 100:
            print("""
            ==========================================
            | ERROR:                                 |
            | The limit has to be between 1 and 100! |
            ==========================================
            """)
            return

        # set the queries
        params = ""

        # listed by position
        if listed:
            params += "listed/"
        params += f"?limit={limit}"

        # name of the demon
        if name:
            params += f"&name={name}"

        # demon containing a specific string in his name
        if name_contains:
            params += f"&name_contains={name_contains.replace(' ', '+')}"

        # after
        if after:
            params += f"&after={after}"

        # before
        if before:
            params += f"&before={before}"

        # verifier id
        if verifier_id:
            params += f"&verifier_id={verifier_id}"

        # publisher id
        if publisher_id:
            params += f"&publisher_id={publisher_id}"

        # publisher name
        if publisher_name:
            params += f"&publisher_name={publisher_name}"

        # request the json
        response = requests.get(api_v2 + "demons/" + params).json()

        if not response:
            print("No results! Check the filters that you used.")

        return response

    @staticmethod
    def get_players_ranked(limit=50, name_contains=None, name=None, after=None, before=None, nation=None, continent=None):
        """

        Args:
            limit: The maximum amount of object to return. Must lie between 1 and 100. Default is 50.
            name: Filter with the name of the player (case sensitive)
            name_contains: Check if the player has a certain string in their name (not case sensitive, use name for specific player!)
            after: Used for pagination, here is an example:
                    limit = 100: You will get the top 100 players on the stats viewer
                    limit = 100 AND after = 100: You will get the players from rank 101 to 200 since the first 100 will be skipped.
            before: Also used for pagination, here is an example:
                        - limit = 100 AND before = 6 : You will get the top 5 demonlist players
                    You can use before and after to easily find players using position:
                        - after=9 and before=25: 10th to 24th ranked players
            nation: The country of the player to search with.
            continent: The continent of the player to search with.

        Returns:
            list: List of objects containing information about players, ordered according to their rank.
        """
        # set the queries
        params = ""
        
        # Handling errors
        if limit < 1 or limit > 100:
            print("""
            ==========================================
            | ERROR:|                                |
            | The limit has to be between 1 and 100! |
            ==========================================
            """)
            return
        else:
            params += f"?limit=50"
        
        if after:
            params += f"&after={after}"
            
        if before:
            params += f"&before={before}"
        
        if name_contains:
            params += f"&name_contains={name_contains.replace(' ', '+')}"
        
        if name:
            params += f"&name={name_contains.replace(' ', '+')}"
        if nation:
            params += f"&nation={nation}"
        
        if continent:
            params += f"&continent={continent}"
        
        # request the json
        response = requests.get(api_v2 + "players/ranking/" + params).json()

        if not response:
            print("No results! Check the filters that you used.")

        return response