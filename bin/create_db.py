from django.contrib.auth.models import User
a = User.objects.create_user('gutumatik', password='test123123')
b = User.objects.create_user('guruolahraga', password='test123123')
c = User.objects.create_user('guruagama', password='test123123')
d = User.objects.create_user('gurubahasaid', password='test123123')
e = User.objects.create_user('gurubahasaen', password='test123123')
a.save()
b.save()
c.save()
d.save()
e.save()

