from pathlib import Path
import numpy.testing as npt
from unittest.mock import Mock

def test_compute_standard_deviation_by_day():
    from inflammation.compute_data import compute_standard_deviation_by_day
    # Each file contains 2D array with rows (patients) and columns (days).
    file_1 = [[0,1,0], [0, 2, 0]]
    input_data = [file_1]
    result = compute_standard_deviation_by_day(input_data)
    npt.assert_almost_equal(result, [0,0,0])


def test_analyse_data():
    from inflammation.compute_data import analyse_data, CSVDataSource, JSONDataSource
    path = Path.cwd() / "data"
    data_dir = CSVDataSource(path)
    result = analyse_data(data_dir)
    print(repr(result))
    npt.assert_array_almost_equal(result, [0, 0.22510286, 0.18157299, 0.1264423 , 0.9495481 ,
       0.27118211, 0.25104719, 0.22330897, 0.89680503, 0.21573875,
       1.24235548, 0.63042094, 1.57511696, 2.18850242, 0.3729574 ,
       0.69395538, 2.52365162, 0.3179312 , 1.22850657, 1.63149639,
       2.45861227, 1.55556052, 2.8214853 , 0.92117578, 0.76176979,
       2.18346188, 0.55368435, 1.78441632, 0.26549221, 1.43938417,
       0.78959769, 0.64913879, 1.16078544, 0.42417995, 0.36019114,
       0.80801707, 0.50323031, 0.47574665, 0.45197398, 0.22070227])
    
def test_compute_data_mock_source():
    from inflammation.compute_data import analyse_data
    data_source = Mock()

    result = data_source.analyse_data.return_value = [0, 0.22510286, 0.18157299, 0.1264423 , 0.9495481 ,
        0.27118211, 0.25104719, 0.22330897, 0.89680503, 0.21573875,
       1.24235548, 0.63042094, 1.57511696, 2.18850242, 0.3729574 ,
       0.69395538, 2.52365162, 0.3179312 , 1.22850657, 1.63149639,
       2.45861227, 1.55556052, 2.8214853 , 0.92117578, 0.76176979,
       2.18346188, 0.55368435, 1.78441632, 0.26549221, 1.43938417,
       0.78959769, 0.64913879, 1.16078544, 0.42417995, 0.36019114,
       0.80801707, 0.50323031, 0.47574665, 0.45197398, 0.22070227]
    
    npt.assert_array_almost_equal(result, [0, 0.22510286, 0.18157299, 0.1264423 , 0.9495481 ,
       0.27118211, 0.25104719, 0.22330897, 0.89680503, 0.21573875,
       1.24235548, 0.63042094, 1.57511696, 2.18850242, 0.3729574 ,
       0.69395538, 2.52365162, 0.3179312 , 1.22850657, 1.63149639,
       2.45861227, 1.55556052, 2.8214853 , 0.92117578, 0.76176979,
       2.18346188, 0.55368435, 1.78441632, 0.26549221, 1.43938417,
       0.78959769, 0.64913879, 1.16078544, 0.42417995, 0.36019114,
       0.80801707, 0.50323031, 0.47574665, 0.45197398, 0.22070227])
    

   