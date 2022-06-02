from ml_test.distance import haversine


def test_haversine_postive_distance(lon1 = 1, lat1 = 2, lon2 = 3, lat2 = 4):
    assert(type(lon1) != "str")
    assert(type(lat1) != "str")
    assert(type(lon2) != "str")
    assert(type(lat2) != "str")
    assert(haversine(lon1 = 1, lat1 = 2, lon2 = 3, lat2 = 4) >0)
