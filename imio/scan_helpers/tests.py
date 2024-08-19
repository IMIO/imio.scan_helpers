from utils import copy_release_files_and_restart
from utils import copy_sub_files
from utils import download_update
from utils import get_dated_backup_dir
from utils import get_download_dir_path
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
        copy_release_files_and_restart("anything", "test_env")
        self.assertTrue(os.path.exists(p("test_env/copy_release_files_and_restart.bat")))
        with open(p("test_env/copy_release_files_and_restart.bat"), "r") as file:
            content = file.read()
            self.assertIn('xcopy /s /e /h /r /y /q "anything\\*" "test_env"', content)
        os.remove(p("test_env/copy_release_files_and_restart.bat"))

    def test_download_update(self):
        download_update(
            "https://github.com/IMIO/imio.scan_helpers/raw/main/requirements.txt", p("test_env/download.txt")
        )
        self.assertTrue(os.path.exists(p("test_env/download.txt")))
        with open(p("test_env/download.txt"), "r") as file:
            content = file.read()
            self.assertIn("pyinstaller\nrequests", content)
        os.remove(p("test_env/download.txt"))

    def test_get_dated_backup_dir(self):
        self.assertFalse(os.path.exists(p("test_env/kofax_backup/2000-01-01")))
        result = get_dated_backup_dir(p("test_env/kofax_backup"), day="2000-01-01")
        self.assertEqual(result, p("test_env/kofax_backup/2000-01-01"))
        self.assertTrue(os.path.exists(p("test_env/kofax_backup/2000-01-01")))
        shutil.rmtree(p("test_env/kofax_backup/2000-01-01"))

    def test_get_download_dir_path(self):
        self.assertTrue(get_download_dir_path().endswith(p("imio.scan_helpers/_downloads")))

    def test_get_main_backup_dir(self):
        self.assertEqual(get_main_backup_dir(create=False), p("test_env/kofax_backup"))

    def test_scan_profiles_dir(self):
        self.assertEqual(get_scan_profiles_dir(), p("test_env/ProgramData/Kofax/Kofax Express 3.2/Jobs"))


if __name__ == "__main__":
    unittest.main()
