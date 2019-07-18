from unittest import TestCase
from ukpostcodeverifier import UKPostCodeVerifier

class TestUKPostCodeVerifier(TestCase):

    # testing with default values
    def test_valid_postcode(self):
        postcode='SW1W 0NY'
        verifier=UKPostCodeVerifier()
        result=verifier.verify(postcode)
        self.assertTrue(result)

    #testing invalid postcode
    def test_invalid_postcode(self):

        postcode = 'BB BBY'
        verifier = UKPostCodeVerifier()
        result = verifier.verify(postcode)
        self.assertFalse(result)
        # with self.assertRaises( ValueError) as valueEx:
        #       verifier.verify(postcode)

        # self.assertIsNotNone(valueEx.exception)