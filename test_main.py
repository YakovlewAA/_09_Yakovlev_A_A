
from main import get_bilet

def test_get_bilet_1():
    lines = ['4, 1, 1, "Futrelle, Mrs. Jacques Heath (Lily May Peel)", female, 35, 1, 0, 0, 53, C123, S',
             '5, 0, 3, "Allen, Mr. William Henry", male, 35, 0, 0, 0, 8,, C',
             '6, 0, 3, "Moran, Mr. James", male,, 0, 0, 0, 85,, Q']

    assert get_bilet(lines) == (53, 1, 53, 53, 8, 1, 8, 8, 85, 1, 85, 85)

def test_get_bilet_2():
    lines = ['4, 1, 1, "Futrelle, Mrs. Jacques Heath (Lily May Peel)", female, 35, 1, 0, 0, 10, C123, S',
             '5, 0, 3, "Allen, Mr. William Henry", male, 35, 0, 0, 0, 1,, C',
             '6, 0, 3, "Moran, Mr. James", male,, 0, 0, 0, 2,, Q',

             '4, 1, 1, "Futrelle, Mrs. Jacques Heath (Lily May Peel)", female, 35, 1, 0, 0, 20, C123, S',
             '5, 0, 3, "Allen, Mr. William Henry", male, 35, 0, 0, 0, 2,, C',
             '6, 0, 3, "Moran, Mr. James", male,, 0, 0, 0, 4,, Q',

             '4, 1, 1, "Futrelle, Mrs. Jacques Heath (Lily May Peel)", female, 35, 1, 0, 0, 30, C123, S',
             '5, 0, 3, "Allen, Mr. William Henry", male, 35, 0, 0, 0, 3,, C',
             '6, 0, 3, "Moran, Mr. James", male,, 0, 0, 0, 6,, Q']

    assert get_bilet(lines) == (60, 3, 10, 30,     6, 3, 1, 3,     12, 3, 2, 6)

def test_get_bilet_3():
    lines = ['4, 1, 1, "Futrelle, Mrs. Jacques Heath (Lily May Peel)", female, 35, 1, 0, 113803, 53, C123, S',
             '5, 0, 3, "Allen, Mr. William Henry", male, 35, 0, 0, 373450, 85,, C',
             '6, 0, 3, "Moran, Mr. James", male,, 0, 0, 330877, 8,, Q',
             # пассажиры с неуказанной стоимостью билета:
             '4, 1, 1, "Futrelle, Mrs. Jacques Heath (Lily May Peel)", female, 35, 1, 0, 0,, C123, S',
             '5, 0, 3, "Allen, Mr. William Henry", male, 35, 0, 0, 0,,, C',
             '6, 0, 3, "Moran, Mr. James", male,, 0, 0, 0,,, Q']

    assert get_bilet(lines) == (53, 1, 53, 53,    85, 1, 85, 85,    8, 1, 8, 8)




