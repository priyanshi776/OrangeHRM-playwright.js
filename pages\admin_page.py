class AdminPage:
    def __init__(self, page):
        self.page = page

    def navigate_to_admin(self):
        self.page.click("a:has-text('Admin')")

    def add_user(self, role, emp_name, username, status, password):
        self.page.click("button:has-text('Add')")
        # Select user role and status from dropdown
        # Fill form fields and save

    def search_user(self, username):
        self.page.fill("input[placeholder='Search']", username)
        self.page.click("button:has-text('Search')")

    def delete_user(self, username):
        self.search_user(username)
        self.page.click("i[class*='trash']")
        self.page.click("button:has-text('Yes, Delete')")
