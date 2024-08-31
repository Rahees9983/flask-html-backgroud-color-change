import unittest
import os
import tempfile
from flask import Flask
from app import app  # Import the Flask app from your app.py file

class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        # Set up the test client and app config
        self.app = app
        self.app.config['TESTING'] = True
        self.app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'uploaded_files')
        self.client = self.app.test_client()

        # Ensure the upload folder exists
        if not os.path.exists(self.app.config['UPLOAD_FOLDER']):
            os.makedirs(self.app.config['UPLOAD_FOLDER'])

    def tearDown(self):
        # Cleanup any created files and directories
        upload_folder = self.app.config['UPLOAD_FOLDER']
        for filename in os.listdir(upload_folder):
            file_path = os.path.join(upload_folder, filename)
            os.remove(file_path)
        os.rmdir(upload_folder)

    def test_main_route(self):
        """Test the main route."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello', response.data)

    def test_new_color_route(self):
        """Test the color change route."""
        response = self.client.get('/color/red')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello', response.data)
        self.assertIn(b'#e74c3c', response.data)  # Check if color red is used

    def test_read_file_route(self):
        """Test the read file route."""
        # Create a test file in the current directory
        test_file_path = os.path.join(os.getcwd(), 'testfile.txt')
        with open(test_file_path, 'w') as f:
            f.write('This is a test file.')

        # Perform the request
        response = self.client.get('/read_file')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'This is a test file.', response.data)

        # Clean up the test file
        os.remove(test_file_path)

    def test_upload_file(self):
        """Test file upload."""
        # Create a file to upload
        data = {
            'file': (tempfile.NamedTemporaryFile(delete=False), 'testfile.txt')
        }
        response = self.client.post('/upload', content_type='multipart/form-data', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'uploaded successfully', response.data)

        # Check if the file exists in the upload folder
        uploaded_file_path = os.path.join(self.app.config['UPLOAD_FOLDER'], 'testfile.txt')
        self.assertTrue(os.path.exists(uploaded_file_path))

        # Clean up
        os.remove(uploaded_file_path)

    def test_uploaded_file_access(self):
        """Test accessing an uploaded file."""
        # Create and upload a file
        filename = 'testfile.txt'
        file_content = b'This is a test file.'
        file_path = os.path.join(self.app.config['UPLOAD_FOLDER'], filename)
        with open(file_path, 'wb') as f:
            f.write(file_content)

        # Perform the request
        response = self.client.get(f'/files/{filename}')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, file_content)

        # Clean up
        os.remove(file_path)

if __name__ == '__main__':
    unittest.main()

