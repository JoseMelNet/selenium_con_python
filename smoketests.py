from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from assertions import AssertionsTest #Importo el modulo AssertionsTest
from searchtests import SearchTests #Importo el módulo de busqueda

# Asigno los test AssertionTest y SearchTests a una nueva variable
# Incializo y cargo con TestLoader
assertions_test = TestLoader().loadTestsFromTestCase(AssertionsTest)
search_tests = TestLoader().loadTestsFromTestCase(SearchTests)

#Construccion de suite de pruebas
smoke_test = TestSuite([assertions_test, search_tests])

#Respecto a los reportes

kwargs = {
    "output": 'smoke-report'
    }

runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test)