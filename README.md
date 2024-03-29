<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/bretheskevin/pointercrate.py">
    <img src="https://i.imgur.com/Voi701d.png" alt="Logo">
  </a>

<h3 align="center">Pointercrate Python API</h3>

  <p align="center">
    pointercratepy is a library that provides its users ability to interact with the api of <a href="https://pointercrate.com/">Pointercrate</a>.
    <br />
    <a href="#documentation"><strong>Explore the docs</strong></a>
    <br />
    <a href="https://github.com/bretheskevin/pointercrate.py/issues">Report Bug</a>
    |
    <a href="https://github.com/bretheskevin/pointercrate.py/issues">Request Feature</a>
 </p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li>
         <a href="#documentation">Documentation</a>
         <ul>
            <li><a href="#demons">Demons</a></li>
            <li><a href="#players">Players</a></li>
            <a href="#examples">Examples</a>
            <ul>
               <li><a href="#limit">limit</a></li>
               <li><a href="#name---case-sensitive">name</a></li>
               <li><a href="#name_contains---not-case-sensitive">name_contains</a></li>
               <li><a href="#after--before">after | before</a></li>
               <li><a href="#verifier_id">verifier_id</a></li>
               <li><a href="#publisher_id">publisher_id</a></li>
               <li><a href="#publisher_name---case-sensitive">publisher_name</a></li>
               <li><a href="#listed">listed</a></li>
               <li><a href="#nation">nation</a></li>
            </ul>
         </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#credits">Credits</a></li>
    <li><a href="#changelog">Changelog</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## <span id="about-the-project">About the project</span>

### <span id="built-with">Built With</span>

