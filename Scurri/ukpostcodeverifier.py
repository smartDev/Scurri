import re

class UKPostCodeVerifier:

    def verify(self,postcode):
        expression = '^([A-PR-UWYZ0-9][A-HK-Y0-9][AEHMNPRTVXY0-9]?[ABEHMNPRVWXY0-9]? {1,2}[0-9][ABD-HJLN-UW-Z]{2}|GIR 0AA)$'
        valid = re.search(expression, postcode)
        return not valid is None


if __name__ == '__main__':
    verifier=UKPostCodeVerifier()
    postcode='SW1W 0NY'
    try:
        result=verifier.verify(postcode)

        if result:
            print(f"'{postcode}' is valid postcode format.")


    except ValueError as ex:
        print( ex )