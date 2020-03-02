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
from datetime import datetime
import unittest

from lingua_franca.parse import (normalize, extract_numbers, extract_number,
                                 extract_datetime, extract_datetime_es,
                                 isFractional_es)

class TestNormalize(unittest.TestCase):
    """
        Test cases for Catalan parsing
    """

    def test_numbers_es(self):
        self.assertEqual(normalize("això es un una", lang="ca"),
                         "esto es 1 1")

    def test_extract_number_es(self):
        self.assertEqual(extract_number("sis punt dos", lang='ca'), 6.2)

    def test_isFraction_es(self):
        self.assertEqual(isFractional_es("mil·lèssima"), 1.0 / 1000)
    
    @unittest.skip("unwritten logic")
    def test_comma_fraction_logic_es(self):
        # Logic has not been written to parse "#,#" as "#.#"
        # English-style decimal numbers work because they just get float(str)ed
        self.assertEqual(extract_number("2,0", lang='ca'), 2.0)


class TestDatetime_es(unittest.TestCase):

    def test_datetime_by_date_es(self):
        # test currentDate==None
        _now = datetime.now()
        relative_year = _now.year if (_now.month == 1 and _now.day < 11) else \
                        (_now.year + 1)
        self.assertEqual(extract_datetime_es("11 ene")[0],
                         datetime(relative_year, 1, 11))

        # test months
        self.assertEqual(extract_datetime(
            "11 gen", lang='ca', anchorDate=datetime(1998, 1, 1))[0],
            datetime(1998, 1, 11))

        self.assertEqual(extract_datetime("", lang='ca'), None)

    # TODO fix bug causing these tests to fail (MycroftAI/mycroft-core#2348)
    #         reparar error de traducción preveniendo las funciones abajo de
    #         retornar correctamente
    #         (escrito con disculpas por un Inglés hablante)
    #      further broken tests are below their respective working tests.
    @unittest.skip("currently processing these months incorrectly")
    def test_bugged_output_wastebasket(self):
        self.assertEqual(extract_datetime(
            "11 jun", lang='ca', anchorDate=datetime(1998, 6, 1))[0],
            datetime(1998, 6, 11))
        self.assertEqual(extract_datetime(
            "11 junio", lang='ca', anchorDate=datetime(1998, 6, 1))[0],
            datetime(1998, 6, 11))
        self.assertEqual(extract_datetime(
            "11 jul", lang='ca', anchorDate=datetime(1998, 7, 1))[0],
            datetime(1998, 7, 11))
        self.assertEqual(extract_datetime(
            "11 ago", lang='ca', anchorDate=datetime(1998, 8, 1))[0],
            datetime(1998, 8, 11))
        self.assertEqual(extract_datetime(
            "11 sep", lang='ca', anchorDate=datetime(1998, 9, 1))[0],
            datetime(1998, 9, 11))

        # It's also failing on years
        self.assertEqual(extract_datetime(
            "11 ago 1998", lang='ca')[0], datetime(1998, 8, 11))

    def test_extract_datetime_relative(self):
        self.assertEqual(extract_datetime(
            "esta noche", anchorDate=datetime(1998, 1, 1),
            lang='ca'), [datetime(1998, 1, 1, 21, 0, 0), 'esta'])
        self.assertEqual(extract_datetime(
            "ayer noche", anchorDate=datetime(1998, 1, 1),
            lang='ca')[0], datetime(1997, 12, 31, 21))
        self.assertEqual(extract_datetime(
            "el noche anteayer", anchorDate=datetime(1998, 1, 1),
            lang='ca')[0], datetime(1997, 12, 30, 21))
        self.assertEqual(extract_datetime(
            "el noche ante ante ayer", anchorDate=datetime(1998, 1, 1),
            lang='ca')[0], datetime(1997, 12, 29, 21))
        self.assertEqual(extract_datetime(
            "mañana por la mañana", anchorDate=datetime(1998, 1, 1),
            lang='ca')[0], datetime(1998, 1, 2, 8))
        self.assertEqual(extract_datetime(
            "ayer por la tarde", anchorDate=datetime(1998, 1, 1),
            lang='ca')[0], datetime(1997, 12, 31, 15))

        self.assertEqual(extract_datetime(
            "qué año es", anchorDate=datetime(1998, 1, 1),
            lang='ca')[0], datetime(1998, 1, 1))

        self.assertEqual(extract_datetime("hoy 2 de la mañana", lang='ca',
                                          anchorDate=datetime(1998, 1, 1))[0],
                         datetime(1998, 1, 1, 2))
        self.assertEqual(extract_datetime("hoy 2 de la tarde", lang='ca',
                                          anchorDate=datetime(1998, 1, 1))[0],
                         datetime(1998, 1, 1, 14))

    @unittest.skip("These phrases are not parsing correctly.")
    def test_extract_datetime_relative_failing(self):
        # parses as "morning" and returns 8:00 on anchorDate
        self.assertEqual(extract_datetime(
            "mañana", anchorDate=datetime(1998, 1, 1), lang='ca')[0],
            datetime(1998, 1, 2))

        # unimplemented logic
        self.assertEqual(extract_datetime(
            "anoche", anchorDate=datetime(1998, 1, 1),
            lang='ca')[0], datetime(1997, 12, 31, 21))
        self.assertEqual(extract_datetime(
            "anteanoche", anchorDate=datetime(1998, 1, 1),
            lang='ca')[0], datetime(1997, 12, 30, 21))
        self.assertEqual(extract_datetime(
            "hace tres noches", anchorDate=datetime(1998, 1, 1),
            lang='ca')[0], datetime(1997, 12, 29, 21))


if __name__ == "__main__":
    unittest.main()
