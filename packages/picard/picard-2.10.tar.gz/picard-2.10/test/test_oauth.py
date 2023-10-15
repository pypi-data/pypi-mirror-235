# -*- coding: utf-8 -*-
#
# Picard, the next-generation MusicBrainz tagger
#
# Copyright (C) 2022 Laurent Monin
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.


from test.picardtestcase import PicardTestCase

from picard.oauth import OAuthManager


class OAuthManagerTest(PicardTestCase):

    def test_query_data(self):
        params = {
            'a&b': 'a b',
            'c d': 'c&d',
            'e=f': 'e=f',
            '': '',
        }
        data = OAuthManager._query_data(params)
        self.assertEqual(data, "a%26b=a+b&c+d=c%26d&e%3Df=e%3Df")
