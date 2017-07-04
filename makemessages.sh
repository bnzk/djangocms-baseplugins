
# transifex infos

# make message
# ./makemessages.sh

# push new messages to be translated
# tx push -s

# fetch new ones
cd djangocms_baseplugins
django-admin.py makemessages -l en-cy -l de -l fr -l en
cd ..