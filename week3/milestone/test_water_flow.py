from pytest import approx
import pytest
from water_flow import water_column_height,pressure_gain_from_water_height,pressure_loss_from_pipe,pressure_loss_from_fittings,reynolds_number,pressure_loss_from_pipe_reduction,convert_kPa_to_psi

def test_water_column_height():
    assert water_column_height(0.0,00)== 0.0
    assert water_column_height(0.0,10.0)==7.5
    assert water_column_height(25.0,00)==25.0
    assert water_column_height(48.3,12.8)==57.9

def test_pressure_gain_from_water_height():
    assert pressure_gain_from_water_height(0.0) == approx(0.000)
    assert pressure_gain_from_water_height(30.2) == approx(295.628)
    assert pressure_gain_from_water_height(50.0) == approx(489.450)

def test_pressure_loss_from_pipe():
    assert pressure_loss_from_pipe(0.048692,0.000,0.018,1.75)== approx(0.000)
    assert pressure_loss_from_pipe(0.048692,200.00,0.000,1.75)== approx(0.000)
    assert pressure_loss_from_pipe(0.048692,200.00,0.018,0.00)== approx(0.000)

    expected_value = -113.008 
    assert abs(pressure_loss_from_pipe(0.048692,200.00,0.018,1.75) - expected_value) <= 0.001

    expected_value =-100.462
    assert abs(pressure_loss_from_pipe(0.048692,200.00,0.018,1.65)- expected_value) <= 0.001

    expected_value = -61.576
    assert abs(pressure_loss_from_pipe(0.286870,1000.00,0.013,1.65)-expected_value) <= 0.001
    
    expected_value = -110.884
    assert abs(pressure_loss_from_pipe(0.286870,1800.75,0.013,1.65)-expected_value) <= 0.001

def test_pressure_loss_from_fittings():
    assert abs(pressure_loss_from_fittings(0.00, 3) - 0.000) <= 0.001
    assert abs(pressure_loss_from_fittings(1.65, 0) - 0.000) <= 0.001
    assert abs(pressure_loss_from_fittings(1.65, 2) + 0.109) <= 0.001
    assert abs(pressure_loss_from_fittings(1.75, 2) + 0.122) <= 0.001
    assert abs(pressure_loss_from_fittings(1.75, 5) + 0.306) <= 0.001

def test_reynolds_number():
    assert abs(reynolds_number(0.048692, 0.00) - 0) <= 1
    assert abs(reynolds_number(0.048692, 1.65) - 80069) <= 1
    assert abs(reynolds_number(0.048692, 1.75) - 84922) <= 1
    assert abs(reynolds_number(0.286870, 1.65) - 471729) <= 1
    assert abs(reynolds_number(0.286870, 1.75) - 500318) <= 1

def test_pressure_loss_from_pipe_reduction():
    assert pressure_loss_from_pipe_reduction(0.28687, 0.00, 1, 0.048692) == approx(0.000, abs=0.001)
    assert pressure_loss_from_pipe_reduction(0.28687, 1.65, 471729, 0.048692) == approx(-163.744, abs=0.001)
    assert pressure_loss_from_pipe_reduction(0.28687, 1.75, 500318, 0.048692) == approx(-184.182, abs=0.001)

#Exceeding the Requirements
def test_convert_kPa_to_psi():
    assert convert_kPa_to_psi(0) == approx(0.0, abs=0.001)
    assert convert_kPa_to_psi(100) == approx(14.5038, abs=0.001)
    assert convert_kPa_to_psi(200) == approx(29.0076, abs=0.001)
    assert convert_kPa_to_psi(500) == approx(72.519, abs=0.001)
    #specific value
    assert convert_kPa_to_psi(158.7) == approx(23.0182, abs=0.001)


pytest.main(["-v", "--tb=line", "-rN", __file__])