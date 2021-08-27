import pytest
from rpdmodel import ltp

def test_oil_ltp_predict():
    volume = 4000.0
    rate_true = [732.005, 598.936, 490.057, 400.97 , 328.079, 268.438, 219.64 ,
                 179.712, 147.042, 120.312,  98.441,  80.545,  65.903,  53.923,
                  44.12 ,  36.1  ,  29.537,  24.168,  19.774,  16.18 ,  13.238,
                  10.832,   8.863,   7.252,   5.933]

    rate_calc = ltp.oil_ltp_predict(volume)

    assert rate_true == pytest.approx(rate_calc)

def test_gas_ltp_predict():
    volume = 1000.0
    rate_true = [ 0.   , 38.471, 76.942, 76.942, 76.942, 76.942, 76.942, 76.942,
                 76.942, 76.942, 76.942, 76.942, 76.942, 46.165, 27.699, 16.62 ,
                  9.972,  5.983,  3.59 ,  2.154,  1.292,  0.775,  0.465,  0.279,
                  0.173]

    rate_calc = ltp.gas_ltp_predict(volume)

    assert rate_true == pytest.approx(rate_calc)