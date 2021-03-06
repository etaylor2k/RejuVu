# encoding: utf-8

'''build
'''

__author__ = 'Chris Miles'
__copyright__ = '(c) Chris Miles 2009. All rights reserved.'
__id__ = '$Id$'
__url__ = '$URL$'


# ---- Imports ----

# - ToscaWidgets & tw.forms modules -
import tw.forms
from tw.api import WidgetsList, CSSSource, JSSource, js_function

# - RejuVu modules -
from rejuvu.model.forms.validators import UserValidators


# ---- Form Definitions ----

#
# Uses ToscaWidgets Forms (tw.forms)
#

# External css files can be wrapped with CSSLink
css = CSSSource("""
.fielderror {
    font-weight: bold;
    color: red;
};
label.required {
    font-weight: bold;
};
"""
)


# We define the source for some JS functions we're going to interface
# External js files can be wrapped with JSLink
functions = JSSource("""
var focus_element = function (elem) {
    var elem = document.getElementById(elem);
    elem.focus(); elem.select();
    }; 
    """,
)

alert = js_function('alert')
focus_element = js_function('focus_element')


# Automatically filter out any unexpected parameters
class FilteringSchema(tw.forms.validators.Schema):
    filter_extra_fields = True
    allow_extra_fields = True


#
# - Form for new user registration -
#

class RegisterUserForm(tw.forms.TableForm):
    template = "rejuvu.templates.forms.register-user"
    # hover_help = True
    
    class fields(WidgetsList):
        user_name = tw.forms.TextField(
            label_text = 'User Name',
            # help_text = '',
            required = True,
            css_classes = ['form-text'],
            attrs = {
                'maxlength': "16",
                'size': "30",
            },
            validator = UserValidators.user_name
        )
        
        display_name = tw.forms.TextField(
            label_text = 'Name',
            # help_text = 'Your Full Name',
            required = True,
            css_classes = ['form-text'],
            attrs = {
                'maxlength': "255",
                'size': "30",
            },
            validator = UserValidators.display_name
        )
        
        email_address = tw.forms.TextField(
            label_text = 'Email Address',
            # help_text = 'Your email address',
            required = True,
            css_classes = ['form-text'],
            attrs = {
                'maxlength': "255",
                'size': "30",
            },
            validator = UserValidators.email_address
        )
        
        email_address2 = tw.forms.TextField(
            label_text = 'Retype Email Address',
            # help_text = 'Retype your email address',
            required = True,
            css_classes = ['form-text'],
            attrs = {
                'maxlength': "255",
                'size': "30",
            },
            validator = tw.forms.validators.String(
                not_empty=True,
            )
        )
        
        password = tw.forms.PasswordField(
            label_text = 'Password',
            # help_text = 'The password you will use to login to the site',
            required = True,
            css_classes = ['form-text'],
            attrs = {
                'maxlength': "75",
                'size': "30",
            },
            validator = UserValidators.password
        )
        
        password2 = tw.forms.PasswordField(
            label_text = 'Retype Password',
            # help_text = 'Retype your password to confirm we have it correct',
            required = True,
            css_classes = ['form-text'],
            attrs = {
                'maxlength': "75",
                'size': "30",
            },
            validator = tw.forms.validators.String(
                not_empty = True,
            )
        )
    
    # allow adding js calls dynamically for a request
    include_dynamic_js_calls = True
    
    css = [css]
    javascript = [functions]
    validator = FilteringSchema(
        chained_validators = [
            tw.forms.validators.FieldsMatch(
                'email_address',
                'email_address2',
                messages={
                    'match': "Email addresses don't match."
                }
            ),
            tw.forms.validators.FieldsMatch(
                'password',
                'password2',
                messages={
                    'match': "Passwords don't match."
                }
            ),
        ]
    )
    
    def update_params(self, d):
        super(RegisterUserForm, self).update_params(d)
        # Focus and select the 'name' field on the form
        # The adapter we just wrote lets us pass formfields as parameters and
        # the right thing will be done.
        if not d.error:
            self.add_call(focus_element(d.c.user_name))
        ### This would show a JS alert containing details of all the validation
        ###     errors.  This is too intrusive so we don't use it.
        # else:
        #     self.add_call(
        #         alert('The form contains invalid data\n%s'% unicode(d.error))
        #     )
    

class NewClientForm(tw.forms.TableForm):
    template = "rejuvu.templates.forms.new-client"
    # hover_help = True

    class fields(WidgetsList):
        client_name = tw.forms.TextField(
            label_text = 'Client Name',
            # help_text = '',
            required = True,
            css_classes = ['form-text'],
            attrs = {
                'maxlength': "16",
                'size': "30",
            },
            validator = UserValidators.client_name
        )

    # allow adding js calls dynamically for a request
    include_dynamic_js_calls = True

    css = [css]
    javascript = [functions]
