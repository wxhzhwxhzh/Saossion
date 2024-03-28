copy Drissionpage_code_helper.py  Drissionpage_code_helper.pyw
pyinstaller --onefile --add-data "sao.ico;." --add-data "logo.png;." --add-data "code_frame.txt;."  -i sao.ico      .\Drissionpage_code_helper.pyw
copy "%~dp0dist\Drissionpage_code_helper.exe" "%CD%\Drissionpage_code_helper.exe"
