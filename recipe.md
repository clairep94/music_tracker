
## 1. Describe the Problem

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class MusicTracker:
    def __init__(self):
        self.tracks = {}
    
    def add(self,artist,song):
        pass

    def all(self):
        pass

```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
given a track
return track added
"""


"""
given multiple tracks
return all tracks added
"""


"""
if the artist of track given is in dict
add track song
"""


"""
if artist or song is not string
raise error message
"""
"Type input not valid"

"""
if artists and song already in dict
raise error message 
"""

"Track already added"

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

