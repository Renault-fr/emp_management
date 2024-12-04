echo:
echo:
@echo ----------------------
@echo   Username: admin
@echo   Password: admin
@echo ----------------------
echo:
echo:
@echo Starting server and Opening browser...
timeout /t 5 /nobreak

start "" http://127.0.0.1:8000/
python manage.py runserver 8000
pause
exit