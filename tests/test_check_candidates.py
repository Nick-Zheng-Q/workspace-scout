import importlib.util
import unittest
from pathlib import Path


SPEC = importlib.util.spec_from_file_location("check_candidates", Path(__file__).resolve().parents[1] / "scripts" / "check_candidates.py")
module = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(module)


class CheckCandidatesTests(unittest.TestCase):
    def test_unknown_required_fee_does_not_become_within_budget(self):
        data = {"hard_requirements": ["weekend"], "budgets": {"monthly_max": 3000}, "candidates": [{
            "id": "desk", "conditions": {"weekend": "met"}, "costs": [
                {"name": "desk", "kind": "recurring", "amount": 2000},
                {"name": "storage", "kind": "recurring", "amount": None},
            ]}]}
        row = module.summarize(data)["candidates"][0]
        self.assertEqual(row["known_monthly"], 2000)
        self.assertEqual(row["monthly_budget_status"], "unknown")
        self.assertEqual(row["hard_condition_gate"], "pass")

    def test_conflict_requires_verification_and_unmet_rejects(self):
        data = {"hard_requirements": ["visitors", "overnight equipment"], "candidates": [
            {"id": "room", "conditions": {"visitors": "conflict", "overnight equipment": "met"}},
            {"id": "day-use", "conditions": {"visitors": "met", "overnight equipment": "unmet"}},
        ]}
        rows = module.summarize(data)["candidates"]
        self.assertEqual([x["hard_condition_gate"] for x in rows], ["verify", "reject"])

    def test_deposit_separate_from_nonrefundable_and_no_discount(self):
        data = {"budgets": {"upfront_max": 5000}, "candidates": [{"id": "room", "costs": [
            {"name": "setup", "kind": "upfront", "amount": 1000},
            {"name": "deposit", "kind": "deposit", "amount": 5000},
            {"name": "possible subsidy", "kind": "recurring", "amount": 1000, "required": False},
        ]}]}
        row = module.summarize(data)["candidates"][0]
        self.assertEqual(row["known_upfront_nonrefundable"], 1000)
        self.assertEqual(row["known_refundable_deposit"], 5000)
        self.assertEqual(row["upfront_budget_status"], "over")
        self.assertEqual(row["known_monthly"], 0)

    def test_missing_hard_condition_is_unknown_and_negative_amount_rejected(self):
        data = {"hard_requirements": ["weekend"], "candidates": [{"id": "room"}]}
        self.assertEqual(module.summarize(data)["candidates"][0]["hard_condition_gate"], "verify")
        data["candidates"][0]["costs"] = [{"name": "rent", "kind": "recurring", "amount": -1}]
        with self.assertRaises(ValueError):
            module.summarize(data)

    def test_no_cost_data_is_not_reported_within_budget(self):
        data = {"budgets": {"monthly_max": 1000, "upfront_max": 2000}, "candidates": [{"id": "unpriced"}]}
        row = module.summarize(data)["candidates"][0]
        self.assertEqual(row["monthly_budget_status"], "unknown")
        self.assertEqual(row["upfront_budget_status"], "unknown")

    def test_below_budget_requires_confirmed_cost_scope(self):
        data = {"budgets": {"monthly_max": 4500}, "candidates": [{"id": "day-pass", "costs": [
            {"name": "13 day passes", "kind": "recurring", "amount": 280, "quantity": 13},
        ]}]}
        self.assertEqual(module.summarize(data)["candidates"][0]["monthly_budget_status"], "unknown")
        data["candidates"][0]["required_costs_complete"] = True
        self.assertEqual(module.summarize(data)["candidates"][0]["monthly_budget_status"], "within_confirmed_scope")

    def test_omitted_upfront_categories_are_not_assumed_zero(self):
        data = {"budgets": {"upfront_max": 1000}, "candidates": [{
            "id": "desk", "required_costs_complete": True,
            "costs": [{"name": "rent", "kind": "recurring", "amount": 500}],
        }]}
        row = module.summarize(data)["candidates"][0]
        self.assertEqual(row["upfront_budget_status"], "unknown")
        data["candidates"][0]["costs"] += [
            {"name": "no setup fee confirmed", "kind": "upfront", "amount": 0},
            {"name": "no deposit confirmed", "kind": "deposit", "amount": 0},
        ]
        self.assertEqual(module.summarize(data)["candidates"][0]["upfront_budget_status"], "within_confirmed_scope")

    def test_free_rent_with_unknown_required_fee_is_not_zero_total(self):
        data = {"budgets": {"monthly_max": 1000}, "candidates": [{
            "id": "approved-free-desk", "required_costs_complete": True,
            "costs": [
                {"name": "rent", "kind": "recurring", "amount": 0},
                {"name": "management fee", "kind": "recurring", "amount": None},
            ],
        }]}
        row = module.summarize(data)["candidates"][0]
        self.assertEqual(row["known_monthly"], 0)
        self.assertEqual(row["monthly_budget_status"], "unknown")


if __name__ == "__main__":
    unittest.main()
