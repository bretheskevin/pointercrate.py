import requests

class Client:
    """
    Main class in demonlist.py, used for interacting with the pointercrate REST API.
    """

    @staticmethod
    def get_demon(limit=50, name="", name_contains="", after=0, before=0, verifier_id=0, publisher_id=0, publisher_name="", listed=True):
        api_v2 = "https://pointercrate.com/api/v2/"
        """
        :param
        - limit: The maximum amount of object to return. Must lie between 1 and 100. Default is 50.
        - name: Filter with the name of the demon [!!!] Case sensitive [!!!]
        - name_contains: Check if a demon has a word in his name, not case sensitive 
        so it's a good alternative to name filter.
        
        - after: Used for pagination, here is an example:
                    limit = 100: You will get the top 100 levels of the list (listed is True by default)
                    limit = 100 AND after = 100: You will get the levels from position 101 to 200 because
                it will skip the 100 first ones.        
        - before: Also used for pagination, here is an example:
                    limit = 100 AND before = 6 : You will get the 5 first levels
        You can use before and after to easily filter by the position:
            after=9 and before=25: 10th to 24th levels            
        
        - verifier_id: Filter with the verifier's id
        - publisher_id: Filter with the publisher's id
        - publisher_name: Filter with the name of the player who uploaded the level
        - listed: Sort the levels by position. Default is True

        :return:
        - List of objects if there no position provided
        - An object containing the demon's information (The demon is at the provided position)

        """

        # Handling errors
        if limit < 1 or limit > 100:
            print("""
            ==========================================
            | ERROR:|                                |
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
        if name != "":
            params += f"&name={name}"

        # demon containing a specific string in his name
        if name_contains != "":
            params += f"&name_contains={name_contains.replace(' ', '+')}"

        #after
        if after != 0:
            params += f"&after={after}"

        #before
        if before != 0:
            params += f"&before={before}"

        # verifier id
        if verifier_id != 0:
            params += f"&verifier_id={verifier_id}"

        # publisher id
        if publisher_id != 0:
            params += f"&publisher_id={publisher_id}"

        # publisher name
        if publisher_name != "":
            params += f"&publisher_name={publisher_name}"

        # request the json
        response = requests.get(api_v2 + "demons/" + params).json()

        if not response:
            print("No results! Check the filters that you used.")

        return response
