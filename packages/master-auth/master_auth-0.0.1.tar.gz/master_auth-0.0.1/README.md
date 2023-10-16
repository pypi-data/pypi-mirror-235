# master-auth

check auth use mongodb 

<!-- insert useage -->
## how to use
### save password to mongodb
```python
from master_auth import core

core.save_password(mongodb_username, mongodb_password, mongodb_host, mongodb_port, database_name,collection_name,username, password)
```

### check password from mongodb
```python
from master_auth import core

core.check_password(mongodb_username, mongodb_password, mongodb_host, mongodb_port, database_name,collection_name,username, password)
```

### update password to mongodb
```python
from master_auth import core

core.update_password(mongodb_username, mongodb_password, mongodb_host, mongodb_port, database_name,collection_name,username, password_old, password_new)
```

## v0.0.1
- [x] save password to mongodb , password is hashed
- [x] check password from mongodb , password is hashed
- [x] update password to mongodb , password is hashed