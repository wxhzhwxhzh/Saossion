copy CAPTCHA_helper.py  CAPTCHA_helper.pyw
pyinstaller --onefile         .\CAPTCHA_helper.pyw
copy "%~dp0dist\CAPTCHA_helper.exe" "%CD%\CAPTCHA_helper.exe"
