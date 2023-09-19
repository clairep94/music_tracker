from lib.music_tracker import MusicTracker
import pytest

def test_add_track():
    tracker = MusicTracker()
    tracker.add("Adele", "Hello")
    assert tracker.all() == {"Adele": ["Hello"]}


def test_add_multiple_tracks():
    tracker = MusicTracker()
    tracker.add("Adele", "hello")
    tracker.add("The beatles", "Yellow submarine")
    tracker.add("John", "My Song")
    assert tracker.all() == {"Adele": ["Hello"], "The Beatles": ["Yellow Submarine"], "John": ["My Song"]}



def test_add_song_to_existing_artists():
    tracker = MusicTracker()
    tracker.add("Adele", "hello")
    tracker.add("Adele", "goodbye")
    assert tracker.all() == {"Adele": ["Hello", "Goodbye"]}

def test_add_track_already_in_dict():
    tracker = MusicTracker()
    tracker.add("Adele", "hello")
    with pytest.raises(Exception) as e:
        tracker.add("Adele", "hello")
    error = str(e.value)
    assert error == "Track already added"
    