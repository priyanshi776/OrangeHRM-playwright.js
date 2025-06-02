from pages.login_page import LoginPage
from pages.admin_page import AdminPage

def test_add_user(page):
    page.goto("https://opensource-demo.orangehrmlive.com/")
    login = LoginPage(page)
    login.login("Admin", "admin123")
    admin = AdminPage(page)
    admin.navigate_to_admin()
    admin.add_user("Admin", "Linda Anderson", "testuserpy", "Enabled", "Testpass123!")

def test_search_user(page):
    page.goto("https://opensource-demo.orangehrmlive.com/")
    login = LoginPage(page)
    login.login("Admin", "admin123")
    admin = AdminPage(page)
    admin.navigate_to_admin()
    admin.search_user("testuserpy")

def test_delete_user(page):
    page.goto("https://opensource-demo.orangehrmlive.com/")
    login = LoginPage(page)
    login.login("Admin", "admin123")
    admin = AdminPage(page)
    admin.navigate_to_admin()
    admin.delete_user("testuserpy")
