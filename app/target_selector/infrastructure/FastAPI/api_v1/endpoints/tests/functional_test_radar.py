import json
import os
from unittest import TestCase

from fastapi.testclient import TestClient

from app.target_selector.infrastructure.config import API_V1_STR
from app.target_selector.infrastructure.FastAPI.api_v1.endpoints.tests.point_mother import \
    PointMother
from app.target_selector.infrastructure.FastAPI.api_v1.endpoints.tests.radar_request_mother import \
    RadarRequestMother
from app.target_selector.infrastructure.FastAPI.main import app


class FunctionalTestRadar(TestCase):
    def setUp(self):
        self._client: TestClient = TestClient(app)

    def make_request(self, json_data):
        return self._client.post(f"{API_V1_STR}/radar", json=json_data)

    def test_invalid_body_unknown_attribute(self) -> None:
        point_data = PointMother.build()
        point_data["unknown_attribute"] = 5

        request_data = RadarRequestMother()
        request_data.add_point(point_data)

        endpoint_response = self.make_request(request_data.build())

        self.assertEqual(422, endpoint_response.status_code)

        json_response = endpoint_response.json()

        self.assertTrue({"error"}.issubset(json_response))
        self.assertTrue({"type", "message"}.issubset(json_response["error"]))
        self.assertEqual("invalid_request", json_response["error"]["type"])
        self.assertIn("unknown_attribute", json_response["error"]["message"])

    def test_invalid_body_missing_attribute(self) -> None:
        point_data = PointMother.build()
        del point_data["coordinates"]["x"]

        request_data = RadarRequestMother()
        request_data.add_point(point_data)

        endpoint_response = self.make_request(request_data.build())

        self.assertEqual(422, endpoint_response.status_code)

        json_response = endpoint_response.json()

        self.assertTrue({"error"}.issubset(json_response))
        self.assertTrue({"type", "message"}.issubset(json_response["error"]))
        self.assertEqual("invalid_request", json_response["error"]["type"])
        self.assertIn("x", json_response["error"]["message"])

    def test_incompatible_protocols(self) -> None:
        incompatible_protocols = [
            ["closest-enemies", "furthest-enemies"],
            ["assist-allies", "avoid-crossfire"],
            ["prioritize-mech", "avoid-mech"],
        ]

        for i in incompatible_protocols:
            request_data = RadarRequestMother(protocols=i)

            endpoint_response = self.make_request(request_data.build())

            self.assertEqual(422, endpoint_response.status_code)

            json_response = endpoint_response.json()

            self.assertTrue({"error"}.issubset(json_response))
            self.assertTrue({"type", "message"}.issubset(json_response["error"]))
            self.assertEqual(
                "invalid_combination_of_protocols", json_response["error"]["type"]
            )
            self.assertEqual(
                "The protocol combination used is not valid.",
                json_response["error"]["message"],
            )

    def test_valid_requests(self) -> None:
        TEST_DATA = "test_radar_valid_requests.json"

        test_data_path = os.path.dirname(os.path.abspath(__file__)) + "/" + TEST_DATA
        data = json.load(open(test_data_path))

        for r in data:
            endpoint_response = self.make_request(r["request"])

            assert endpoint_response.status_code == 200
            assert endpoint_response.json() == r["response"]
