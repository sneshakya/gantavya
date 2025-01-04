from django.shortcuts import render


def index( request ):
	return render( request, "index.html" )


def about( request ):
	return render( request, "pages/about.html" )


def after_federated_signup( request ):
	return render( request, "pages/after_federate_signup.html" )
