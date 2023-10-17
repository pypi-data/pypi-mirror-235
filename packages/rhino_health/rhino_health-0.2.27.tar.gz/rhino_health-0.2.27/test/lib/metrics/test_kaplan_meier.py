import json
import os

import pytest

from rhino_health.lib.metrics.base_metric import KaplanMeierMetricResponse


@pytest.mark.skipif(
    os.environ.get("RHINO_SDK_WITH_EXTRAS") != "1",
    reason="Optional statsmodels dependency statsmodels not installed",
)
def test_kaplan_meier_statsmodels():
    """
    Test that when the sdk is installed "with_extras" then the statsmodels package is installed and the statsmodels
     survival function model is created correctly by the KaplanMeierMetricResponse.surv_func_right_model() method
    """
    time_vector = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    event_vector = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
    response = KaplanMeierMetricResponse(
        metric_configuration_dict={
            "arguments": json.dumps({"time_variable": "Time", "event_variable": "Event"})
        },
        output={"null": {"Time": time_vector, "Event": event_vector}},
    )
    model = response.surv_func_right_model()
    assert model.summary()["num events"] == 5
    assert model.summary()["num censored"] == 5


@pytest.mark.skipif(
    os.environ.get("RHINO_SDK_WITH_EXTRAS") == "1",
    reason="Optional statsmodels dependency statsmodels is installed",
)
def test_kaplan_meier_no_statsmodels():
    time_vector = [1]
    event_vector = [1]
    response = KaplanMeierMetricResponse(
        metric_configuration_dict={
            "arguments": json.dumps({"time_variable": "Time", "event_variable": "Event"})
        },
        output={"null": {"Time": time_vector, "Event": event_vector}},
    )

    with pytest.raises(ImportError) as e:
        response.surv_func_right_model()
        assert "statsmodels" in str(e)
