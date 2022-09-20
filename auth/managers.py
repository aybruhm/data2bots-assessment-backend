from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(
        self, firstname: str, lastname: str, 
        email: str, username: str, password=None
    ):
        """
        This method creates a user with no priviledges.
        """

        if email is None:
            raise TypeError("User must have an email address.")

        if username is None:
            raise TypeError("User must have a username.")

        user = self.model(
            firstname=firstname,
            lastname=lastname,
            username=username,
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save()

        return user

    def create_superuser(
        self, firstname: str, lastname: str,
        username: str, email: str, password=None,
    ):
        """
        This method creates a user with admin priviledges.
        """

        if firstname is None:
            raise TypeError("User must have a lastname.")
        
        if lastname is None:
            raise TypeError("User must have a lastname.")

        if password is None:
            raise TypeError("Superuser must have a password.")

        user = self.create_user(
            firstname=firstname,
            lastname=lastname,
            email=email,
            username=username,
            password=password,
        )
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save()

        return user