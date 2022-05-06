import random
from typing import List
from unittest import TestCase

from app.target_selector.domain.entities.ranked_scanned_point import \
    RankedScannedPoint
from app.target_selector.domain.priority_protocols.assist_allies_protocol import \
    AssistAlliesProtocol
from app.target_selector.domain.priority_protocols.tests.null_protocol import \
    NullProtocol
from app.target_selector.domain.priority_protocols.tests.scanned_point_mother import \
    ScannedPointMother


class UnitTestAssistAlliesProtocol(TestCase):
    def _assert_list_ranked_points_only_contains_allies(
        self, points: List[RankedScannedPoint]
    ):
        self.assertTrue(all(p.scanned_point.allies > 0 for p in points))

    def setUp(self):
        self.assist_allies_protocol = AssistAlliesProtocol(NullProtocol())

    def test_points_without_allies(self):
        pre_ranked_scanned_points = [
            RankedScannedPoint(scanned_point=ScannedPointMother.build(allies=0))
            for _ in range(random.randint(1, 10))
        ]

        post_ranked_scanned_points = self.assist_allies_protocol.rank_points(
            pre_ranked_scanned_points
        )

        self.assertEqual(pre_ranked_scanned_points, post_ranked_scanned_points)

    def test_one_point_with_allies(self):
        pre_ranked_scanned_points = [
            RankedScannedPoint(scanned_point=ScannedPointMother.build(allies=0))
            for _ in range(random.randint(1, 10))
        ]
        pre_ranked_scanned_points.append(
            RankedScannedPoint(
                scanned_point=ScannedPointMother.build(allies=random.randint(1, 10))
            )
        )

        post_ranked_scanned_points = self.assist_allies_protocol.rank_points(
            pre_ranked_scanned_points
        )

        self._assert_list_ranked_points_only_contains_allies(post_ranked_scanned_points)

    def test_two_points_with_allies(self):
        pre_ranked_scanned_points = [
            RankedScannedPoint(scanned_point=ScannedPointMother.build(allies=0))
            for _ in range(random.randint(1, 10))
        ]
        pre_ranked_scanned_points.append(
            RankedScannedPoint(
                scanned_point=ScannedPointMother.build(allies=random.randint(1, 10))
            )
        )
        pre_ranked_scanned_points.append(
            RankedScannedPoint(
                scanned_point=ScannedPointMother.build(allies=random.randint(1, 10))
            )
        )

        post_ranked_scanned_points = self.assist_allies_protocol.rank_points(
            pre_ranked_scanned_points
        )

        self._assert_list_ranked_points_only_contains_allies(post_ranked_scanned_points)
