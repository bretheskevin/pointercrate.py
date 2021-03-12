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
    <img src="images/logo.png" alt="Logo">
  </a>

  <h3 align="center">Pointercrate Python  API</h3>

  <p align="center">
    pointercrate.py is a library that provides its users ability to interact with the api of <a href="https://pointercrate.com/">Pointercrate</a>.
    <br />
    <a href="#documentation"><strong>Explore the docs »</strong></a>
    <br />
    <a href="https://github.com/bretheskevin/pointercrate.py/issues">Report Bug</a>
    ·
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
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li>
         <a href="#documentation">Documentation</a>
         <ul>
            <li><a href="#demons">Demons</a></li>
            <li>
            <a href="#examples">Examples</a>
             <ul>
                <li><a href="#limit">limit</a></li>
                <li>
                <a href="#name">name</a>
                </li>
             </ul>
            </li>
         </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About the project
### Built With

* [Python 3.9](https://www.python.org/)

<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites


* requests

#### Windows

```
py -3 -m pip install requests==2.25.1
``` 

  
#### Linux
```shell
python3 -m pip install requests==2.25.1
```

### Installation

1. Clone the repository
   ```sh
   git clone https://github.com/bretheskevin/pointercrate.py.git
   ```

2. Put the pointercrate.py file in your project (you can rename it)

<!-- USAGE EXAMPLES -->
## Usage

```python
from pointercrate import Client  # replace "pointercrate" by the corresponding name if you renamed it
client = Client()
```

## Documentation

### Demons

pointercrate.py allows you searching and interacting with the demons of pointercrate !
You can also get information about the demons that are not in the list anymore.

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


**Returns:** All demons' information.

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
      "requirement": 50, "video": "https://www.youtube.com/watch?v=Aas8_QKLnuc", 
      "publisher": 
         {
            "id": 35150, 
            "name": "BoBoBoBoBoBoBo", 
            "banned": false
         }, 
      "verifier": 
         {
            "id": 5240, 
            "name": "nSwish", 
            "banned": false
         }, 
      "level_id": 60978746}
]
```

&nbsp;

`id` 

__Type:__ <span style="font-weight: bold; color: #813832">int</span>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The ID of the object in the database.

&nbsp;

`position` 

__Type:__ <span style="font-weight: bold; color: #813832">int</span>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The position of the demon in the list.

&nbsp;

`name` 

__Type:__ <span style="font-weight: bold; color: #813832">str</span>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The name of the demon.

&nbsp;

`requirement` 

__Type:__ <span style="font-weight: bold; color: #813832">int</span>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The requirement % to get your record accepted.

&nbsp;

`video` 

__Type:__ <span style="font-weight: bold; color: #813832">str</span>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Link of the video of the level.

&nbsp;

*Object* `publisher: contains information about the player who uploaded the level` 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`id`


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;__Type:__ <span style="font-weight: bold; color: #813832">int</span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Player's ID.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`name`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;__Type:__ <span style="font-weight: bold; color: #813832">str</span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Player's name.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`banned`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;__Type:__ <span style="font-weight: bold; color: #813832">bool</span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;If the player is banned from pointercrate or not.

&nbsp;

*Object* `verifier: contains information about the player who verified the level`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`id`


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;__Type:__ <span style="font-weight: bold; color: #813832">int</span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Player's ID.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`name`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;__Type:__ <span style="font-weight: bold; color: #813832">str</span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Player's name.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`banned`

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;__Type:__ <span style="font-weight: bold; color: #813832">bool</span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;If the verifier is banned from pointercrate or not.

&nbsp;

`level_id` 

__Type:__ <span style="font-weight: bold; color: #813832">int</span>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The ID of the demon.

### Examples

#### <li>limit</li> 

```python
from pointercrate import Client
client = Client()

demons = client.get_demons(limit=3) # [{....}, {....}, {....}]
# List of 3 objects containing the top 3


# demonlist from march 2021 
print(demons[0].get("name"))    # Tartarus
print(demons[1].get("name"))    # The Golden
print(demons[2].get("name"))    # Zodiac
```

&nbsp;


#### <li>name - CASE SENSITIVE</li>
```python
from pointercrate import Client
client = Client()

demons = client.get_demons(name="Tartarus") # [{....}]
# List with one object containing information about the demon named Tartarus

demons = client.get_demons(name="tartarus") # [] Empty list 
```

&nbsp;

#### <li>name_contains - NOT CASE SENSITIVE</li> 

```python
from pointercrate import Client
client = Client()

demons = client.get_demons(name_contains="blade") # [{Edge of the Blade's info}, {Blade of Justice's info}....]
# List of levels containing "edge" in their name

demons = client.get_demons(name_contains="tartarus") # [{ "Tartarus's info "}]
# As you can see, it's not case sensitive so it can be a good alternative to "name"
```

&nbsp;

#### <li>after | before</li> 

```python
from pointercrate import Client
client = Client()

demons = client.get_demons(after=5, before=9) # [{...}, {...}]
# Demons which are at position 6, 7 and 8

demons = client.get_demons(limit=100) # [{...}, {...}, ...] List of top 100 demons
demons = client.get_demons(limit=100, after=100) # [{...}, {...}, ...] Demons between top 101 and 200
```

&nbsp;

#### <li>verifier_id</li> 

```python
# Kugelblitz's id is 598
from pointercrate import Client
client = Client()

demons = client.get_demons(verifier_id=598) # [{SARY NEVER CLEAR's info}] 
# List of levels that Kugelblitz has verified
```

&nbsp;

#### <li>publisher_id</li> 

```python
# Dolphy's id is 34134
from pointercrate import Client
client = Client()

demons = client.get_demons(publisher_id=34134) # [{Tartarus's info}] 
# List of levels that Dolphy has uploaded
```

&nbsp;

#### <li>publisher_name - CASE SENSITIVE</li> 

```python
from pointercrate import Client
client = Client()

demons = client.get_demons(publisher_name="ViPriN") # [{...}, {...}, ...] Contains all levels uploaded by "ViPriN"
demons = client.get_demons(publisher_name="viprin") # [{}] No results because it's case sensitive
```

&nbsp;

#### <li>listed</li> 

```python
from pointercrate import Client
client = Client()

demons = client.get_demons(listed=True) # default value, give the demons ordered by position
demons = client.get_demons(listed=False) # give the demons disorderly
```


<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/bretheskevin/pointercrate.py/issues) for a list of proposed features (and known issues).


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learned, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Hikudo - [@bretheskevin](https://twitter.com/bretheskevin) - bretheskevin@gmail.com

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
[license-url]: https://github.com/bretheskevin/pointercrate.py/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/k%C3%A9vin-br%C3%A8thes-08a6951b6/
