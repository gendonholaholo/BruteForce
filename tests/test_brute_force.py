# tests/test_brute_force.py - Unit test
import unittest
from bruteforce_tester.response_analyzer import analyze_response

class TestBruteForce(unittest.TestCase):
    def test_analyze_response(self):
        class MockResponse:
            def __init__(self, status_code, text):
                self.status_code = status_code
                self.text = text
        
        response_success = MockResponse(200, "Welcome to Dashboard")
        response_fail = MockResponse(401, "Invalid Credentials")
        
        self.assertTrue(analyze_response(response_success))
        self.assertFalse(analyze_response(response_fail))

if __name__ == "__main__":
    unittest.main()
