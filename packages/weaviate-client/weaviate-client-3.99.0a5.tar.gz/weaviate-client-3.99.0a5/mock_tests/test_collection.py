from datetime import datetime

from pytest_httpserver import HTTPServer

import weaviate
from mock_tests.conftest import MOCK_SERVER_URL


def test_warning_old_weaviate(recwarn, ready_mock: HTTPServer):
    ready_mock.expect_request("/v1/meta").respond_with_json({"version": "1.21.0"})
    ready_mock.expect_request("/v1/objects").respond_with_json({})

    client = weaviate.Client(MOCK_SERVER_URL)
    client.collection.get("Class").data.insert(
        {
            "date": datetime.now(),
        }
    )

    assert len(recwarn) == 1
    w = recwarn.pop()
    assert issubclass(w.category, UserWarning)
    assert str(w.message).startswith("Con002")
