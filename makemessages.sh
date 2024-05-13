
# make message
# ./makemessages.sh

# fetch new ones
cd djangocms_baseplugins
django-admin.py makemessages -l de -l fr -l en
cd ..
