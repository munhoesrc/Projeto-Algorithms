# from challenges.challenge_encrypt_message import encrypt_message
import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    # pass
    message = "SSOOLL"

    assert encrypt_message(message, -1) == "LLOOSS"  # esseOK
    assert encrypt_message(message, 1) == "S_LLOOS"
    assert encrypt_message(message, 2) == "LLOO_SS"
    assert encrypt_message(message, 3) == "OSS_LLO"  # esseOK
    assert encrypt_message(message, 4) == "LL_OOSS"  # esseOK

    with pytest.raises(TypeError):
        encrypt_message(message, "")
