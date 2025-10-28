import sys, os
import pytest
import allure

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.database import create_table, insert_user, get_users, update_user, delete_user


@allure.feature("Database CRUD Operations")
def test_database_crud_operations():
    with allure.step("Create users table if not exists"):
        create_table()

    with allure.step("Insert two users into the table"):
        insert_user("Taras", 7)
        insert_user("Yehor", 39)

    with allure.step("Check that at least two users exist"):
        users = get_users()
        assert len(users) >= 2, f"Expected at least 2 users, got {len(users)}"

    with allure.step("Update the first user in the list"):
        user_id = users[0][0]
        update_user(user_id, "Taras Updated", 8)

    with allure.step("Verify that user data was updated"):
        updated_users = get_users()
        updated_user = next((u for u in updated_users if u[0] == user_id), None)
        assert updated_user is not None, "Updated user not found"
        assert updated_user[1] == "Taras Updated"
        assert updated_user[2] == 8

    with allure.step("Delete updated user and verify deletion"):
        delete_user(user_id)
        users_after_delete = get_users()
        assert not any(user[0] == user_id for user in users_after_delete), "User was not deleted"