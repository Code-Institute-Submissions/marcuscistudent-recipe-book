# tests/test_basic.py

from app import app
import unittest
import os
import tempfile

class FlaskTestCase(unittest.TestCase):
    
    # Ensure that Flask was set up correctly
    def test_Flask_route(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        
    # Ensure that Flask index page was set up correctly
    def test_index_loads(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertTrue(b'Search Recipe By Name' in response.data)
    
     # Ensure that Flask all recipes page was set up correctly
    def test_all_recipes_loads(self):
        tester = app.test_client(self)
        response = tester.get('/get_recipes', content_type='html/text')
        self.assertTrue(b'All Recipes' in response.data)
        
     # Ensure that Flask Add Recipe page was set up correctly
    def test_add_recipe_loads(self):
        tester = app.test_client(self)
        response = tester.get('/add_recipe', content_type='html/text')
        self.assertTrue(b'Add Recipe' in response.data)
        
     # Ensure that Flask categories page was set up correctly
    def test_categories_loads(self):
        tester = app.test_client(self)
        response = tester.get('/get_categories', content_type='html/text')
        self.assertTrue(b'Categories' in response.data)
        
     # Ensure that Flask search by category page was set up correctly
    def test_category_search_loads(self):
        tester = app.test_client(self)
        response = tester.get('/category_search', content_type='html/text')
        self.assertTrue(b'Search Recipe By Category' in response.data)
        
    # Ensure that Flask add category page was set up correctly
    def test_add_category_loads(self):
        tester = app.test_client(self)
        response = tester.get('/new_category', content_type='html/text')
        self.assertTrue(b'Add Category' in response.data)
        
    # Ensure that Flask Edit category page was set up correctly
    def test_Edit_category_loads(self):
        tester = app.test_client(self)
        response = tester.get('/edit_category/<category_id>', content_type='html/text')
        self.assertTrue(b'Edit Category' in response.data)


        
        
if __name__ == '__main__':
    unittest.main()