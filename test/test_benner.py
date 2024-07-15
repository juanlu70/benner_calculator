import benner_calculator


bc = benner_calculator.BennerCalculator()


def test_cycle_discovery_loop():
    bc.input_year = 1924
    cycle = {
        'initial_year': 1927,
        'years_distance': [1, 2, 3],
        'years': [1927],
        'explanation': "This is only a test."
    }

    years = bc.cycle_discovery_loop(cycle)

    assert years[10] == 1946

    return
