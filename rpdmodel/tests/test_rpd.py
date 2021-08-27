import pytest
from rpdmodel import RPDModel

def test_predict_rate():
    volume = 100
    rate_true = [ 0., 5.449, 10.898, 10.898, 10.898, 10.061, 9.287, 8.573,
                  7.914, 7.305, 6.744, 6.225, 5.748]
                
    rpd = RPDModel()
    rate_calc = rpd.predict(volume)
    print(rate_calc)

    assert pytest.approx(rate_calc) == rate_true

def test_predict_sum_equal_volume():
    volume = 100

    rpd = RPDModel()
    assert volume == pytest.approx(rpd.predict(volume).sum())