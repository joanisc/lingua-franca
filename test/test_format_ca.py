#
# Copyright 2017 Mycroft AI Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import unittest
import datetime

from lingua_franca.format import nice_number
from lingua_franca.format import nice_time
from lingua_franca.format import pronounce_number

NUMBERS_FIXTURE_ES = {
1.435634: '1,436',
2: '2',
5.0: '5',
0.027: '0,027',
0.5: 'un mig',
1.333: '1 i 1 terç',
2.666: '2 i 2 terç',
0.25: 'un quart',
1.25: '1 i 1 quart',
0.75: '3 quarts',
1.75: '1 i 3 quarts',
3.4: '3 i 2 cinquens',
16.8333: '16 i 5 sisens',
12.5714: '12 i 4 setens',
9.625: '9 i 5 vuitens',
6.777: '6 i 7 novens',
3.1: '3 i 1 dècim',
2.272: '2 i 3 onzens',
5.583: '5 i 7 dotzens',
0.071: 'un catorzè',
6.466: '6 i 7 quinzens',
8.312: '8 i 5 setzens',
0.05: 'un vintè'

}


class TestNiceNumberFormat_es(unittest.TestCase):
    def test_convert_float_to_nice_number_es(self):
        for number, number_str in NUMBERS_FIXTURE_ES.items():
            self.assertEqual(nice_number(number, lang="ca-es"), number_str,
                             'should format {} as {} and not {}'.format(
                                 number, number_str, nice_number(
                                     number, lang="ca-es")))

    def test_specify_denominator_es(self):
        self.assertEqual(nice_number(5.5, lang="ca-es",
                                     denominators=[1, 2, 3]),
                         '5 y medio',
                         'should format 5.5 as 5 y medio not {}'.format(
                             nice_number(5.5, lang="ca-es",
                                         denominators=[1, 2, 3])))
        self.assertEqual(nice_number(2.333, lang="ca-es",
                                     denominators=[1, 2]),
                         '2,333',
                         'should format 2.333 as 2,333 not {}'.format(
                             nice_number(2.333, lang="ca-es",
                                         denominators=[1, 2])))

    def test_no_speech_es(self):
        self.assertEqual(nice_number(6.777, lang="ca-es", speech=False),
                         '6 7/9',
                         'should format 6.777 as 6 7/9 not {}'.format(
                             nice_number(6.777, lang="ca-es", speech=False)))
        self.assertEqual(nice_number(6.0, lang="ca-es", speech=False),
                         '6',
                         'should format 6.0 as 6 not {}'.format(
                             nice_number(6.0, lang="ca-es", speech=False)))
        self.assertEqual(nice_number(1234567890, lang="ca-es", speech=False),
                         '1 234 567 890',
                         'should format 1234567890 as'
                         '1 234 567 890 not {}'.format(
                             nice_number(1234567890, lang="ca-es",
                                         speech=False)))
        self.assertEqual(nice_number(12345.6789, lang="ca-es", speech=False),
                         '12 345,679',
                         'should format 12345.6789 as'
                         '12 345,679 not {}'.format(
                             nice_number(12345.6789, lang="ca-es",
                                         speech=False)))


class TestPronounceNumber(unittest.TestCase):
    def test_convert_int(self):
        self.assertEqual(pronounce_number(0, lang="es"), "zero")
        self.assertEqual(pronounce_number(1, lang="es"), "un")
        self.assertEqual(pronounce_number(10, lang="es"), "deu")
        self.assertEqual(pronounce_number(15, lang="es"), "quinze")

    def test_convert_negative_int(self):
        self.assertEqual(pronounce_number(-1, lang="es"), "menys un")
        self.assertEqual(pronounce_number(-10, lang="es"), "menys deu")
        self.assertEqual(pronounce_number(-15, lang="es"), "menos quince")
        self.assertEqual(pronounce_number(-99, lang="es"),
                         "menys noranta nou")

    def test_convert_decimals(self):
        self.assertEqual(pronounce_number(
            0.05, lang="es"), "zero coma zero cinc")
        self.assertEqual(pronounce_number(
            -0.05, lang="es"), "menys zero coma zero cinc")
        self.assertEqual(pronounce_number(1.234, lang="es"),
                         "un coma dos tres")

class TestNiceDateFormat(unittest.TestCase):
    def test_convert_times(self):
        dt = datetime.datetime(2017, 1, 31,
                               13, 22, 3)

        # Verify defaults haven't changed
        self.assertEqual(nice_time(dt, lang="ca-es"),
                         nice_time(dt, "ca-es", True, False, False))
    
if __name__ == "__main__":
    unittest.main()
