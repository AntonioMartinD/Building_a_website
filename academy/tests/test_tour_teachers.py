from odoo.tests import HttpCase, tagged


@tagged("post_install", "-at_install", "academy")
class TestUiTeachers(HttpCase):
    def test_01_admin_teachers_tour(self):
        self.start_tour("/academy/academy", "tour_show_biographies", login="admin")
