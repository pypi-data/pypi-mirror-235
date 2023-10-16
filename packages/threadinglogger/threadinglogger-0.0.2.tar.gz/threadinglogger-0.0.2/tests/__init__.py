import unittest
import threadinglogger

class TestClass(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        threadinglogger.init_file_writer('unittest', '../logs')
        threadinglogger.start()
        threadinglogger.information('a', 'b')
        
    @classmethod
    def tearDownClass(cls) -> None:
        threadinglogger.change_write_format("{date_str} {log_type:{log_type_length}} {thread_id:0{thread_id_length}d} [ChangeFormat] {text}")
        threadinglogger.information("tearDownClass stop")
        threadinglogger.stop()
        
    def test_running(self):
        self.assertTrue(threadinglogger.is_running())
        self.assertTrue(threadinglogger.is_print_console())

if __name__ == '__main__':
    unittest.main()