import pytest

from tests.functional.adapter.utils.base_utils import BaseUtils
from tests.functional.adapter.utils.fixture_bool_or import (
    models__test_bool_or_sql,
    models__test_bool_or_yml,
    seeds__data_bool_or_csv,
    seeds__data_bool_or_expected_csv,
)


class BaseBoolOr(BaseUtils):
    @pytest.fixture(scope="class")
    def seeds(self):
        return {
            "data_bool_or.csv": seeds__data_bool_or_csv,
            "data_bool_or_expected.csv": seeds__data_bool_or_expected_csv,
        }

    @pytest.fixture(scope="class")
    def models(self):
        return {
            "test_bool_or.yml": models__test_bool_or_yml,
            "test_bool_or.sql": self.interpolate_macro_namespace(
                models__test_bool_or_sql, "bool_or"
            ),
        }


class TestBoolOr(BaseBoolOr):
    pass
