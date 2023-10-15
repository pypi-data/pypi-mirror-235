"""User mutations."""

from typing import Any, Dict, Literal, Optional

from typeguard import typechecked

from kili.entrypoints.base import BaseOperationEntrypointMixin
from kili.entrypoints.mutations.user.queries import (
    GQL_CREATE_USER,
    GQL_UPDATE_PASSWORD,
    GQL_UPDATE_PROPERTIES_IN_USER,
)


class MutationsUser(BaseOperationEntrypointMixin):
    """Set of User mutations."""

    # pylint: disable=too-many-arguments
    @typechecked
    def create_user(
        self,
        email: str,
        password: str,
        organization_role: str,
        firstname: Optional[str] = None,
        lastname: Optional[str] = None,
    ) -> Dict[Literal["id"], str]:
        """Add a user to your organization.

        Args:
            email: Email of the new user, used as user's unique identifier.
            password: On the first sign in, he will use this password and be able to change it.
            organization_role: One of "ADMIN", "USER".
            firstname: First name of the new user.
            lastname: Last name of the new user.

        Returns:
            A dictionary with the id of the new user.
        """
        variables = {
            "data": {
                "email": email,
                "password": password,
                "organizationRole": organization_role,
            }
        }
        if firstname is not None:
            variables["data"]["firstname"] = firstname
        if lastname is not None:
            variables["data"]["lastname"] = lastname
        result = self.graphql_client.execute(GQL_CREATE_USER, variables)
        return self.format_result("data", result)

    @typechecked
    def update_password(
        self, email: str, old_password: str, new_password_1: str, new_password_2: str
    ) -> Dict[Literal["id"], str]:
        """Allow to modify the password that you use to connect to Kili.

        This resolver only works for on-premise installations without Auth0.

        Args:
            email: Email of the person whose password has to be updated.
            old_password: The old password
            new_password_1: The new password
            new_password_2: A confirmation field for the new password

        Returns:
            A dict with the user id.
        """
        variables = {
            "data": {
                "oldPassword": old_password,
                "newPassword1": new_password_1,
                "newPassword2": new_password_2,
            },
            "where": {"email": email},
        }
        result = self.graphql_client.execute(GQL_UPDATE_PASSWORD, variables)
        return self.format_result("data", result)

    @typechecked
    def update_properties_in_user(
        self,
        email: str,
        firstname: Optional[str] = None,
        lastname: Optional[str] = None,
        organization_id: Optional[str] = None,
        organization_role: Optional[str] = None,
        activated: Optional[bool] = None,
    ) -> Dict[Literal["id"], str]:
        """Update the properties of a user.

        Args:
            email: The email is the identifier of the user.
            firstname:Change the first name of the user.
            lastname: Change the last name of the user.
            organization_id: Change the organization the user is related to.
            organization_role: Change the role of the user.
                One of "ADMIN", "TEAM_MANAGER", "REVIEWER", "LABELER".
            activated: In case we want to deactivate a user, but keep it.

        Returns:
            A dict with the user id.
        """
        variables: Dict[str, Any] = {
            "email": email,
        }
        if firstname is not None:
            variables["firstname"] = firstname
        if lastname is not None:
            variables["lastname"] = lastname
        if organization_id is not None:
            variables["organizationId"] = organization_id
        if organization_role is not None:
            variables["organizationRole"] = organization_role
        if activated is not None:
            variables["activated"] = activated
        result = self.graphql_client.execute(GQL_UPDATE_PROPERTIES_IN_USER, variables)
        return self.format_result("data", result)
