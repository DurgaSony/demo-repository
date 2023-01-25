class Test_uti:
    def test_verify(self,list,toverify):
        for i in list:
            assert i.text == toverify
            print('assert pass')