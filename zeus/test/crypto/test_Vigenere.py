# -----------------------------------------------------------------
# zeus: test_crypto.py
#
# Define zeus.crypto.Vigenere class unittest
#
# Copyright (C) 2016-2018, Christophe Fauchard
# -----------------------------------------------------------------

import unittest
import zeus


class VigenereTest(unittest.TestCase):
    """
    define unit tests for zeus.crypto.Vigenere class
    """

    def setUp(self):
        self.message = "decrypted message"
        self.key = 'rqieD]-87M.xE}o!nU?EXTf.U!Dxvy'

    def test_vigenere_memory(self):
        vigenere = zeus.crypto.Vigenere(string_key=self.key)
        vigenere.encrypt(self.message)

        self.assertIsInstance(vigenere, zeus.crypto.Vigenere)
        self.assertNotEqual(vigenere.get_crypted_datas(), self.message)
        self.assertEqual(vigenere.get_decrypted_datas_utf8(), self.message)


if __name__ == '__main__':
    unittest.main()
