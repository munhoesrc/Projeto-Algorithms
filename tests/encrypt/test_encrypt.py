from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    # pass
    message = "RENAN"

    assert encrypt_message(message, -1) == "NANER"
    assert encrypt_message(message, 3) == "NER_NA"
    assert encrypt_message(message, 4) == "N_ANER"

    with pytest.raises(TypeError):
        encrypt_message(message, "")
