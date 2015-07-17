from app.views import app
import unittest


class TestCaseMethods(unittest.TestCase):

    def setUp(self):
        tester = app.test_client(self)
        test_file = 'tester.yaml'
        response = tester.post('/on-board-nsd',
                               data={'nsd_file': open(test_file)})
        self.assertEqual(response.status_code, 200)
        expected_msg = 'SUCCESS'
        self.assertEqual(response.data, expected_msg)

    def tearDown(self):
        tester = app.test_client(self)
        filename_version = 'tester.yaml_1.0'
        response = tester.post('/delete-nsd',
                               data={'nsd_name_version': filename_version})
        self.assertEqual(response.status_code, 200)
        expected_msg = 'NSD Deleted'
        self.assertEqual(response.data, expected_msg)

    def test_no_input_nsd(self):
        tester = app.test_client(self)
        response = tester.post('/on-board-nsd', data={})
        self.assertEqual(response.status_code, 200)
        expected_msg = 'An error with input parameter.'
        self.assertEqual(response.data, expected_msg)

    def test_wrong_input_nsd(self):
        tester = app.test_client(self)
        filename_version = 'tester.yaml'
        response = tester.post('/on-board-nsd',
                               data={'filedat': open(filename_version)})
        self.assertEqual(response.status_code, 200)
        expected_msg = 'An error with input parameter.'
        self.assertEqual(response.data, expected_msg)

    def test_not_allowed_file_nsd(self):
        tester = app.test_client(self)
        test_file = 'tester.py'
        response = tester.post('/on-board-nsd',
                               data={'nsd_file': open(test_file)})
        self.assertEqual(response.status_code, 200)
        expected_msg = 'tester.py is not a "yaml" file.'
        self.assertEqual(response.data, expected_msg)

    def test_enable_and_disable_NSD(self):
        tester = app.test_client(self)
        filename_version = 'tester.yaml_1.0'
        response = tester.post('/enable-nsd',
                               data={'nsd_name_version': filename_version})
        self.assertEqual(response.status_code, 200)
        expected_msg = "NSD Enabled"
        self.assertEqual(response.data, expected_msg)
        response = tester.post('/enable-nsd',
                               data={'nsd_name_version': filename_version})
        self.assertEqual(response.status_code, 200)
        expected_msg = "NSD is already Enabled"
        self.assertEqual(response.data, expected_msg)
        response = tester.post('/disable-nsd',
                               data={'nsd_name_version': filename_version})
        self.assertEqual(response.status_code, 200)
        expected_msg = "NSD Disabled"
        self.assertEqual(response.data, expected_msg)
        response = tester.post('/disable-nsd',
                               data={'nsd_name_version': filename_version})
        self.assertEqual(response.status_code, 200)
        expected_msg = "NSD is already Disabled"
        self.assertEqual(response.data, expected_msg)

    def test_no_input_enable_nsd(self):
        tester = app.test_client(self)
        response = tester.post('/enable-nsd', data={})
        self.assertEqual(response.status_code, 200)
        expected_msg = 'An error with input parameter.'
        self.assertEqual(response.data, expected_msg)

    def test_wrong_nsd_name_version_enable_nsd(self):
        tester = app.test_client(self)
        filename_version = 'tester.yaml_1.0'
        response = tester.post('/enable-nsd',
                               data={'nsd_name_vesion': filename_version})
        self.assertEqual(response.status_code, 200)
        expected_msg = 'An error with input parameter.'
        self.assertEqual(response.data, expected_msg)

    def test_no_package_enable_nsd(self):
        tester = app.test_client(self)
        filename_version = 'test.yaml_1.0'
        response = tester.post('/enable-nsd',
                               data={'nsd_name_version': filename_version})
        self.assertEqual(response.status_code, 200)
        expected_msg = 'No NSD of given ID is found'
        self.assertEqual(response.data, expected_msg)

    def test_no_input_disable_nsd(self):
        tester = app.test_client(self)
        response = tester.post('/disable-nsd', data={})
        self.assertEqual(response.status_code, 200)
        expected_msg = 'An error with input parameter.'
        self.assertEqual(response.data, expected_msg)

    def test_wrong_nsd_name_version_disable_nsd(self):
        tester = app.test_client(self)
        filename_version = 'tester.yaml_1.0'
        response = tester.post('/disable-nsd',
                               data={'nsd_name_vesion': filename_version})
        self.assertEqual(response.status_code, 200)
        expected_msg = 'An error with input parameter.'
        self.assertEqual(response.data, expected_msg)

    def test_no_package_disable_nsd(self):
        tester = app.test_client(self)
        filename_version = 'test.yaml_1.0'
        response = tester.post('/disable-nsd',
                               data={'nsd_name_version': filename_version})
        self.assertEqual(response.status_code, 200)
        expected_msg = 'No NSD of given ID is found'
        self.assertEqual(response.data, expected_msg)

    def test_update_nsd(self):
        tester = app.test_client(self)
        test_file = 'tester.yaml'
        response = tester.post('/update-nsd',
                               data={'nsd_file': open(test_file)})
        self.assertEqual(response.status_code, 200)
        expected_msg = 'NSD Updated'
        self.assertEqual(response.data, expected_msg)
        filename_version = 'tester.yaml_2.0'
        response = tester.post('/delete-nsd',
                               data={'nsd_name_version': filename_version})

    def test_no_input_update_nsd(self):
        tester = app.test_client(self)
        response = tester.post('/update-nsd', data={})
        self.assertEqual(response.status_code, 200)
        expected_msg = 'An error with input parameter.'
        self.assertEqual(response.data, expected_msg)

    def test_wrong_input_update_nsd(self):
        tester = app.test_client(self)
        filename_version = 'tester.yaml'
        response = tester.post('/update-nsd',
                               data={'filedat': open(filename_version)})
        self.assertEqual(response.status_code, 200)
        expected_msg = 'An error with input parameter.'
        self.assertEqual(response.data, expected_msg)

    def test_not_allowed_file_update_nsd(self):
        tester = app.test_client(self)
        test_file = 'tester.py'
        response = tester.post('/update-nsd',
                               data={'nsd_file': open(test_file)})
        self.assertEqual(response.status_code, 200)
        expected_msg = 'tester.py is not a "yaml" file.'
        self.assertEqual(response.data, expected_msg)

    def test_no_input_query_nsd(self):
        tester = app.test_client(self)
        response = tester.post('/query-nsd', data={})
        self.assertEqual(response.status_code, 200)
        expected_msg = 'An error with input parameter.'
        self.assertEqual(response.data, expected_msg)

    def test_wrong_nsd_name_version_query_nsd(self):
        tester = app.test_client(self)
        filename_version = 'tester.yaml_1.0'
        response = tester.post('/query-nsd',
                               data={'nsd_name_vesion': filename_version})
        self.assertEqual(response.status_code, 200)
        expected_msg = 'An error with input parameter.'
        self.assertEqual(response.data, expected_msg)

    def test_no_package_query_nsd(self):
        tester = app.test_client(self)
        filename_version = 'test.yaml_1.0'
        response = tester.post('/query-nsd',
                               data={'nsd_name_version': filename_version})
        self.assertEqual(response.status_code, 200)
        expected_msg = 'No NSD of given ID is found'
        self.assertEqual(response.data, expected_msg)

    def test_no_input_delete_nsd(self):
        tester = app.test_client(self)
        response = tester.post('/delete-nsd', data={})
        self.assertEqual(response.status_code, 200)
        expected_msg = 'An error with input parameter.'
        self.assertEqual(response.data, expected_msg)

    def test_wrong_nsd_name_version_delete_nsd(self):
        tester = app.test_client(self)
        filename_version = 'tester.yaml_1.0'
        response = tester.post('/delete-nsd',
                               data={'nsd_name_vesion': filename_version})
        self.assertEqual(response.status_code, 200)
        expected_msg = 'An error with input parameter.'
        self.assertEqual(response.data, expected_msg)

    def test_no_package_delete_nsd(self):
        tester = app.test_client(self)
        filename_version = 'test.yaml_1.0'
        response = tester.post('/delete-nsd',
                               data={'nsd_name_version': filename_version})
        self.assertEqual(response.status_code, 200)
        expected_msg = 'No NSD of given id is found.'
        self.assertEqual(response.data, expected_msg)


if __name__ == '__main__':
    unittest.main()
