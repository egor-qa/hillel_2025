import pytest

correct_secrets = {
    "frame1": "Frame1_Secret",
    "frame2": "Frame2_Secret"
}

wrong_secrets = {
    "frame1": "wrongtext",
    "frame2": "123456"
}


@pytest.mark.parametrize("verify_secret_text", [(frame, secret) for frame, secret in correct_secrets.items()],
                         indirect=True)
def test_correct_secrets(verify_secret_text):
    alert_message = verify_secret_text
    assert alert_message == "Verification was successful!"


@pytest.mark.parametrize("verify_secret_text", [(frame, secret) for frame, secret in wrong_secrets.items()],
                         indirect=True)
def test_incorrect_secrets(verify_secret_text):
    alert_message = verify_secret_text
    assert alert_message == "Invalid text entered!"