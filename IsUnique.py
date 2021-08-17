#IsUnique : Implement an Algorihm to determine if a string has all unique characters.
    #Hint: Use Hastable => Dictionary (key-value)
    
import unittest      #Unit test ( kiểm thử mức đơn vị), là thư viện kiểm thử phần mềm

def unique(str):
    char_set = {}
    for character in str:
        if character in char_set:
            return False
        char_set[character] = True
    return True

class Test(unittest.TestCase):
    data_True = [('abcd'), ('s23fde'), ('')]
    data_False = [('282'), ('abfafhh')]
    
    def test_unique(self):
        #check true
        for test_case in self.data_True:
            actualResult = unique(test_case)
            self.assertTrue(actualResult)
            
        #check False
        for test_case in self.data_False:
            actualResult = unique(test_case)
            self.assertFalse(actualResult)

def main():
    unittest.main()     #Khi chạy hàm main thì sẽ vận hành class Test -> def test_unique và chạy từng string 1 và pass vào trong hàm unique
    
main()