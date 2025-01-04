from django.dispatch import receiver
from allauth.account.signals import user_signed_up, user_logged_in


@receiver( user_signed_up )
def create_profile( request, user, sociallogin=None, **kwargs ):
	if sociallogin:
		email = sociallogin.account.extra_data.get( 'email' )

		if email:
			user.email = email
			user.save()


@receiver( user_logged_in )
def login_user( request, user, sociallogin=None, **kwargs ):
	if sociallogin:
		print( "Provider Login" )