# OTUS-FINAL-PROJECT


source env/bin/activate


pytest --alluredir=%allure_result_folder% ./tests

allure serve %allure_result_folder%  