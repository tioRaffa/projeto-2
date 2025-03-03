from django.test import TestCase

from authors.forms import RegisterForm

class TestAuthorRegister(TestCase):
    
    
    def test_placeholder(self):
        form = RegisterForm()
        
        '''   FIRST NAME      '''        
        placeholder_fname = form['first_name'].field.widget.attrs['placeholder']
        self.assertEqual('Digite seu Nome', placeholder_fname)

        '''   LAST  NAME      '''        
        placeholder_lname = form['last_name'].field.widget.attrs['placeholder']
        self.assertEqual('Digite seu Último Nome', placeholder_lname)
        
        placeholder_ = form['password'].field.widget.attrs['placeholder']
        self.assertEqual('ex: Ab12345678', placeholder_)

        