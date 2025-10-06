import pytest
import random

@pytest.mark.usefixtures("go_to_registration")
def test_user_registration(registration_page):

    email = f"test_user_{random.randint(1000,9999)}@mail.com"

    registration_page.first_name.clear()
    registration_page.first_name.send_keys("Yehor")

    registration_page.last_name.clear()
    registration_page.last_name.send_keys("Bulhakov")

    registration_page.email.clear()
    registration_page.email.send_keys(email)

    registration_page.password.clear()
    registration_page.password.send_keys("Qwerty123!")

    registration_page.repeat_password.clear()
    registration_page.repeat_password.send_keys("Qwerty123!")

    registration_page.register_button.click()

    success_text = registration_page.success_message.text
    assert "Registration complete" in success_text or "successfully" in success_text.lower()