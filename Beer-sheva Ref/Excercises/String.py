class String(str):
    def base64(self) -> 'String':
        '''
        Encode the String (self) to a base64 string
        :return: a new instance of String with the encoded string.
        '''
        raise NotImplemented
    def byte_pair_encoding(self) -> 'String':
        '''
        Encode the String (self) to a byte pair string
        :return: a new instance of String with the encoded string.
        :exception: BytePairError
        '''
        raise NotImplemented
    def cyclic_bits(self, num: int) -> 'String':
        '''
        Encode the String (self) to a cyclic bits string
        :return: a new instance of String with the encoded string.
        '''
        raise NotImplemented
    def cyclic_chars(self, num:int ) -> 'String':
        '''
        Encode the String (self) to a cyclic chars string
        :return: a new instance of String with the encoded string.
        :exception: CyclicCharsError
        '''
        raise NotImplemented
    def histogram_of_chars(self) -> dict:
        '''
        calculate the histogram of the String (self). The bins are
        "control code", "digits", "upper", "lower" , "other printable"
        and "higher than 128".
        :return: a dictonery of the histogram. keys are bins.
        '''
        raise NotImplemented
    def decode_base64(self) -> 'String':
        '''
        Decode the String (self) to its original base64 string.
        :return: a new instance of String with the endecoded string.
        :exception: Base64DecodeError
        '''
        raise NotImplemented
    def decode_byte_pair(self) -> 'String':
        '''
        Decode the String (self) to its original byte pair string.
        Uses the property rules.
        :return: a new instance of String with the endecoded string.
        :exception: BytePairDecodeError
        '''
        raise NotImplemented
    def decode_cyclic_bits(self) -> 'String':
        '''
        Decode the String (self) to its original cyclic bits string.
        :return: a new instance of String with the endecoded string.
        '''
        raise NotImplemented
    def decode_cyclic_chars(self) -> 'String':
        '''
        Decode the String (self) to its original cyclic chars string.
        :return: a new instance of String with the endecoded string.
        :exception: CyclicCharsDecodeError
        '''
        raise NotImplemented

