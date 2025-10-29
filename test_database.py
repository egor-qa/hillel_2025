import sys, os
import pytest
import allure

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.database import create_table, insert_user, get_users, update_user, delete_user

@allure.feature("Database CRUD Operations")
def test_database_crud_operations():
    create_table()
    insert_user("Taras", 7)
    insert_user("Yehor", 39)

    users = get_users()
    assert len(users) >= 2, f"Expected at least 2 users, got {len(users)}"

    user_id = users[0][0]
    update_user(user_id, "Taras Updated", 8)

    updated_users = get_users()
    updated_user = next((u for u in updated_users if u[0] == user_id), None)
    assert updated_user is not None, "Updated user not found"
    assert updated_user[1] == "Taras Updated"
    assert updated_user[2] == 8

    delete_user(user_id)
    users_after_delete = get_users()
    assert not any(user[0] == user_id for user in users_after_delete), "User was not deleted"
