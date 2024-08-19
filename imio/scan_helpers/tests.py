from utils import copy_sub_files
from utils import get_dated_backup_dir
from utils import get_main_backup_dir
from utils import get_scan_profiles_dir

import os
import shutil
import unittest


def p(path):
    return os.path.join(*(path.split("/")))


class TestUtils(unittest.TestCase):
    def test_copy_sub_files(self):
        dated_backup_dir = get_dated_backup_dir(p("test_env/kofax_backup"), day="2000-01-01")
        copy_sub_files(p("test_env/ProgramData/Kofax/Kofax Express 3.2/Jobs"), dated_backup_dir, files=["IMIO ENTRANT"])
        self.assertTrue(os.path.exists(p("test_env/kofax_backup/2000-01-01/IMIO ENTRANT/file1")))
        self.assertFalse(os.path.exists(p("test_env/kofax_backup/2000-01-01/IMIO SORTANT")))
        shutil.rmtree(p("test_env/kofax_backup/2000-01-01"))

    def test_copy_release_files_and_restart(self):
        pass

    def test_get_dated_backup_dir(self):
        self.assertFalse(os.path.exists(p("test_env/kofax_backup/2000-01-01")))
        result = get_dated_backup_dir(p("test_env/kofax_backup"), day="2000-01-01")
        self.assertEqual(result, p("test_env/kofax_backup/2000-01-01"))
        self.assertTrue(os.path.exists(p("test_env/kofax_backup/2000-01-01")))
        shutil.rmtree(p("test_env/kofax_backup/2000-01-01"))

    def test_get_main_backup_dir(self):
        self.assertEqual(get_main_backup_dir(create=False), p("test_env/kofax_backup"))

    def test_scan_profiles_dir(self):
        self.assertEqual(get_scan_profiles_dir(), p("test_env/ProgramData/Kofax/Kofax Express 3.2/Jobs"))


if __name__ == "__main__":
    unittest.main()
