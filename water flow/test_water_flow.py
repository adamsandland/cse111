from water_flow import water_column_height, pressure_gain_from_tank_height, pressure_loss_from_pipe
import pytest

def test_water_column_height():
    assert water_column_height(0,0) == pytest.approx(0, abs=1e-1)
    assert water_column_height(25,0) == pytest.approx(25, abs=1e-1)
    assert water_column_height(0,10) == pytest.approx(7.5, abs=1e-1)
    assert water_column_height(48.3,12.8) == pytest.approx(57.9, abs=1e-1)

def test_pressure_gain_from_tank_height():
    assert pressure_gain_from_tank_height(0) == pytest.approx(0,1e-3)
    assert pressure_gain_from_tank_height(30.2) == pytest.approx(295.628,1e-3)
    assert pressure_gain_from_tank_height(50.0) == pytest.approx(489.450,1e-3)

def test_pressure_loss_from_pipe():
    assert pressure_loss_from_pipe(0.048692,0,0.018,1.75) == pytest.approx(0, 1e-3)
    assert pressure_loss_from_pipe(0.048692,200,0,1.75) == pytest.approx(0, 1e-3)
    assert pressure_loss_from_pipe(0.048692,200,0.018,0) == pytest.approx(0, 1e-3)
    assert pressure_loss_from_pipe(0.048692,200,0.018,1.75) == pytest.approx(-113.008, 1e-3)
    assert pressure_loss_from_pipe(0.048692,200,0.018,1.65) == pytest.approx(-100.462, 1e-3)
    assert pressure_loss_from_pipe(0.28687,1000,0.013,1.65) == pytest.approx(-61.576, 1e-3)
    assert pressure_loss_from_pipe(0.28687,1800.75,0.013,1.65) == pytest.approx(-110.884, 1e-3)

# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
