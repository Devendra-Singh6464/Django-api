-------- Start  the server --------

- Go inside the project directory:
```
/home/deepak/Django/
```
- Activate virtual envirment server:
```
source .venv/bin/activate
```
- Enter in main directory:
```
cd main/
```
- Run the server:
```
python manage.py runserver 1404
```

---------Check data bases
- Enter in database (USER: django_user):
```
mysql -u django_user -p
```
- Password(root user name and password: root, root123): 
```
django123
```

- Check databases:
```
SHOW DATABASES;
```

- Check tables:
```
SHOW TABLES;
```

- Use database:
```
USE Blabla_DB;
```

- Select all from table:
```
SELECT * FROM auth_user;
```

- Describe table:
```
DESCRIBE auth_user;
```