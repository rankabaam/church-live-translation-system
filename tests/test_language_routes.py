import unittest
from app.main import app


class LanguagePreviewRouteTests(unittest.TestCase):
    def test_routes_are_registered(self):
        routes = {route.path: route for route in app.routes}
        self.assertIn("/api/languages", routes)
        self.assertIn("/api/language-demo", routes)
        self.assertIn("/language-demo", routes)
        self.assertIn("POST", routes["/api/language-demo"].methods)

    def test_original_routes_remain_available(self):
        paths = {route.path for route in app.routes}
        self.assertIn("/api/process", paths)
        self.assertIn("/ws", paths)
        self.assertIn("/api/segments", paths)


if __name__ == "__main__":
    unittest.main()
