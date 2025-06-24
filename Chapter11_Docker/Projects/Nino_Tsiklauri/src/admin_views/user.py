from src.admin_views.base import SecureModelView
from wtforms.fields import SelectField

class UserView(SecureModelView):
    can_view_details = True
    can_edit = False
    can_create = True
    can_delete = False

    column_exclude_list = ['_password',]
    column_searchable_list = ['username', 'role']

    form_overrides = {"role": SelectField}
    form_args = {"role":{
        "choices":["Admin", "Moderator", "User"]
    }}