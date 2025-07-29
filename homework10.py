"""
Ваша команда та ви розробляєте систему входу для веб-додатка,
і вам потрібно реалізувати тести на функцію для логування подій в системі входу.
Дано функцію, напишіть набір тестів для неї.
"""
import logging

def log_event(username: str, status: str):
    """
    Логує подію входу в систему.
    """

    log_message = f"Login event - Username: {username}, Status: {status}"

    # Видаляємо всі хендлери, щоб basicConfig працював
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    # Налаштування логування через root logger
    logging.basicConfig(
        filename='login_system.log',
        level=logging.DEBUG,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    # Логування напряму через logging
    if status == "success":
        logging.info(log_message)
    elif status == "expired":
        logging.warning(log_message)
    else:
        logging.error(log_message)
