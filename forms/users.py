import mongoengine as me

class User(me.Document):
    meta ={'collection': 'users'}
    firstname = me.StringField()
    lastname = me.StringField()
    age = me.IntField()

me.connect('unittest_db')

new_user = User()
new_user.firstname = 'atthawit'
new_user.save()

user = User.objects()

print(user.to_json(indent=4))