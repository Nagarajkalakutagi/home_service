from service.models import *
import logging


class RegisterAuthBackend:
    def authenticate(self, email, password):
        try:
            user = MyUser.objects.get(email=email)

            if user.check_password(password):
                return user
            else:
                return None
        except Exception as e:
            logging.getLogger("error_logger").error(repr(e))
            return None

    def admin_authenticate(self, email, password):
        try:
            user = MyUser.objects.get(email=email)

            if user.is_superuser:
                print("pass")
                if user.check_password(password):
                    return {'msg': 'superuser', 'code': 200, 'obj': user}
                else:
                    return {'msg': 'invalid password', 'code': 401}
            elif user.is_staff:
                if user.check_password(password):
                    return {'msg': 'staff', 'code': 200, 'obj': user}
                else:
                    return {'msg': 'invalid password', 'code': 401}
            else:
                return {'msg': 'invalid user', 'code': 401}
        except Exception as e:
            logging.getLogger("error_logger").error(repr(e))
            return {'msg': 'invalid user', 'code': 401}

    def get_user(self, email):
        try:
            user = MyUser.objects.get(email=email)
            if user.is_active:
                return user
            return None
        except MyUser.DoesNotExist:
            logging.getLogger("error_logger").error("user with %(user_id)d not found")
            return None

    def get_phone(self, mobile):
        try:
            phone = MyUser.objects.get(mobile=mobile)
            if phone.is_active:
                return phone
            return None
        except MyUser.DoesNotExist:
            logging.getLogger("error_logger").error("user with %(user_id)d not found")
            return None