* [Python 3.9](https://www.python.org/)

<!-- GETTING STARTED -->

## <span id="getting-started">Getting Started</span>

### <span id="installation">Installation</span>

#### Windows

```
python -m pip install pointercratepy
``` 

#### Linux

```shell
python3 -m pip install pointercratepy
```

<!-- USAGE EXAMPLES -->

## <span id="usage">Usage</span>

```python
from pointercratepy import Client

client = Client()
```

## <span id="documentation">Documentation</span>

pointercratepy allows you searching and interacting with the demons of pointercrate !
You can also get information about the demons that are not in the list anymore.

### <span id="demons">Demons</span>

### <span style="color: grey">*function*</span> get_demons(<span style="color: grey">*\*\*options*</span>)

**Parameters:**
<ul>
    <li><span style="font-weight: bold;">limit</span> (Optional <span style="font-weight: bold;">[int]</span>) - The maximum amount of object to return. Must lie between 1 and 100 | Default is <span style="font-weight: bold; color: #813832;">50</span></li>
    <li><span style="font-weight: bold;">name</span> (Optional <span style="font-weight: bold;">[str]</span>) - Filter with the name of the demon [!!!] Case sensitive [!!!]</li>
    <li><span style="font-weight: bold;">name_contains</span> (Optional <span style="font-weight: bold;">[str]</span>) - Check if a demon has the specified string in his name, not case sensitive 
        so it's a good alternative to name filter.</li>
    <li><span style="font-weight: bold;">after</span> (Optional <span style="font-weight: bold;">[int]</span>) - Used for pagination, example below.</li>
    <li><span style="font-weight: bold;">before</span> (Optional <span style="font-weight: bold;">[int]</span>) - Used for pagination, example below.</li>
    <li><span style="font-weight: bold;">verifier_id</span> (Optional <span style="font-weight: bold;">[int]</span>) - Filter with the verifier's id.</li>
    <li><span style="font-weight: bold;">publisher_id</span> (Optional <span style="font-weight: bold;">[int]</span>) - Filter with the publisher's id.</li> 
    <li><span style="font-weight: bold;">publisher_name</span> (Optional <span style="font-weight: bold;">[str]</span>) - Filter with the name of the player who uploaded the level.  [!!!] Case sensitive [!!!]</li>
    <li><span style="font-weight: bold;">listed</span> (Optional <span style="font-weight: bold;">[bool]</span>) - Sort the levels by their position in the list. | Default is <span style="font-weight: bold; color: #813832">True</span> </li>
</ul> 


**Returns:** All demons information.

**Return type:** List of objects

```json
[
  {
    "id": 250,
    "position": 1,
    "name": "Tartarus",
    "requirement": 47,
    "video": "https://www.youtube.com/watch?v=9YYQBbrsV5Y",
    "publisher": {
      "id": 34134,
      "name": "Dolphy",
      "banned": false
    },
    "verifier": {
      "id": 34134,
      "name": "Dolphy",
      "banned": false
    },
    "level_id": 59075347
  },
  {
    "id": 274,
    "position": 2,
    "name": "The Golden",
    "requirement": 50,
    "video": "https://www.youtube.com/watch?v=Aas8_QKLnuc",
    "publisher": {
      "id": 35150,
      "name": "BoBoBoBoBoBoBo",
      "banned": false
    },
    "verifier": {
      "id": 5240,
      "name": "nSwish",
      "banned": false
    },
    "level_id": 60978746
  }
]
```

&nbsp;

`id`

__Type:__ <span style="font-weight: bold; color: #813832">int</span>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The ID of the object in the
database.

&nbsp;

`position`

__Type:__ <span style="font-weight: bold; color: #813832">int</span>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The position of the demon in the
list.

&nbsp;

`name`

__Type:__ <span style="font-weight: bold; color: #813832">str</span>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The name of the demon.

&nbsp;

`requirement`

__Type:__ <span style="font-weight: bold; color: #813832">int</span>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The requirement % to get your record
accepted.

&nbsp;

`video`

__Type:__ <span style="font-weight: bold; color: #813832">str</span>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Link of the video of the level.

&nbsp;

*Object* `publisher: contains information about the player who uploaded the level`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`id`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
__Type:__ <span style="font-weight: bold; color: #813832">int</span>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Player's ID.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`name`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
__Type:__ <span style="font-weight: bold; color: #813832">str</span>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Player's name.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`banned`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
__Type:__ <span style="font-weight: bold; color: #813832">bool</span>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;If the player is banned from pointercrate or not.

&nbsp;

*Object* `verifier: contains information about the player who verified the level`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`id`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
__Type:__ <span style="font-weight: bold; color: #813832">int</span>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Player's ID.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`name`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
__Type:__ <span style="font-weight: bold; color: #813832">str</span>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Player's name.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`banned`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
__Type:__ <span style="font-weight: bold; color: #813832">bool</span>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;If the verifier is banned from pointercrate or not.

&nbsp;

`level_id`

__Type:__ <span style="font-weight: bold; color: #813832">int</span>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The ID of the demon.

### <span id="players">Players</span>

### <span style="color: grey">*function*</span> get_players_ranked(<span style="color: grey">*\*\*options*</span>)

**Parameters:**
<ul>
    <li><span style="font-weight: bold;">limit</span> (Optional <span style="font-weight: bold;">[int]</span>) - The maximum amount of object to return. Must lie between 1 and 100 | Default is <span style="font-weight: bold; color: #813832;">50</span></li>
    <li><span style="font-weight: bold;">name</span> (Optional <span style="font-weight: bold;">[str]</span>) - Filter with the name of the player [!!!] Case sensitive [!!!]</li>
    <li><span style="font-weight: bold;">name_contains</span> (Optional <span style="font-weight: bold;">[str]</span>) - Check if a player has the specified string in his name, not case sensitive 
        so it's a good alternative to name filter.</li>
    <li><span style="font-weight: bold;">nation</span> (Optional <span style="font-weight: bold;">[str]</span>) - Filter with the nation of the player.</li>
    <li><span style="font-weight: bold;">after</span> (Optional <span style="font-weight: bold;">[int]</span>) - Used for pagination, example below.</li>
    <li><span style="font-weight: bold;">before</span> (Optional <span style="font-weight: bold;">[int]</span>) - Used for pagination, example below.</li>
</ul> 


**Returns:** All player's information.

**Return type:** List of objects

```json
[
  {
    "id": 34124,
    "name": "Wolvez",
    "rank": 1,
    "score": 4466.7859672865025,
    "nationality": {
      "country_code": "SE",
      "nation": "Sweden",
      "subdivision": null
    }
  }
]
```

&nbsp;

`id`

__Type:__ <span style="font-weight: bold; color: #813832">int</span>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The ID of the player.

&nbsp;

`rank`

__Type:__ <span style="font-weight: bold; color: #813832">int</span>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The position of the player in the
list.

&nbsp;

`score`

__Type:__ <span style="font-weight: bold; color: #813832">float</span>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The number of list points that the
player has.

&nbsp;

*Object* `nationality: contains information about the location of the player`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`country_code`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
__Type:__ <span style="font-weight: bold; color: #813832">str</span>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ISO country code.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`nation`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
__Type:__ <span style="font-weight: bold; color: #813832">str</span>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Nation's name.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`subdivision`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
__Type:__ <span style="font-weight: bold; color: #813832">str</span>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Subdivision of the nation.

&nbsp;


### <span id="examples">Examples</span>

#### <li id="limit">limit</li>

```python
from pointercratepy import Client

client = Client()

demons = client.get_demons(limit=3)  # [{....}, {....}, {....}]
# List of 3 objects containing the top 3


# demonlist from march 2021 
print(demons[0].get("name"))  # Tartarus
print(demons[1].get("name"))  # The Golden
print(demons[2].get("name"))  # Zodiac
```

&nbsp;

#### <li id="name---case-sensitive">name - CASE SENSITIVE</li>

```python
from pointercratepy import Client

client = Client()

demons = client.get_demons(name="Tartarus")  # [{....}]
# List with one object containing information about the demon named Tartarus

demons = client.get_demons(name="tartarus")  # [] Empty list 
```

&nbsp;

#### <li id="name_contains---not-case-sensitive">name_contains - NOT CASE SENSITIVE</li>

```python
from pointercratepy import Client

client = Client()

demons = client.get_demons(name_contains="blade")  # [{Edge of the Blade's info}, {Blade of Justice's info}....]
# List of levels containing "edge" in their name

demons = client.get_demons(name_contains="tartarus")  # [{ "Tartarus's info "}]
# As you can see, it's not case sensitive so it can be a good alternative to "name"
```

&nbsp;

#### <li id="after--before">after | before</li>

```python
from pointercratepy import Client

client = Client()

demons = client.get_demons(after=5, before=9)  # [{...}, {...}]
# Demons which are at position 6, 7 and 8

demons = client.get_demons(limit=100)  # [{...}, {...}, ...] List of top 100 demons
demons = client.get_demons(limit=100, after=100)  # [{...}, {...}, ...] Demons between top 101 and 200
```

&nbsp;

#### <li id="verifier_id">verifier_id</li>

```python
# Kugelblitz's id is 598
from pointercratepy import Client

client = Client()

demons = client.get_demons(verifier_id=598)  # [{SARY NEVER CLEAR's info}] 
# List of levels that Kugelblitz has verified
```

&nbsp;

#### <li id="publisher_id">publisher_id</li>

```python
# Dolphy's id is 34134
from pointercratepy import Client

client = Client()

demons = client.get_demons(publisher_id=34134)  # [{Tartarus's info}] 
# List of levels that Dolphy has uploaded
```

&nbsp;

#### <li id="publisher_name---case-sensitive">publisher_name - CASE SENSITIVE</li>

```python
from pointercratepy import Client

client = Client()

demons = client.get_demons(publisher_name="ViPriN")  # [{...}, {...}, ...] Contains all levels uploaded by "ViPriN"
demons = client.get_demons(publisher_name="viprin")  # [{}] No results because it's case sensitive
```

&nbsp;

#### <li id="listed">listed</li>

```python
from pointercratepy import Client

client = Client()

demons = client.get_demons(listed=True)  # default value, give the demons ordered by position
demons = client.get_demons(listed=False)  # give the demons disorderly
```

&nbsp;


#### <li id="nation">nation</li>

```python
from pointercratepy import Client

client = Client()

players = client.get_players_ranked(limit=2, nation="FR")  # [{....}, {....}]
players = client.get_players_ranked(limit=2, nation="France")  # [{....}, {....}]
# This will give the same results since you can filter both by country code and country name
# List of 2 objects containing the top 2 french players

# demonlist from june 2022
print(players[0].get("name"))  # GDonut
print(players[1].get("name"))  # Boodbdog
```


<!-- ROADMAP -->

## <span id="roadmap">Roadmap</span>

See the [open issues](https://github.com/bretheskevin/pointercrate.py/issues) for a list of proposed features (and known
issues).


<!-- CONTRIBUTING -->

## <span id="contributing">Contributing</span>

Contributions are what make the open source community such an amazing place to be learned, inspire, and create. Any
contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->

## <span id="license">License</span>

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->

## <span id="contact">Contact</span>

Hikudo - [@bretheskevin](https://twitter.com/bretheskevin) - bretheskevin@gmail.com

Discord - Hikudo#1714

<!-- CREDITS -->

## <span id="credits">Credits</span>

<li>
Thanks to <a href="https://github.com/nekitdev">nekitdev</a>, this is my first API wrapper and his work on <a href="https://gdpy.readthedocs.io/en/latest/index.html">gd.py</a> helped me to write de documentation and find a description for the project.
</li>
<li>Thanks to Nimbus who answered my questions about the REST API of pointercrate.</li>


<!-- CHANGELOG -->

## <span id="changelog">Changelog [day/month/year]</span>

0.0.1 < 1.0.0 (13/03/2021)
------------------
<li>Setting up pip</li>
<li>First release</li>
<li>Method get_demons() : Get information about the demons of pointercrate.</li>

1.0.1 & 1.0.2 (13/03/2021)
------------------
<li>Documentation correction</li>

1.1.0 (06/30/2022)
------------------
<li>Method get_players_ranked() : Get information about the ranked players of pointercrate.</li>
<li>Simplified the code and changed some grammar</li>

&nbsp;

Project Link: [https://github.com/bretheskevin/pointercrate.py](https://github.com/bretheskevin/pointercrate.py)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/bretheskevin/pointercrate.py.svg?style=for-the-badge

[contributors-url]: https://github.com/bretheskevin/pointercrate.py/graphs/contributors

[forks-shield]: https://img.shields.io/github/forks/bretheskevin/pointercrate.py.svg?style=for-the-badge

[forks-url]: https://github.com/bretheskevin/pointercrate.py/network/members

[stars-shield]: https://img.shields.io/github/stars/bretheskevin/pointercrate.py.svg?style=for-the-badge

[stars-url]: https://github.com/bretheskevin/pointercrate.py/stargazers

[issues-shield]: https://img.shields.io/github/issues/bretheskevin/pointercrate.py/pointercrate.py.svg?style=for-the-badge

[issues-url]: https://github.com/bretheskevin/pointercrate.py/issues

[license-shield]: https://img.shields.io/github/license/bretheskevin/pointercrate.py.svg?style=for-the-badge

[license-url]: https://github.com/bretheskevin/pointercrate.py/blob/master/LICENSE
<!-- @IGNORE PREVIOUS: link -->

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555

[linkedin-url]: https://www.linkedin.com/in/bretheskevin
