from repeated_word import repeated_word
import pytest


@pytest.fixture
def small_string():
    string = "This is my string. Its pretty cool isnt it? The only thing is this should work."
    return string

@pytest.fixture
def large_string():
    string = "He didnt say any more but we've always been unusually communicative in a reserved way and I understood that he meant a great deal more than that. In consequence Im inclined to reserve all judgements, a habit that has opened up many curious natures to me and also made me the victim of not a few veteran bores. The abnormal mind is quick to detect and attach itself to this quality when it appears in a normal person, and so it came about that in college I was unjustly accused of being a politician, because I was privy to the secret griefs of wild, unknown men. Most of the confidences were unsought — frequently I have feigned sleep, preoccupation or a hostile levity when I realized by some unmistakable sign that an intimate revelation was quivering on the horizon — for the intimate revelations of young me nor at least the terms in which they express them are usually plagiaristic and marred by obvious suppressions. Reserving judgements is a matter of infinite hope. I am still a little afraid of missing something if I forget that, as my father snobbishly suggested and I snobbishly repeat, a sense of the fundamental decencies is parceled out unequally at birth."
    return string

def test_repeated_word():
    assert repeated_word

def test_repeated_word(small_string):
    actual = repeated_word(small_string)
    expected = "is"
    assert actual == expected

def test_repeated_word_big_string(large_string):
    actual = repeated_word(large_string)
    expected = "a"

def test_repeated_word_raise_error_typeerror():
    with pytest.raises(AttributeError):
        repeated_word(123041230)

def test_repeated_word_no_repeat():
    my_string = "This is my string"
    actual = repeated_word(my_string)
    expected = 'No Duplicate'
    assert actual == expected

def test_repeated_word_none_input():
    with pytest.raises(AttributeError):
        repeated_word(None)
