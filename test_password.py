# coding: utf-8
import unittest
import password as pwd

class TestPassword(unittest.TestCase):

 def test_getNextNormal(self):
 self.assertEqual(pwd.getNext("bcde"), "bcdf")

 def test_getNextEndLine(self):
 self.assertEqual(pwd.getNext("abgz"), "abha")


# Permet d'exécuter les tests si ce fichier est exécuté
unittest.main()