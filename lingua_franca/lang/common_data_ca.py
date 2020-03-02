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

# NOTE: This file as no use yet. It needs to be called from other functions

from collections import OrderedDict


_ARTICLES_ES = {'el', 'la', 'los', 'las'}


_NUM_STRING_ES = {
    "zero": 0,
"un": 1,
"un": 1,
"una": 1,
"dos": 2,
"dues": 2,
"tres": 3,
"quatre": 4,
"cinc": 5,
"sis": 6,
"set": 7,
"vuit": 8,
"nou": 9,
"deu": 10,
"onze": 11,
"dotze": 12,
"tretze": 13,
"catorze": 14,
"quinze": 15,
"setze": 16,
"disset": 17,
"divuit": 18,
"dinou": 19,
"vint": 20,
"vint-i-un": 21,
"vint-i-dos": 22,
"vint-i-tres": 23,
"vint-i-quatre": 24,
"vint-i-cinc": 25,
"vint-i-sis": 26,
"vint-i-set": 27,
"vint-i-vuit": 28,
"vint-i-nou": 29,
"trenta": 30,
"quaranta": 40,
"cinquanta": 50,
"seixanta": 60,
"setanta": 70,
"vuitanta": 80,
"noranta": 90,
"cent": 100,
"cent": 100,
"dos-cents": 200,
"dues-centes": 200,
"tres-cents": 300,
"tres-centes": 300,
"quatre-cents": 400,
"quatre-centes": 400,
"cinc-cents": 500,
"cinc-centes": 500,
"sis-cents": 600,
"sis-centes": 600,
"set-cents": 700,
"set-centes": 700,
"vuit-cents": 800,
"vuit-centes": 800,
"nou-cents": 900,
"nou-centes": 900,
"mil": 1000}


_FRACTION_STRING_ES = {
2: 'mig',
3: 'terç',
4: 'quart',
5: 'cinquè',
6: 'sisè',
7: 'setè',
8: 'vuitè',
9: 'novè',
10: 'dècim',
11: 'onzè',
12: 'dotzè',
13: 'tretzè',
14: 'catorzè',
15: 'quinzè',
16: 'setzè',
17: 'disetè',
18: 'divuitè',
19: 'dinovè',
20: 'vintè'
}

# https://www.grobauer.at/es_eur/zahlnamen.php
_LONG_SCALE_ES = OrderedDict([
(100, 'centena'),
(1000, 'miler'),
(1000000, 'milió'),
(1e9, "miliard"),
(1e12, "bilió"),
(1e18, 'trilió'),
])


_SHORT_SCALE_ES = OrderedDict([
(100, 'centena'),
(1000, 'miler'),
(1000000, 'milió'),
(1e9, "bilió"),
(1e12, 'trilió'),
])

# TODO: female forms.
_ORDINAL_STRING_BASE_ES = {
1: 'primer',
2: 'segon',
3: 'tercer',
4: 'quart',
5: 'cinquè',
6: 'sisè',
7: 'setè',
8: 'vuitè',
9: 'novè',
10: 'dècim',
11: 'onzè',
12: 'dotzè',
13: 'tretzè',
14: 'catorzè',
15: 'quinzè',
16: 'setzè',
17: 'dissetè',
18: 'divuitè',
19: 'dinovè',
20: 'vintè',
30: 'trentè',
40: "quarantè",
50: "cinquantè",
60: "seixantè",
70: "setantè",
80: "vuitantè",
90: "norantè",
10e3: "centèssim",
1e3: "mil·lèsim"
}


_SHORT_ORDINAL_STRING_ES = {
1e6: "milionèsim",
1e9: "milmilionèsim",
1e12: "bilionéssim",


    # TODO > 1e-18
}
_SHORT_ORDINAL_STRING_ES.update(_ORDINAL_STRING_BASE_ES)


_LONG_ORDINAL_STRING_ES = {
1e6: "milionèsim",
1e9: "milmilionèsim",
1e12: "bilionéssim",
    # TODO > 1e-18
}
_LONG_ORDINAL_STRING_ES.update(_ORDINAL_STRING_BASE_ES)
